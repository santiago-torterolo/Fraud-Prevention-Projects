# Forensic Investigation: Money Laundering Detection 🕵️‍♂️

This project demonstrates an **Anti-Money Laundering (AML)** investigation framework. It leverages **Graph Theory (NetworkX)** and **SQL** to detect hidden "Smurfing" and "Structuring" patterns that traditional tabular analysis often misses.

---

## 🔍 The Scenario: "The Smurfing Ring"

A sophisticated money laundering scheme was suspected involving a classic 3-stage process:

1.  **Placement:** Multiple "money mules" depositing small amounts (structuring) just below the $3,000 reporting threshold.
2.  **Layering:** Funds being funneled into a single intermediate account to obscure their origin.
3.  **Integration:** The aggregated total moving to a final beneficiary ("The Boss").

---

## 📂 Project Structure

The project connects a SQL backend with a Python Graph visualizer.

04_Forensic_Graph_Analysis/
├── images/
│ └── evidence_flow.png # The generated evidence graph
│
├── src/
│ ├── setup_database.py # Generates synthetic Smurfing Ring data
│ └── graph_analysis.py # Runs NetworkX algorithms & plotting
│
├── README.md # Case documentation
└── requirements.txt # Dependencies (networkx, matplotlib, etc.)

---

## 📊 Forensic Evidence Analysis

The script generated the following evidence graph, visualizing the flow of illicit funds:

![Forensic Evidence Graph](evidence_flow.png)

### How to Read this Graph:

- **⚪ The "Grey" Layer (Noise):** Normal transaction noise. Represents legitimate users (`USER_X`) making small purchases at shops. Notice the unconnected, organic structure.
- **🟡 The "Gold" Layer (Mules):** A coordinated group of 12 accounts (`MULE_01` to `MULE_12`) initiating the scheme.
  - _Red Flag:_ All transfers are curiously close to the **€3,000 limit** (e.g., €2,980, €2,830).
- **🔴 The "Red" Hub (Layering):** Account `ACC_LAYER_99`.
  - _Red Flag:_ Extremely high **In-Degree Centrality** (12 incoming connections) but only 1 outgoing connection. It acts as a funnel.
- **⚫ The "Black" Target (The Boss):** Account `BOSS_ACC_001`.
  - _Red Flag:_ Receives the aggregated total (**€34,658**) in a single lump sum, completing the laundering cycle.

---

## 🚀 How to Run this Investigation

1.  **Install Requirements:**

    ```
    pip install pandas networkx matplotlib
    ```

2.  **Initialize Database (Mock Data):**
    This script creates the SQLite database and populates it with the suspicious patterns.

    ```
    python src/setup_database.py
    ```

3.  **Run Analysis & Generate Graph:**
    The forensic engine queries the DB and builds the visualization.
    ```
    python src/graph_analysis.py
    ```
    _(Output image saved to: `evidence_flow.png`)_

---

## 🛠️ Tech Stack

- **NetworkX:** Graph algorithms (Centrality, Fan-in/Fan-out metrics).
- **SQL (SQLite):** Data storage and querying.
- **Matplotlib:** Network visualization.
- **Pandas:** Data handling.

**Santiago Torterolo**
[LinkedIn Profile](https://linkedin.com/in/santiago-torterolo-5u)
