# Executive Risk Dashboard 📊

**Strategic Monitoring of Compliance & Financial Exposure**

This project delivers a high-level command center designed for **C-Level Executives** and **Heads of Compliance**. It moves beyond transactional details to visualize aggregate risk exposure, blockage efficiency, and global fraud hotspots.

### 🚀 [View Live Dashboard on Tableau Public](https://public.tableau.com/views/ExecutiveRiskDashboard/ExecutiveRiskMonitorQ42024?:language=es-ES&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

---

## 🖼️ Dashboard Preview

![Dashboard Preview](assets/dashboard_preview.png)
_Snapshot of the Executive Risk Monitor showing real-time exposure and critical alerts._

---

## 🎯 Business Objectives

The dashboard answers three critical strategic questions:

1.  **Financial Impact:** What is the total monetary value of fraud prevented by our compliance rules?
2.  **Operational Load:** What is the volume of transactions held for manual review vs. automated blocking?
3.  **Geo-Risk:** Which jurisdictions (e.g., Offshore Zones) are generating the highest risk traffic?

## 📊 Key Performance Indicators (KPIs)

- **Total Fraud Prevented (BAN):** Aggregate EUR value of transactions with `Status = BLOCKED_COMPLIANCE`.
- **Risk Distribution:** Breakdown of traffic into _Approved_, _Manual Review_, and _Blocked_.
- **Regional Exposure:** Heatmap identifying high-value attack vectors by geography.

---

## 🛠️ Technical Implementation & Logic

### 1. Risk Logic Architecture

The following diagram illustrates the decision flow from transaction input to final status (Approve/Block/Review), utilizing both Rule-Based engines and ML Scoring.

![Risk Logic Diagram](assets/logical_diagram.png)

### 2. Data Simulation Engine

The data is generated via a custom Python script (`src/generate_viz_data.py`) that simulates realistic Q4 financial traffic patterns:

- **Transaction Types:** SWIFT, ACH, WIRE, Internal Transfers.
- **Scenarios:** "Whales" (High value/High risk), "Structuring" (Smurfing), and Compliance Blocks.

---

## 📂 Project Structure

03_Executive_Risk_Dashboard/
├── data/
│ └── executive_risk_data.csv # The primary dataset used for the dashboard
├── src/
│ └── generate_viz_data.py # Python script for synthetic data generation
├── assets/
│ ├── dashboard_preview.png # Screenshot of the final dashboard
│ └── logical_diagram.png # Architecture of the risk model
├── Tableau/
│ └── Executive_Risk_Workbook.twbx # Local backup of the Tableau workbook
└── README.md # Project documentation

---

## 📬 Contact & Feedback

This dashboard is part of a broader **Fraud Prevention Project**. If you have questions about the risk logic or the data generation process, feel free to reach out.

**Santiago Torterolo**
[LinkedIn Profile](https://linkedin.com/in/santiago-torterolo-5u)
