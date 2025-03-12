import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation

# Inisialisasi graf
G = nx.Graph()
entities = ["Mahasiswa", "Mata Kuliah", "Dosen"]
relations = [("Mahasiswa", "Mata Kuliah"), ("Dosen", "Mata Kuliah")]

G.add_nodes_from(entities)
G.add_edges_from(relations)

pos = nx.spring_layout(G)
fig, ax = plt.subplots()

def update(frame):
    ax.clear()
    # Gambar node secara bertahap
    for i, node in enumerate(entities):
        if i <= frame:
            nx.draw_networkx_nodes(G, pos, nodelist=[node], node_color="lightblue", node_size=2000, ax=ax)
            nx.draw_networkx_labels(G, pos, labels={node: node}, font_size=12, ax=ax)
    
    # Gambar edge secara bertahap
    edges_to_draw = relations[:frame] if frame < len(relations) else relations
    nx.draw_networkx_edges(G, pos, edgelist=edges_to_draw, ax=ax)
    
    ax.set_title("Animasi ERD", fontsize=16)
    plt.axis("off")

# Buat animasi
ani = FuncAnimation(fig, update, frames=len(entities) + len(relations), interval=1000, repeat=False)
plt.show()