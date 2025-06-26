
# 🧱 Homellc Data Engineering Assessment – Quick Guide

This project takes a flat CSV file and loads it into a **normalized MySQL database** using **Python ETL**.

---

## ⚙️ Main Steps

### ✅ 1. Set up Python Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

### 🐳 2. Start MySQL via Docker

```bash
docker-compose -f docker-compose.initial.yml up --build -d
```

---

### 🏗️ 3. Create Tables

Run the following command to execute the SQL schema and create normalized tables inside the MySQL container:

```bash
docker exec -it mysql_ctn mysql -u db_user -p
```

> 🔒 **Note**: You'll be prompted to enter the password.

---

### 📥 4. Run ETL Script

```bash
python scripts/etl.py
```

* Reads `fake_data.csv`
* Normalizes and loads data into MySQL using foreign keys

---

### 🔍 5. Verify

```sql
SELECT COUNT(*) FROM property;
SELECT * FROM leads LIMIT 5;
```

---

## 📁 Project Structure

```
project-root/
├── sql/
│   ├── 00_init_db_dump.sql
│   └── fake_data.csv
├── scripts/
│   └── etl.py

```
