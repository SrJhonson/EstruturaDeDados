from lib.graph import Graph

grafo2 = Graph(True)    # Grafo direcionado
grafo2.add_edge("Fausto", "Fatec Franca", "leciona em")
grafo2.add_edge("Fausto", "Prefeitura de Franca", "trabalhou em")
grafo2.add_edge("Fausto", "Uni-FACEF", "leciona em")
grafo2.add_edge("Fausto", "Valentina Eugênia", "é professor de")
grafo2.add_edge("Valentina Eugênia", "Fausto", "leciona em")
grafo2.add_edge("Valentina Eugênia", "Prefeitura de Franca", "faz estágio em")
grafo2.add_edge("Valentina Eugênia", "Fatec Franca", "estuda em")
grafo2.add_edge("Uni-FACEF", "Prefeitura de Franca", "é autarquia de")
print(grafo2)

# Removendo as arestas que tocam "Prefeitura de Franca"
# antes de remover esse vértice do grafo
grafo2.remove_edge("Uni-FACEF", "Prefeitura de Franca", "é autarquia de")
grafo2.remove_edge("Fausto", "Prefeitura de Franca", "trabalhou em")
grafo2.remove_edge("Valentina Eugênia", "Prefeitura de Franca", "faz estágio em")
print(grafo2)

# Excluindo o vértice "Prefeitura de Franca", agora que ele está isolado
grafo2.remove_vertex("Prefeitura de Franca")
print(grafo2)