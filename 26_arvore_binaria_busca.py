from lib.binary_search_tree import BinarySearchTree

# Cria uma novo ABB
abb = BinarySearchTree()

# Insere alguns valores
abb.insert(47)
abb.insert(31)
abb.insert(20)
abb.insert(63)
abb.insert(58)
abb.insert(40)
abb.insert(60)
abb.insert(26)
abb.insert(16)
abb.insert(73)
abb.insert(40)
abb.insert(51)
abb.insert(45)
abb.insert(36)
abb.insert(59)
abb.insert(79)

def inline_print(val):
    print(str(val) + " ", end = "")

# Percorre a árvore em-ordem
print("Em-ordem:")
abb.in_order_traversal(inline_print)
print("\n")

# Percorre a árvore em pré-ordem
print("Pré-ordem:")
abb.pre_order_traversal(inline_print)
print("\n")

# Percorre a árvore em pós-ordem
print("Pós-ordem:")
abb.post_order_traversal(inline_print)
print("\n")

# Pesquisa a existência do valor 58 na árvore
print("58 existe na árvore?", abb.exists(58))

# Pesquisa a existência do valor 35 na árvore
print("35 existe na árvore?", abb.exists(35))

print("=" * 80)

# Remoção de um nodo folha (grau 0): 51
abb.remove(51)
print("51 (grau 0) removido")
print("Pré-ordem:")
abb.pre_order_traversal(inline_print)
print("\n")
print("Em-ordem:")
abb.in_order_traversal(inline_print)
print("\n")
print("-" * 80)

# Remoção de um nodo grau 1 à esquerda: 60
abb.remove(60)
print("60 (grau 1 à esquerda) removido")
print("Pré-ordem:")
abb.pre_order_traversal(inline_print)
print("\n")
print("Em-ordem:")
abb.in_order_traversal(inline_print)
print("\n")
print("-" * 80)

# Remoção de um nodo grau 1 à direita: 73
abb.remove(73)
print("73 (grau 1 à direita) removido")
print("Pré-ordem:")
abb.pre_order_traversal(inline_print)
print("\n")
print("Em-ordem:")
abb.in_order_traversal(inline_print)
print("\n")
print("-" * 80)

# Remoção de um nodo grau 2: 31
abb.remove(31)
print("31 (grau 2) removido")
print("Pré-ordem:")
abb.pre_order_traversal(inline_print)
print("\n")
print("Em-ordem:")
abb.in_order_traversal(inline_print)
print("\n")
print("-" * 80)

# Remoção da raiz (grau 2): 47
abb.remove(47)
print("Raiz 47 (grau 2) removida")
print("Pré-ordem:")
abb.pre_order_traversal(inline_print)
print("\n")
print("Em-ordem:")
abb.in_order_traversal(inline_print)
print("\n")
print("-" * 80)

