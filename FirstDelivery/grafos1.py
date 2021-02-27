import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node('a')
G.add_node('b')
G.add_node('c')
G.add_node('d')
G.add_node('e')
G.add_node('f')

G.add_edge('a','b')
G.add_edge('a','d')
G.add_edge('b','c')
G.add_edge('c','e')
G.add_edge('e','f')
G.add_edge('f','c')
G.add_edge('e','d')

plt.figure(4)
nx.draw_networkx(G, pos=nx.spring_layout(G), with_labels=True)
plt.show()