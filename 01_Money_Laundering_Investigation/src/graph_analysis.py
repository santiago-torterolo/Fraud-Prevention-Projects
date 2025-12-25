import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import sqlite3
import os
import math

def run_investigation():
    print("🕵️‍♂️ [FORENSIC SYSTEM] Connecting to Financial Database...")

    # --- PATH SETUP ---
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.join(base_dir, "..")
    db_path = os.path.join(project_root, "data/financial_records.db")

    if not os.path.exists(db_path):
        print(f"❌ ERROR: Database not found at {db_path}")
        return

    # 1. CONNECT & QUERY
    conn = sqlite3.connect(db_path)
    query = "SELECT source_acc, target_acc, amount, tx_type FROM transactions WHERE amount > 0"
    df = pd.read_sql_query(query, conn)
    conn.close()

    # 2. BUILD GRAPH
    G = nx.from_pandas_edgelist(df, source='source_acc', target='target_acc', 
                               edge_attr=['amount', 'tx_type'], create_using=nx.DiGraph())

    # 3. DEFINE LAYERS
    layer_account = "ACC_LAYER_99"
    boss_account = "BOSS_ACC_001"

    for node in G.nodes():
        if "MULE" in node:
            G.nodes[node]['layer'] = 0
            G.nodes[node]['role'] = 'Mule'
        elif node == layer_account:
            G.nodes[node]['layer'] = 1
            G.nodes[node]['role'] = 'Layer'
        elif node == boss_account:
            G.nodes[node]['layer'] = 2
            G.nodes[node]['role'] = 'Boss'
        else:
            G.nodes[node]['layer'] = 3
            G.nodes[node]['role'] = 'Normal'

    # 4. VISUALIZATION
    print("   -> Generating Money Flow Chart (Corrected Colors)...")
    plt.figure(figsize=(14, 9))
    
    pos = nx.multipartite_layout(G, subset_key="layer", align='horizontal', scale=1.0)
    
    # Push Noise Down
    for node in G.nodes():
        if G.nodes[node]['role'] == 'Normal':
            x, y = pos[node]
            pos[node] = (x, y - 0.6)

    # Node Colors
    node_colors = []
    for node in G.nodes():
        role = G.nodes[node]['role']
        if role == 'Mule': node_colors.append('#FFD700')
        elif role == 'Layer': node_colors.append('#FF4B4B')
        elif role == 'Boss': node_colors.append('#000000') # BLACK
        else: node_colors.append('#E0E0E0')

    nx.draw_networkx_nodes(G, pos, node_size=1600, node_color=node_colors, edgecolors='black')
    
    # Edge Colors & Style
    edge_colors = ['red' if d.get('tx_type') != 'Normal' else '#CCCCCC' for u,v,d in G.edges(data=True)]
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors, arrowsize=20, width=2.0, connectionstyle='arc3,rad=0.1')
    
    # --- LABELS FIX (White Text for Black Node) ---
    labels_boss = {n: n for n in G.nodes() if n == boss_account}
    labels_rest = {n: n for n in G.nodes() if n != boss_account}
    
    nx.draw_networkx_labels(G, pos, labels=labels_boss, font_size=8, font_weight="bold", font_color="white")
    nx.draw_networkx_labels(G, pos, labels=labels_rest, font_size=8, font_weight="bold", font_color="black")

    # Edge Amounts
    labels = { (u,v): f"€{d['amount']:.0f}" for u,v,d in G.edges(data=True) if d.get('tx_type') != 'Normal' }
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=7, label_pos=0.7)

    plt.title("Money Flow Analysis: Placement -> Layering -> Integration", fontsize=16, fontweight='bold')
    plt.axis('off')
    
    output_path = os.path.join(project_root, "evidence_flow.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✅ Evidence saved to: {output_path}")

if __name__ == "__main__":
    run_investigation()
