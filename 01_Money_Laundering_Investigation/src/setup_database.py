


import sqlite3
import random
import os

def create_mock_database():
    print("🛠️ [DB SETUP] Creating 'financial_records.db'...")
    
    # Path Setup
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "../data/financial_records.db")
    
    # Connect (Creates file if not exists)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        tx_id INTEGER PRIMARY KEY AUTOINCREMENT,
        source_acc TEXT,
        target_acc TEXT,
        amount REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        tx_type TEXT
    )
    ''')
    
    # Insert Data (Smurfing Scenario)
    data = []
    layer = "ACC_LAYER_99"
    boss = "BOSS_ACC_001"
    
    # 12 Mules -> Layer
    for i in range(1, 13):
        mule = f"MULE_{i:02d}"
        amt = random.uniform(2800, 2990)
        data.append((mule, layer, amt, 'Placement'))
        
    # Layer -> Boss
    total = sum(d[2] for d in data)
    data.append((layer, boss, total, 'Integration'))
    
    # Noise
    for i in range(5):
        data.append((f"USER_{i}", f"SHOP_{i}", random.uniform(20, 100), 'Normal'))
        
    cursor.executemany('INSERT INTO transactions (source_acc, target_acc, amount, tx_type) VALUES (?,?,?,?)', data)
    
    conn.commit()
    conn.close()
    print(f"✅ Database created successfully at: {db_path}")

if __name__ == "__main__":
    create_mock_database()
