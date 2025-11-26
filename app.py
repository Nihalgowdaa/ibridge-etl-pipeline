import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
import logging
import os
import urllib.parse   # Required to encode password

# ---------- Step 1: Logging Setup ----------
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/etl_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("🚀 MySQL ETL App started successfully!")

# ---------- Step 2: Database Creation Helper ----------
def create_mysql_database(user, password, host, db_name):
    """Create database if it does not already exist."""
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        conn.close()
        logging.info(f"Database '{db_name}' verified/created successfully.")
        return True
    except Exception as e:
        logging.error(f"Database creation failed: {e}")
        st.error(f"❌ Failed to create database: {e}")
        return False

# ---------- Step 3: UI ----------
st.title("🧩 MySQL Data Extraction & Loading Tool")

file = st.file_uploader("📁 Upload File", type=["csv", "xlsx", "json"])
file_format = st.selectbox("📄 File Format", ["CSV", "Excel", "JSON"])

db_name = st.text_input("MySQL Database Name")
user = st.text_input("MySQL Username")
password = st.text_input("MySQL Password", type="password")
host = st.text_input("MySQL Host", "localhost")
table_name = st.text_input("MySQL Table Name", "etl_table")
table_name = table_name.strip().lower().replace(" ", "_")   # Auto-fix table name

# ---------- Step 4: Main Logic ----------
if st.button("🚀 Extract & Load into MySQL"):
    if not file:
        st.warning("⚠️ Please upload a file first.")
        logging.warning("No file uploaded.")
        st.stop()

    try:
        # ----------- Extract Layer -----------
        if file_format == "CSV":
            try:
                df = pd.read_csv(file, encoding="utf-8")
            except UnicodeDecodeError:
                df = pd.read_csv(file, encoding="latin1")

        elif file_format == "Excel":
            df = pd.read_excel(file)

        elif file_format == "JSON":
            df = pd.read_json(file)
            st.info("📌 Flattening nested JSON...")
            df = pd.json_normalize(df.to_dict(orient="records"))
            st.success("✅ JSON flattened successfully!")

        st.success("✅ File extracted successfully!")
        st.dataframe(df.head())
        logging.info(f"Extracted file successfully. Rows: {len(df)}")

        # ----------- TRANSFORMATION LAYER (Phase 2) -----------
        st.subheader("✨ Optional Data Transformations")
        apply_transform = st.checkbox("Enable Data Transformations")

        if apply_transform:
            st.info("🔄 Applying transformations...")

            df.dropna(how='all', inplace=True)
            df.fillna("", inplace=True)
            df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
            df.drop_duplicates(inplace=True)

            st.success("✨ Transformations applied!")
            st.dataframe(df.head())
            logging.info("Transformations applied successfully.")

        # ----------- Create Database if Missing -----------
        created = create_mysql_database(user, password, host, db_name)
        if not created:
            st.stop()

        # ----------- Load Layer -----------
        try:
            encoded_password = urllib.parse.quote(password)
            engine = create_engine(
                f"mysql+mysqlconnector://{user}:{encoded_password}@{host}/{db_name}"
            )

            df.to_sql(table_name, con=engine, if_exists="replace", index=False)

            st.success(f"✅ Data loaded into MySQL table '{table_name}' successfully!")
            logging.info(f"Loaded data into MySQL → {db_name}.{table_name}")

        except Exception as e:
            st.error(f"❌ Failed to load into MySQL: {e}")
            logging.error(f"MySQL load error: {e}")

    except Exception as e:
        st.error(f"❌ File extraction failed: {e}")
        logging.error(f"File extraction error: {e}")
