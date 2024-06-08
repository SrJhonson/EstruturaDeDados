class BinarySearchTree:
    """
    ESTRUTURA DE DADOS ÁRVORE BINÁRIA DE BUSCA
    * Árvore ~> é uma estrutura de dados não-linear, considerada
      uma especialização do grafo, formada recursivamente por
      outras árvores (subárvores)
    * Árvore binária ~> uma árvore na qual cada nodo tem grau
      menor ou igual a 2. Em outras palavras, cada nodo pode ter
      até dois descendentes diretos
    * Árvore binária de busca ~> é uma árvore binária em que as
      inserções são feitas de forma ordenada, de modo a otimizar
      a operação de busca binária
    """

    class Node:
        """
        Classe interna que representa cada unidade de informação
        (nodo) da árvore binária de busca
        Possui três atributos:
        1 ~> informação relevante para o usuário (data)
        2 ~> ponteiro para o nodo descendente à esquerda (left)
        3 ~> ponteiro para o nodo descendente à direita (right)
        """
        def __init__(self, val):
            self.data = val
            self.left = None
            self.right = None

    def __init__(self):
        """ Método construtor da classe BinarySearchTree """
        self.__root = None      # Raiz da árvore

    def insert(self, val):
        """ Método PÚBLICO para a inserção de um VALOR na árvore """
        # Cria um novo nodo para armazenar o valor
        new = self.Node(val)

        # 1º caso: a árvore está vazia
        # O primeiro nodo inserido será a raiz
        if self.__root is None: self.__root = new

        # 2º caso: a raiz já existe. É necessário procurar pela
        # posição de inserção do novo nodo, o que é feito por um
        # método privado
        else: self.__insert_node(self.__root, new)

    def __insert_node(self, root, new):
        """ Método PRIVADO que insere um NODO na árvore """
        # 1º caso: o valor do novo nodo é MENOR do que o valor na raiz
        if new.data < root.data:
            # Se a esquerda da raiz estiver desocupada, insere aí
            if root.left is None: root.left = new
            # Senão, passa a considerar o nodo da esquerda como raiz
            # e chama de novo, recursivamente, a função
            else: self.__insert_node(root.left, new)

        # 2º caso: o valor do novo nodo é MAIOR do que o valor na raiz
        elif new.data > root.data:
            # Se a direita da raiz estiver desocupada, insere aí
            if root.right is None: root.right = new
            # Senão, passa a considerar o nodo da direita como raiz
            # e chama de novo, recursivamente, a função
            else: self.__insert_node(root.right, new)

    def in_order_traversal(self, action, root = False):
        """
        Método que percorre a árvore em-ordem
        1º ~> percorre recursivamente a subárvore esquerda
        2º ~> visita a raiz
        3º ~> percorre recursivamente a subárvore direita
        Os valores armazenados na árvore serão mostrados em
        ordem crescente, do menor para o maior
        """
        if root is False: root = self.__root
        if root is not None:
            self.in_order_traversal(action, root.left)
            action(root.data)
            self.in_order_traversal(action, root.right)

    def pre_order_traversal(self, action, root = False):
        """
        Método que percorre a árvore em pré-ordem
        1º ~> visita a raiz
        2º ~> percorre recursivamente a subárvore esquerda
        3º ~> percorre recursivamente a subárvore direita
        A raiz será o primeiro valor a ser exibido, seguida dos
        valores à sua esquerda e depois os valores à sua direita
        """
        if root is False: root = self.__root
        if root is not None:
            action(root.data)
            self.pre_order_traversal(action, root.left)
            self.pre_order_traversal(action, root.right)

    def post_order_traversal(self, action, root = False):
        """
        Método que percorre a árvore em pós-ordem
        1º ~> percorre recursivamente a subárvore esquerda
        2º ~> percorre recursivamente a subárvore direita
        3º ~> visita a raiz
        A raiz será o último valor a ser exibido, após os
        valores à sua esquerda e os valores à sua direita
        """
        if root is False: root = self.__root
        if root is not None:
            self.post_order_traversal(action, root.left)
            self.post_order_traversal(action, root.right)
            action(root.data)

    def exists(self, key):
        """ 
        Método PÚBLICO que verifica se um valor (key) existe na ABB
        """
        node = self.__search_node(self.__root, key)
        return (node is not None)
    
    def __search_node(self, root, key):
        """
        Método PRIVADO que procura por um nodo que contém um valor
        fornecido (key) e retorna esse nodo, se ele existir, ou None,
        caso contrário
        """
        # 1º caso: árvore vazia
        if root is None: return None

        # 2º caso: o valor de key é MENOR que o valor na raiz
        # Continua a buscar recursivamente pela subárvore ESQUERDA
        if key < root.data: return self.__search_node(root.left, key)

        # 3º caso: o valor de key é MAIOR que o valor na raiz
        # Continua a buscar recursivamente pela subárvore DIREITA
        elif key > root.data: return self.__search_node(root.right, key)

        # 4º caso: o valor de key é IGUAL ao valor na raiz
        # ENCONTROU O NODO; retorna o nodo root
        return root
    
    def __max_node(self, root = None):
        """
        Método PRIVADO que retorna o nodo de MAIOR valor de uma árvore
        """
        if root is None: root = self.__root
        node = root
        # A partir da raiz, desce pela DIREITA até onde for possível
        while node is not None and node.right is not None:
            node = node.right
        return node
    
    def remove(self, key):
        """
        Método PÚBLICO para a remoção de um nodo da árvore, dado o valor
        nele armazenado (key)
        """
        self.__root = self.__remove_node(self.__root, key)

    def __remove_node(self, root, key):
        """
        Método PRIVADO que remove um nodo da árvore
        """
        # 1º caso: árvore vazia
        if root is None: return None

        # 2º caso: o valor a ser removido é MENOR do que o valor da raiz
        # Continua procurando o nodo a ser removido pelo lado ESQUERDO
        if key < root.data:
            root.left = self.__remove_node(root.left, key)
            return root
        
        # 3º caso: o valor a ser removido é MAIOR do que o valor da raiz
        # Continua procurando o nodo a ser removido pelo lado DIREITO
        if key > root.data:
            root.right = self.__remove_node(root.right, key)
            return root
        
        # 4º caso: o valor a ser removido é IGUAL ao valor da raiz
        # O NODO A SER REMOVIDO FOI ENCONTRADO
        # Agora, é necessário determinar o grau do nodo para aplicar
        # o algoritmo de remoção correto para cada situação

        # 4.1: remoção de nodo de grau 0
        if root.left is None and root.right is None:
            # Sobrescreve o nodo (root) com None
            root = None
            return root
        
        # 4.2: remoção de nodo de grau 1 com subárvore à ESQUERDA
        if root.left is not None and root.right is None:
            root = root.left
            return root
        
        # 4.3: remoção de nodo de grau 1 com subárvore à DIREITA
        if root.left is None and root.right is not None:
            root = root.right
            return root
        
        # 4.4: remoção do nodo de grau 2
        # É necessário encontrar:
        # ~> o nodo de MAIOR valor da subárvore ESQUERDA; *OU*
        # ~> o nodo de MENOR valor da subárvore DIREITA
        # Nesta implementação, foi escolhido usar o nodo de maior valor
        # da subárvore esquerda

        new_root = self.__max_node(root.left)

        # Copia o valor do nodo encontrado e sobrescreve o valor do
        # nodo que está sendo "removido"
        root.data = new_root.data

        # Exclui o valor duplicado que está na subárvore esquerda
        # (de onde veio o valor de new_root)
        root.left = self.__remove_node(root.left, new_root.data)

        return root