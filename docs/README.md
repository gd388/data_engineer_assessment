# Data Engineering Assessment

Welcome! This exercise is designed to evaluate your core skills in **data engineering**:

- **SQL databases**: Data modeling, normalization, and scripting
- **Python and ETL**: Data cleaning, transformation, and loading workflows

---

## 📚 How This Document Works

Each section is structured with:

- **Problem:** Background and context for the task
- **Task:** What you are required to do (including any bonus “extra” tasks)
- **Solution:** Where you must document your approach, decisions, and provide instructions for reviewers

> **Tech Stack:**  
> Please use only Python (for ETL/data processing) and SQL/MySQL (for database).  
> Only use extra libraries if they do not replace core logic, and clearly explain your choices in your solution.

---

## 0. Setup

1. **Fork and clone this repository:**
    ```bash
    git clone https://github.com/<your-username>/homellc_data_engineer_assessment_skeleton.git
    ```
2. **Start the MySQL database in Docker:**
    ```bash
    docker-compose -f docker-compose.initial.yml up --build -d
    ```
    - Database is available on `localhost:3306`
    - Credentials/configuration are in the Docker Compose file
    - **Do not change** database name or credentials

3. For MySQL Docker image reference:  
   [MySQL Docker Hub](https://hub.docker.com/_/mysql)

---

### Problem

You are provided with property-related data in a CSV file.
- Each row relates to a property.
- There are multiple Columns related to this property.
- The database is not normalized and lacks relational structure.


### Task

- **Normalize the data:**
  - Develop a Python ETL script to read, clean, transform, and load   data into your normalized MySQL tables.
  - Refer the field config document for the relation of business logic
  - Use primary keys and foreign keys to properly capture relationships

- **Deliverable:**
  - Write necessary python and sql scripts
  - Place the scripts inside the `sql/` directory)
  - The scripts should take the initial csv to your final, normalized schema when executed
  - Clearly document how to run your script, dependencies, and how it integrates with your database.

**Tech Stack:**  
- Python (include a `requirements.txt`)
Use **MySQL** and SQL for all database work  
- You may use any CLI or GUI for development, but the final changes must be submitted as python/ SQL scripts 
- **Do not** use ORM migrations—write all SQL by hand

### Solution

> **Document your database design and solution here:**  
> - Explain your schema and any design decisions  
> - Give clear instructions on how to run and test your script

> **Document your ETL logic here:**  
> - Outline your approach and design  
> - Provide instructions and code snippets for running the ETL  
> - List any requirements

---

## Submission Guidelines

- Edit this README with your solutions and instructions for each section
- Place all scripts/code in their respective folders (`sql/`, `scripts/`, etc.)
- Ensure all steps are fully **reproducible** using your documentation

---

**Good luck! We look forward to your submission.**



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

* Host: `localhost`, Port: `3306`
* User: `db_user`, Password: `6equj5_db_user`
* DB: `home_db`

---

### 🏗️ 3. Create Tables

Run the following command to execute the SQL schema and create normalized tables inside the MySQL container:

```bash
docker exec -i mysql_ctn mysql -u db_user -p home_db < sql/00_init_db_dump.sql
```

> 🔒 **Note**: You'll be prompted to enter the password.
> If you're scripting or using environment variables, consider using a `.env` file or Docker secrets for secure credential handling.


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
sql/
  ├── 00_init_db_dump.sql
  └── fake_data.csv
  └── etl.py
requirements.txt
docker-compose.initial.yml
Dockerfile.initial_db
```
