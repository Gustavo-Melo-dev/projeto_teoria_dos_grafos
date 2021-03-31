import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

vertex = ['V1','V2','V3','V4','V5','V6']

for vertex in G.graph:
  G.add_node(vertex)

G.add_edge('v1', 'v2')
G.add_edge('v2', 'v3')
G.add_edge('v3', 'v4')
G.add_edge('v4', 'v5')
G.add_edge('v5', 'v1')
G.add_edge('v2', 'v4')


def ehRegular(graph):
    len_adj_vertices = []
    for vertice in G.graph:
        len_adj_vertices.append(len(vertice.arestas))
    if len(set(len_adj_vertices)) > 1:
        return False
    return


def ehCompleto(graph):
    tamanho_grafo = len(G.graph)
    print(tamanho_grafo)
    for vertice in G.graph:
        if len(vertice.arestas) != tamanho_grafo:
            return False
    return True


def ehConexo(graph):
    busca_em_largura(graph)
    for vertice in G.graph:
        if vertice.visitado == False:
            print(f'{vertice} Visitado: {vertice.visitado}')
            return False
    return True


def busca_em_largura(graph):
    fila = []
    vertice.visitado = True
    fila.append(vertice)
    # print(fila)

    while len(fila):
        u = fila[0]
        # print(fila)

        fila.pop(0)
        # print(fila)

        for w in u.arestas:
            if w.visitado == False:
                w.visitado = True
                fila.append(w)
        print(fila)


plt.figure(2)
nx.draw_networkx(G, pos=nx.spring_layout(G), with_labels=True)
plt.show()
print(ehRegular(G))
print(ehCompleto(G))
print(ehConexo(G))