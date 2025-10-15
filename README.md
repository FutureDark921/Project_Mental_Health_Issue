# Mental Health Trends Among University Students In PH. (Portfolio Project)

**Author:** Jeric Cabalde  
**Dataset:** `data/Student_Mental_health.csv` (uploaded)  
**Tools:** Excel (optional), Python (pandas), MySQL, Tableau

## Project Overview
This project analyzes mental health indicators among university students using a survey dataset. It demonstrates data cleaning, SQL-based analysis, and dashboard-ready outputs for Tableau — ideal for showcasing data analyst skills.

## Contents
- `data/Student_Mental_health.csv` - Original dataset (as uploaded)
- `notebooks/data_cleaning.ipynb` - A Jupyter notebook that performs ETL and preprocessing
- `sql/mysql_analysis.sql` - SQL schema and analysis queries you can run in MySQL
- `docs/tableau_dashboard_plan.md` - Step-by-step dashboard design for Tableau
- `docs/summary_report.md` - Executive summary template and findings
- `README.md` - This file

## How to run
1. (Optional) Open `notebooks/data_cleaning.ipynb` in Jupyter to run cleaning steps and produce `Student_Mental_health_CLEAN.csv`.
2. Use `sql/mysql_analysis.sql` to create the MySQL schema and load the cleaned CSV (or original CSV if you prefer to use the SQL cleaning steps inside MySQL).
3. Open Tableau and connect to `data/Student_Mental_health_CLEAN.csv` (or to your MySQL database) and follow `docs/tableau_dashboard_plan.md` to build the dashboard.

## Notes
- The original CSV header names are preserved. The cleaning notebook contains steps to standardize column names and convert Yes/No to numeric (1/0).
- If `LOAD DATA LOCAL INFILE` is disabled in your MySQL server, either enable `local_infile` or import via Workbench's import tool.
