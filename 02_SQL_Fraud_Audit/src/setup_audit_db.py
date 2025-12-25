


import sqlite3
import pandas as pd
import random
import os

def setup_paysim_db():
    print("🛠️ [PaySim SETUP] Generating High-Fidelity Audit Database...")
    
    # Define database path (relative to this script)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "../data/paysim_audit.db")
    
    # Ensure data directory exists
    if not os.path.exists(os.path.dirname(db_path)):
        os.makedirs(os.path.dirname(db_path))

    # 1. GENERATE SYNTHETIC DATA (Mimicking PaySim Schema)
    data = []
    
    # --- SCENARIO A: Structuring (Smurfing) ---
    # Logic: User 'C_SMURF_01' withdraws amounts just below the $10,000 threshold
    print("   -> Injecting 'Structuring' patterns (Smurfing)...")
    for i in range(5):
        data.append({
            'step': 12, # Hour 12
            'type': 'CASH_OUT', 
            'amount': 9900.00 + random.uniform(10, 80),
            'nameOrig': 'C_SMURF_01', 
            'oldbalanceOrg': 100000, 'newbalanceOrig': 90000,
            'nameDest': 'M_CASINO_88', 
            'oldbalanceDest': 0, 'newbalanceDest': 9900, 
            'isFraud': 0 # System has not flagged it yet
        })

    # --- SCENARIO B: Velocity Abuse (Bot Attack) ---
    # Logic: User 'C_BOT_99' executes rapid small transfers in a single hour
    print("   -> Injecting 'Velocity' patterns (Bot Attack)...")
    for i in range(25):
        data.append({
            'step': 14, # Hour 14
            'type': 'PAYMENT', 
            'amount': 50.00,
            'nameOrig': 'C_BOT_99', 
            'oldbalanceOrg': 5000, 'newbalanceOrig': 4000,
            'nameDest': f"M_SHOP_{i}", 
            'oldbalanceDest': 0, 'newbalanceDest': 0, 
            'isFraud': 0
        })

    # --- SCENARIO C: Normal Traffic (Background Noise) ---
    print("   -> Generating background noise...")
    for i in range(200):
        data.append({
            'step': random.randint(1, 24), 
            'type': random.choice(['PAYMENT', 'CASH_IN', 'TRANSFER']), 
            'amount': round(random.uniform(10, 5000), 2),
            'nameOrig': f"C{random.randint(10000,99999)}", 
            'oldbalanceOrg': 10000, 'newbalanceOrig': 9000,
            'nameDest': f"M{random.randint(10000,99999)}", 
            'oldbalanceDest': 0, 'newbalanceDest': 0, 
            'isFraud': 0
        })

    df = pd.DataFrame(data)
    
    # 2. LOAD INTO SQLITE
    conn = sqlite3.connect(db_path)
    df.to_sql('paysim_transactions', conn, if_exists='replace', index=False)
    conn.close()
    
    print(f"✅ Database successfully created at: {db_path}")
    print(f"   Total Records: {len(df)}")
    print("   Schema Compliance: PaySim (step, type, amount, nameOrig...)")

if __name__ == "__main__":
    setup_paysim_db()
