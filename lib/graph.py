class Graph:
    """
    ESTRUTURA DE DADOS GRAFO
    Trata-se de uma estrutura de dados não linear, formada por
    vértices (ou nodos, ou nós) e arestas (ou arcos). Sua principal
    finalidade é representar as relações entre diferentes entidades.
    Tais relações podem ser bidirecionais, resultando em grafos não
    direcionados, ou unidirecionais, constituindo grafos direcionados
    (digrafos). Entre suas aplicações, estão representações de redes
    de computadores, mapas, caminhos e redes sociais.
    """
    def __init__(self, is_directed = False):
        """ Método construtor """
        self.__is_directed = is_directed    # O grafo é direcionado?
        # __data armazenará o grafo no formato de lista de adjacência
        self.__data = {}    # Dicionário vazio

    def add_vertex(self, val):
        """
        Método que adiciona um novo vértice ao grafo
        """
        # Verifica se o vértice já existe no dicionário.
        # A criação só será efetivada se o vértice ainda não existir
        if not val in self.__data:
            self.__data[val] = set()    # Conjunto vazio

    def add_edge(self, origin, dest, label = None):
        """"
        Método que adiciona uma aresta ao grafo. Precisa das 
        seguintes informações:
        origin ~> vértice de origem da aresta
        dest ~> vértice de destino da aresta
        label (opcional) ~> rótulo descritivo para a aresta
        """
        # Cria os vértices de origem e destino, caso ainda não existam
        if not origin in self.__data: self.add_vertex(origin)
        if not dest in self.__data: self.add_vertex(dest)

        # Monta a aresta origin -> dest
        edge1 = (dest, label)       # Isto é uma tupla
        # Adiciona a aresta origin -> dest
        self.__data[origin].add(edge1)

        # Se o grafo não for direcionado, devemos adicionar também
        # um vértice no sentido oposto, isto é, dest -> origin
        if not self.__is_directed:
            edge2 = (origin, label)
            self.__data[dest].add(edge2)

    def __str__(self):
        """ Método que cria uma representação em string do grafo """
        output = f"Direcionado? {self.__is_directed}\n"
        output += str(self.__data) + "\n"
        return output       
        