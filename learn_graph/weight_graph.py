import networkx as nx
import matplotlib.pyplot as mp

G = nx.Graph()

nodes = ["A", "B", "C", "D", "E"]
G.add_nodes_from(nodes)

G.add_edge("A", "E", weight=8)
G.add_edge("C", "D", weight=15)

pos = nx.circular_layout(G)
edge_labels = nx.get_edge_attributes(G, "weight")

nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

mp.show()
