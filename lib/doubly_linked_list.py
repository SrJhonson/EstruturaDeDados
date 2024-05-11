class DoublyLinkedList:
    """
    ESTRUTURA DE DADOS LISTA DUPLAMENTE ENCADEADA
    Trata-se de uma lista linear, em que seus elementos
    (chamados nodos ou nós) não estão fisicamente adjacentes
    uns dos outros, mas ligados de forma lógica por ponteiros
    que indicam o nodo anterior e o nodo seguinte da
    sequência. Não possui restrições de acesso - inserções,
    exclusões e consultas podem ser executadas em qualquer
    posição da lista
    """
    #---------------------------------------------------------
    class Node:
        """
        Classe interna que representa a unidade de informação
        (nodo) armazenado pela lista duplamente encadeada
        """
        def __init__(self, data):
            """ Construtor da classe interna """
            self.prev = None  # Ponteiro para o nodo anterior
            self.data = data  # Dado útil para usuário
            self.next = None  # Ponteiro para o nodo seguinte
    #---------------------------------------------------------

    def __init__(self):
        """
        Construtor da classe principal DoublyLinkedList
        """
        self.__head = None  # Ponteiro para o primeiro nodo
        self.__tail = None  # Ponteiro para o último nodo
        self.__count = 0    # Quantidade de nodos na lista

    def __find_node(self, pos):
        """
        Método PRIVADO que encontra um nodo na posição
        especificada
        """
        # 1º caso: posição 0, retorna self.__head
        if pos == 0: return self.__head

        # 2º caso: posição final (self.__count - 1),
        # retorna self.__tail
        if pos == self.__count - 1: return self.__tail

        # 3º caso: posição intermediária

        # Se a posição estiver na primeira metade da lista,
        # faz o percurso a partir de self.__head, seguindo
        # o ponteiro next
        if pos < self.__count // 2:
            # Percorre a lista quantas vezes forem necessárias
            # até encontrar o nodo da posição desejada
            node = self.__head
            for _ in range(1, pos + 1): node = node.next
            return node
        
        # Senão, a posição estando na segunda metade da lista,
        # faz o percurso reverso a partir de self.__tail,
        # seguindo o ponteiro prev
        else:
            node = self.__tail
            for _ in range(self.__count - 2, pos - 1, -1):
                node = node.prev
            return node

    def insert(self, pos, val):
        """
            Método que insere na posição 'pos' o valor 'val'
        """

        # Se a posição passada for negativa, exibimos um erro
        # e terminamos o programa
        if(pos < 0):
            raise Exception("ERRO: posição para inserção não pode ser negativa.")

        # Criamos um novo nodo para armazenar "val" e também
        # os ponteiros "prev" e "next", ambos apontando
        # inicialmente para None
        new = self.Node(val)

        # 1º caso: a lista está vazia, e "new" será, ao mesmo
        # tempo, tanto o primeiro quanto o último nodo
        if self.__count == 0:
            self.__head = new
            self.__tail = new

        # 2º caso: inserção no início da lista (posição 0)
        elif pos == 0:
            new.next = self.__head
            self.__head.prev = new
            self.__head = new

        # 3º caso: inserção no final da lista
        # OBS.: consideramos como posição final da lista
        # qualquer uma que seja >= self.__count
        elif pos >= self.__count:
            new.prev = self.__tail
            self.__tail.next = new
            self.__tail = new

        # 4º caso: inserção em posição intermediária
        # Não temos acesso direto às posições intermediárias.
        # Para encontrá-la, precisaremos partir de uma das
        # extremidades (__head ou __tail) e percorrer a lista
        # até encontrar o nodo que, atualmente, ocupa a
        # posição onde o novo será inserido. Essa busca será
        # feita por um outro método, chamado __find_node()
        else:
            # Busca o nodo que atualmente ocupa a posição de 
            # inserção
            current = self.__find_node(pos)

            # Determina o nodo anterior à posição
            before = current.prev

            # Efetua o encaixe do novo nodo na sequência
            before.next = new
            new.prev = before
            new.next = current
            current.prev = new

        # Incrementa a quantidade de elementos da lista
        # após uma inserção em qualquer caso
        self.__count += 1

    def append(self, val):
        """
        Método de atalho para inserir no final da lista
        """
        self.insert(self.__count, val)

    def get_count(self):
        """
        Método que retorna a quantidade de elementos da lista
        """
        return self.__count
    
    def peek(self, pos = None):
        """
        Método que retorna o valor, dada a posição
        Se a posição for omitida, retorna o valor do último elemento
        """
        if pos is None: pos = self.__count - 1

        if pos < 0 or pos >= self.__count:
            raise Exception("ERRO: posição inexistente na lista.")
        
        node = self.__find_node(pos)
        return node.data
    
    def remove(self, pos):
        """
        Método que remove um nodo da lista, dada sua posição
        """
        # 1º caso: lista vazia ou posição fora dos limites
        if self.__count == 0 or pos < 0 or pos >= self.__count:
            raise Exception("ERRO: posição inválida para remoção.")
        
        # 2º caso: remoção do início da lista
        if pos == 0:
            # Vamos remover o nodo apontado por __head
            being_removed = self.__head
            # O novo __head passa a ser o sucessor do nodo removido
            self.__head = being_removed.next
            # Se o novo __head for um nodo válido, ele não pode ter um antecessor
            if self.__head is not None: self.__head.prev = None
            # SITUAÇÃO ESPECIAL: em caso de remoção do único nodo restante da
            # lista, __tail também precisa passar a valer None
            if self.__count == 1: self.__tail = None

        # 3º caso: remoção do final da lista
        elif pos == self.__count - 1:
            # Vamos remover o nodo apontado por __tail
            being_removed = self.__tail
            # O novo __tail passa a ser o antecessor do nodo removido
            self.__tail = being_removed.prev
            # Se o novo __tail for um nodo válido, ele não pode ter um sucessor
            if self.__tail is not None: self.__tail.next = None
            # SITUAÇÃO ESPECIAL: em caso de remoção do único nodo restante da
            # lista, __head também precisa passar a valer None
            if self.__count == 1: self.__head = None

        # 4º caso: remoção de posição intermediária
        else:
            # Pedimos a __find_node() para localizar o nodo a ser removido
            being_removed = self.__find_node(pos)
            before = being_removed.prev # Nodo anterior ao que está sendo removido
            after = being_removed.next  # Nodo seguinte ao que está sendo removido
            # O nodo anterior passa a apontar, à frente, para o nodo posterior
            before.next = after
            # O nodo seguinte passa a apontar, para trás, para o nodo anterior
            after.prev = before

        self.__count -= 1

        return being_removed.data

    def pop(self):
        """
        Método de atalho para remover o último nodo da lista
        """
        return self.remove(self.__count - 1)

    def __str__(self):
        """
        Método que gera uma representação em string da lista duplamente encadeada
        """
        if self.__count == 0: return "[*** LISTA VAZIA ***]\n\n"

        repr = f"*** LISTANDO {self.__count} ITEM(NS) ***\n"
        repr += f"Endereço do __head: {hex(id(self.__head))}\n"
        repr += f"Endereço do __tail: {hex(id(self.__tail))}\n"
        repr += ("=" * 80) + "\n"

        node = self.__head
        for pos in range(self.__count):
            repr += f"NODO posição {pos}, endereço: {hex(id(node))}\n"
            repr += f"   Endereço do nodo anterior: {hex(id(node.prev))}\n"
            repr += f"   DADO DO USUÁRIO: {node.data}\n"
            repr += f"   Endereço do nodo seguinte: {hex(id(node.next))}\n"
            repr += ("-" * 80) + "\n"
            node = node.next

        repr += ("=" * 80) + "\n\n"
        return repr