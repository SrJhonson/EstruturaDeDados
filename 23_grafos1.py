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

    def __get_degree(self, vertex):
        """
        Método PRIVADO que retorna o grau (número de arestas que entram
        ou saem) de um vértice
        """
        total = 0

        # GRAU DE SAÍDA (OUT-DEGREE)
        # É determinado contando-se o número de arestas associadas à
        # entrada de dicionário correspondente ao vértice
        if vertex in self.__data: total = len(self.__data[vertex])

        # GRAU DE ENTRADA (IN-DEGREE)
        # É determinado procurando-se referências ao vértice nos conjuntos
        # de adjacência associadas a cada um dos vértices do dicionário
        for v in self.__data.keys():    # Percorre o dicionário (vértices)
            for s in self.__data[v]:    # Percorre os conjuntos (arestas0)
                if vertex == s[0]: total += 1

        # O grau final é a soma dos graus de entrada e saída
        return total

    def remove_vertex(self, vertex):
        """
        Método que exclui um vértice do grafo
        Para que essa operação seja possível, o vértice precisa ter
        grau 0 (nenhuma aresta saindo ou entrando nele)
        """
        degree = self.__get_degree(vertex)
        if degree != 0:
            raise Exception(f"ERRO: impossível remover um vértice cujo grau seja diferente de zero (grau encontrado: {degree}).")
        # Exclui o vértice quando ele possui grau 0
        if vertex in self.__data: del self.__data[vertex]

    def remove_edge(self, origin, dest, label = None):
        """
        Método que remove uma aresta do grafo, tendo sido
        fornecidos o vértice de origem, o vértice de destino
        e o rótulo (opcional)
        """
        # Montagem da aresta
        edge1 = (dest, label)   # Tupla
        # Retira edge1 do conjunto de arestas do vértice de origem
        self.__data[origin].discard(edge1)

        # Se o grafo não for direcionado, precisamos remover também a aresta
        # em sentido contrário
        if not self.__is_directed:
            edge2 = (origin, label)
            self.__data[dest].discard(edge2)

    def __str__(self):
        """ Método que cria uma representação em string do grafo """
        output = f"Direcionado? {self.__is_directed}\n"
        output += str(self.__data) + "\n"
        return output       
        
    