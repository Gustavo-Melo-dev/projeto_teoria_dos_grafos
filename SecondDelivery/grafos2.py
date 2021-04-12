import networkx as nx
import matplotlib.pyplot as plt

E = nx.Graph()

vertex = ['V1','V2','V3','V4','V5','V6']

for vertex in E.graph:
  E.add_node(vertex)

E.add_edge('v1', 'v2')
E.add_edge('v2', 'v3')
E.add_edge('v3', 'v1')
E.add_edge('v4', 'v5')
E.add_edge('v6', 'v5')
E.add_edge('v6', 'v4')


G = nx.Graph()

vertex = ['V1','V2','V3']

for vertex in G.graph:
  G.add_node(vertex)

G.add_edge('v1', 'v2')
G.add_edge('v2', 'v3')
G.add_edge('v3', 'v1')



def get_adjacentes(vertice, graph):
  vertices_adjacentes = []
  for aresta in graph.edges:
      if vertice in aresta:
        if aresta[0] != vertice:
          vertices_adjacentes.append(aresta[0])
        else:
          vertices_adjacentes.append(aresta[1])
  return vertices_adjacentes

def ehRegular(graph):
    k_grau = len(get_adjacentes(list(graph.nodes)[0], graph))
    for vertice in list(graph.nodes):
      grau = len(get_adjacentes(vertice, graph))
      if k_grau != grau:
        return False
    return True

def ehCompleto(graph):
    for vertice in list(graph.nodes):
      adj = get_adjacentes(vertice, graph)
      adj.append(vertice)
      if sorted(adj) != sorted(list(graph.nodes)):
        return False
    return True

def ehConexo(graph):
  visitados = busca_em_largura(graph)
  for vertice in list(graph.nodes):
    if vertice not in visitados:
      return False
  return True

def busca_em_largura(graph):
    vertice = list(graph.nodes)[0]
    vertices_visitados = [vertice]
    fila = [vertice]
    while len(fila) > 0:
      vertice = fila[0]
      fila.pop(0)
      adjacentes = get_adjacentes(vertice, graph)
      for adjacente in adjacentes:
        if adjacente not in vertices_visitados:
          vertices_visitados.append(adjacente)
          fila.append(adjacente)
    return vertices_visitados


plt.figure(2)
nx.draw_networkx(G, pos=nx.spring_layout(G), with_labels=True)
plt.show()
print(ehCompleto(G))
print(ehRegular(G))
print(ehConexo(G))

plt.figure(2)
nx.draw_networkx(E, pos=nx.spring_layout(E), with_labels=True)
plt.show()
print(ehCompleto(E))
print(ehRegular(E))
print(ehConexo(E))