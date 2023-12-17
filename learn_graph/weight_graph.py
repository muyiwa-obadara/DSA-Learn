import networkx as nx
import matplotlib.pyplot as mp

G = nx.Graph()

nodes = ["A", "B", "C", "D", "E"]
G.add_nodes_from(nodes)

G.add_edge("A", "E", weight=8)
G.add_edge("C", "D", weight=15)

pos = nx.circular_layout(G)


# Draw Graphs

nx.draw(G, with_labels=True)
mp.show()
