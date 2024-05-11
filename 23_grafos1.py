from lib.graph import Graph

america_sul = Graph()   # Não direcionado

# Adicionando vértices
america_sul.add_vertex("Brasil")
america_sul.add_vertex("Argentina")
print(america_sul)

# Estabelecendo uma aresta entre dois vértices já existentes
america_sul.add_edge("Brasil", "Argentina")
print(america_sul)

# Adicionando arestas com criação automática dos vértices
america_sul.add_edge("França", "Suriname")
america_sul.add_edge("Suriname", "Guiana")
print(america_sul)

america_sul.add_edge("Brasil", "Uruguai")
america_sul.add_edge("Argentina", "Uruguai")
print(america_sul)

grafo2 = Graph(True)    # Grafo direcionado

grafo2.add_edge("Fausto", "Fatec Franca", "leciona em")
print(grafo2)