#!/bin/python
"""In  this exercise, we will create an undirexted graph
with 2 nodes, and one edge between them.

The Simplest graph

G = (V, E)
V = {1, 2}
E = {{1, 2}}
"""

import networkx as nx
import matplotlib.pyplot as mp

# Create an instance of a graph
G = nx.Graph()

# add a nodes
G.add_node("a")
G.add_node("b")
G.add_node("c")
G.add_node("d")

# Add an edge to join node 1 to node 2
G.add_edge("a", "b")
G.add_edge("c", "d")

nx.draw(G, with_labels=True)
mp.show()
