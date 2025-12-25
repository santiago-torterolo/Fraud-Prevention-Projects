# SQL Fraud Audit System ⚖️

This project implements a **Rule-Based Audit System** using SQL to detect financial fraud patterns that often bypass real-time filters. It focuses on identifying **Structuring (Smurfing)** and **Velocity Abuse** in transaction logs.

## 📂 Dataset: PaySim Simulation

This project is based on the schema of the **[PaySim Mobile Money Dataset](https://www.kaggle.com/datasets/ealaxi/paysim1)**.

> **Note on Data Strategy:**
> The full PaySim dataset is ~250MB (6 million rows), which is impractical for a lightweight GitHub portfolio.
> Instead, I built a **Simulation Engine** (`src/setup_audit_db.py`) that:
>
> 1.  Replicates the exact PaySim schema (`step`, `type`, `amount`, `nameOrig`, etc.).
> 2.  Injects specific adversarial patterns (Structuring & Bots) for validation.
> 3.  Generates a local SQLite database for instant auditing.

## 🕵️‍♂️ Audit Logic

The system runs post-transaction SQL queries to flag suspicious actors:

### 1. Structuring Detection (Smurfing)

- **Goal:** Detect users evading the $10,000 reporting threshold.
- **Query:** Finds users with multiple `CASH_OUT` transactions between **$9,000 and $9,999**.
- **File:** `sql/1_structuring_alert.sql`

### 2. Velocity Abuse (Bot Activity)

- **Goal:** Detect automated scripts draining accounts.
- **Query:** Flags users executing **> 15 transactions** within a single hour (step).
- **File:** `sql/2_velocity_alert.sql`

## 🚀 How to Run

1.  **Generate the Database:**

    ```
    python src/setup_audit_db.py
    ```

    _(Creates `data/paysim_audit.db` with simulated fraud)_

2.  **Run the Audit:**
    ```
    python src/run_audit.py
    ```
    _(Executes the SQL logic and prints the detected fraud rings)_

## 🛠️ Tech Stack

- **Python:** Data generation & Orchestration
- **SQLite:** Database engine
- **Pandas:** Reporting & Data formatting
