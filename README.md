# 🧩 Data Extraction & Loading Tool (ETL Component)

A lightweight ETL tool built using Python to automate extracting structured data from CSV, Excel, and JSON files and loading them directly into a MySQL database.  
This tool serves as the **Extraction + Loading** phases of the ETL pipeline, with an optional **Transformation Layer (Phase 2)**.

---

# 🚀 Features
- Upload CSV, Excel, JSON files  
- Extract data using Pandas  
- Optional Transformation Layer  
- Auto-create MySQL database if missing  
- Load data into SQL table using SQLAlchemy  
- Detailed error handling and logging  
- Simple Streamlit UI  

---

# 🛠️ Tech Stack
- Python 3.x  
- Streamlit  
- Pandas  
- SQLAlchemy  
- mysql-connector-python  
- MySQL Database  

---

# 📐 Architecture
```
UI → Extraction (Pandas) → Transformation → Loading (SQLAlchemy) → Logging
```

---

# 📦 Installation

```bash
pip install streamlit pandas sqlalchemy mysql-connector-python
```

---

# ▶️ Running the Application

```bash
streamlit run app.py
```

---

# 🧑‍💻 Usage Instructions

1. Launch the app using Streamlit  
2. Upload a file (CSV / Excel / JSON)  
3. Select the file format  
4. Enter MySQL database details  
5. Click **Extract & Load into MySQL**  
6. View data preview & success message  
7. Check MySQL Workbench for loaded table  

---

# ✨ Transformation Layer (Phase 2 – Optional)

The optional transformation module includes:

- Remove empty rows  
- Replace NaN with blanks  
- Convert column names to lowercase  
- Replace spaces with underscores  
- Drop duplicate rows  

---

# 📁 Project Structure

```
project-folder/
│
├── app.py                     # Main Streamlit application
├── logs/
│   └── etl_log.txt            # Logs for ETL operations
│
├── README.md                  # Project documentation
├── requirements.txt           # Dependencies (optional)
└── sample_data/               # (Optional) Test files
```

---

# 📸 Screenshots (Add your own)

```
![UI Screenshot](screenshots/ui.png)
![MySQL Table](screenshots/mysql_table.png)
```

---

# 🤝 Contribution Guidelines

1. Fork the repository  
2. Create a new branch  
3. Commit your changes  
4. Submit a pull request  

---

# 📜 License

MIT License  
Free to use, modify, and distribute.

---

# 🧑‍🎓 Author

**Nagarjun H R**  
B.Tech CSE — Malnad College of Engineering  
Aspirant in Data Science & AI  

