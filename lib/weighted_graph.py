from graph import Graph

class WeightedGraph(Graph):
    """
    ESTRUTURA DE DADOS GRAFO PONDERADO
    Trata-se de uma estrutura do tipo grafo, cujas arestas
    trazem, como informação extra, o peso (weight) atribuído
    a ela. Grafos ponderados podem ser utilizados, por exemplo,
    para o cálculo da menor distância entre dois pontos quando
    há mais de um caminho possível (algoritmo de Dijkstra).

    Na nossa implemetação, vamos herdar a classe Graph e 
    sobrescrever (override) apenas os métodos em que a estrutura
    diferente da aresta do grafo ponderado seja utilizada.
    """