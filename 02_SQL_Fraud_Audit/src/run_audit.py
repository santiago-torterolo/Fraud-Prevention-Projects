


import sqlite3
import pandas as pd
import os

def run_paysim_audit():
    print("🔍 [AUDIT SYSTEM] Running Post-Transaction SQL Analysis...")
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "../data/paysim_audit.db")
    
    if not os.path.exists(db_path):
        print("❌ Error: DB not found. Run 'setup_audit_db.py' first.")
        return

    conn = sqlite3.connect(db_path)

    # --- RULE 1: STRUCTURING DETECTION (Smurfing) ---
    # Objective: Identify accounts moving significant funds via small CASH_OUTs
    # Threshold: Amounts between 9,000 and 9,999 (avoiding 10k reporting limit)
    print("\n[ALERT 1] Scanning for Structuring (Smurfing < $10k Limit)...")
    
    query_structuring = """
    SELECT 
        nameOrig as User_ID, 
        COUNT(*) as Tx_Count, 
        SUM(amount) as Total_Laundered
    FROM paysim_transactions
    WHERE type = 'CASH_OUT' 
      AND amount BETWEEN 9000 AND 9999
    GROUP BY nameOrig
    HAVING Tx_Count >= 3
    ORDER BY Total_Laundered DESC
    """
    
    df_struct = pd.read_sql_query(query_structuring, conn)
    print(df_struct if not df_struct.empty else "No anomalies found.")

    # --- RULE 2: HIGH VELOCITY DETECTION (Bots) ---
    # Objective: Detect automated scripts executing high volume of transactions
    # Threshold: > 15 transactions within a single time step (1 hour)
    print("\n[ALERT 2] Scanning for Velocity Abuse (>15 TXs/Hour)...")
    
    query_velocity = """
    SELECT 
        nameOrig as User_ID, 
        step as Hour_Step, 
        COUNT(*) as Velocity_Count
    FROM paysim_transactions
    GROUP BY nameOrig, step
    HAVING Velocity_Count > 15
    ORDER BY Velocity_Count DESC
    """
    
    df_vel = pd.read_sql_query(query_velocity, conn)
    print(df_vel if not df_vel.empty else "No anomalies found.")
    
    conn.close()
    print("\n✅ SQL Audit Finished. Report Generated.")

if __name__ == "__main__":
    run_paysim_audit()
