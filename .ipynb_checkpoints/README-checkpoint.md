`README.md` file for **Mobile Payments ETL Project** using **Python**, **Pandas**, and **SQLite (DB Browser)**.

---

```markdown
# 📊 Mobile Payments ETL Pipeline using Python, Pandas, and SQLite

## 🧾 Project Overview

This project implements a complete **ETL (Extract, Transform, Load)** pipeline for **Mobile Payments Data** using Python, Pandas, and SQLite. The dataset contains mobile transaction metrics such as active agents, registered accounts, and transaction volumes and values collected over multiple years. This pipeline cleans, transforms, and loads the data into a SQLite database, enabling fast access, analysis, and reporting.

> **Target Users**: Beginners in SQL, Data Science, and ETL workflows who want a real-world project using Python and SQLite (DB Browser for SQLite).

---

## 🧠 Problem Statement

**Title**: Building a Full ETL Pipeline for Mobile Payments Data Using Python, Pandas, and SQLite

### Context

The adoption of mobile money services has grown exponentially. Organizations need clean and structured data to analyze these trends. This dataset offers insights into mobile financial activity in Kenya over time.

### Challenge

The challenge is to build a reliable ETL pipeline that:
- **Extracts** data from a raw CSV file
- **Transforms** it into a structured format
- **Loads** it into a local SQLite database
- **Validates** the results
- **Provides insights** using SQL or Python

---

## 🎯 Objectives

1. **Extract** data from the CSV file, ensuring correct parsing.
2. **Clean** and **Transform** the data (missing values, data types, formatting).
3. **Load** the processed data into a SQLite database (`mobile_payments.db`).
4. **Validate** the inserted data.
5. Perform **basic analysis** or verification queries.

---

## 📁 Project Structure

```

ETL/
├── data/
│   └── MOBILE\_PAYMENTS.csv
├── etl\_mobile\_payments\_sqlite.ipynb
├── mobile\_payments.db
└── README.md

````

---

## ⚙️ Requirements

- Python 3.8+
- pandas
- sqlite3 (built-in with Python)
- Jupyter Notebook (optional, for interactive exploration)
- DB Browser for SQLite (for GUI inspection)

Install requirements:
```bash
pip install pandas
````

---

## 🔄 ETL Pipeline Breakdown

### 🔹 1. Extract

* Load the dataset using `pandas.read_csv()`
* Handle encoding issues (e.g., BOM characters)
* Preview the dataset and column names

### 🔹 2. Transform

* Strip whitespace from column names
* Rename columns to be SQL-compatible if needed
* Drop or impute missing values
* Generate new features like `year_month`

### 🔹 3. Load

* Connect to SQLite (`sqlite3.connect`)
* Create the table if it doesn't exist
* Insert each row into the SQLite database
* Commit and close the connection

### 🔹 4. Validate

* Run a SELECT query to inspect the inserted data
* Use `pandas.DataFrame` to display queried results

### 🔹 5. Analysis & Insights (Optional)

* Aggregate monthly or yearly transaction volume/value
* Top 5 months with highest agent activity
* Growth trends over time

---

## 📝 Sample SQL Table Schema

```sql
CREATE TABLE mobile_payments (
    year INTEGER,
    month INTEGER,
    "Active Agents" INTEGER,
    "Total Registered Mobile Money Accounts (Millions)" REAL,
    "Total Agent Cash in Cash Out (Volume Million)" REAL,
    "Total Agent Cash in Cash Out (Value KSh billions)" REAL,
    year_month TEXT
);
```

---

## 🧪 Example Jupyter Output

| year | month | Active Agents | Total Registered Mobile Money Accounts (Millions) | Total Agent Cash in Cash Out (Volume Million) | Total Agent Cash in Cash Out (Value KSh billions) | year\_month |
| ---- | ----- | ------------- | ------------------------------------------------- | --------------------------------------------- | ------------------------------------------------- | ----------- |
| 2020 | 1     | 215000        | 33.4                                              | 188.2                                         | 245.6                                             | 2020-01     |

---

## 📊 Sample Insights

```sql
-- Monthly totals of cash-in/cash-out
SELECT year_month, 
       SUM("Total Agent Cash in Cash Out (Value KSh billions)") AS total_value
FROM mobile_payments
GROUP BY year_month
ORDER BY total_value DESC
LIMIT 5;
```

---

## 💡 Key Learnings

* How to build a real-world ETL pipeline from scratch
* Data cleaning and preprocessing in pandas
* Loading structured data into a SQL database (SQLite)
* Validating and querying data using SQL
* Using DB Browser for GUI exploration

---

## 🧰 Tools Used

* **Python 3.11**
* **pandas**: Data handling and transformation
* **sqlite3**: Database interaction
* **DB Browser for SQLite**: Visual database inspection

---

## ✅ How to Run

1. Clone the repository or copy files to a local folder.
2. Launch Jupyter Notebook or run the script.
3. Make sure the CSV file is in the correct `data/` folder.
4. Run the notebook: `etl_mobile_payments_sqlite.ipynb`
5. Open `mobile_payments.db` in DB Browser to inspect the table.

---

## 🔐 Data Source

The dataset is assumed to be public and anonymized, containing no sensitive user-level information.

---

## 🧩 Author

**Daniel Wanjala Machimbo**
Machine Learning Engineer & Data Scientist
📧 [dmwanjala254@gmail.com](mailto:dmwanjala254@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/daniel-wanjala-91)

---

## 📌 License

MIT License.

---

## 📞 Support

For any issues, reach out via [email](mailto:dmwanjala254@gmail.com) or [LinkedIn](https://www.linkedin.com/in/daniel-wanjala-91).

```
