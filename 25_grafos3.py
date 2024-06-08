from lib.weighted_graph import WeightedGraph

# Cria um grafo ponderado não direcionado
gpond = WeightedGraph()

gpond.add_edge("A", "B", 10)
gpond.add_edge("A", "D", 20)
gpond.add_edge("B", "C", 3)
gpond.add_edge("B", "F", 5)
gpond.add_edge("C", "D", 3)
gpond.add_edge("C", "E", 12)
gpond.add_edge("D", "E", 4)
gpond.add_edge("D", "G", 8)
gpond.add_edge("E", "F", 6)
gpond.add_edge("E", "G", 1)

print(gpond)

# Exibir a menor distância de A até os demais vértices
print(gpond.shortest_distance("A"))
print('-' * 60)
print(gpond.shortest_distance("C"))