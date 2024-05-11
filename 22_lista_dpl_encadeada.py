from lib.doubly_linked_list import DoublyLinkedList

lista = DoublyLinkedList()
print(lista)

# Inserção do primeiro elemento
lista.insert(0, "Fusca")
print(lista)

# Inserção de um novo elemento no final da lista
lista.insert(1, "Chevette")
print(lista)

# Inserção de um elemento no início da lista
lista.insert(0, "Opala")
print(lista)

# Inserindo um novo elemento entre Opala e Fusca
lista.insert(1, "Maverick")
print(lista)

# Tentativa de inserção em uma posição negativa
# lista.insert(-3, "Corcel")
# print(lista)

# Podemos inserir no final da lista de duas formas diferentes
lista.insert(lista.get_count(), "Fiat 147")
lista.append("Kombi")
print(lista)

# Consultando o valor de algumas posições
primeiro = lista.peek(0)
pos4 = lista.peek(4)
pos5 = lista.peek(5)
ultimo = lista.peek()   # Para consultar o último, não passamos a posição
print(f"PRIMEIRO: {primeiro}, POS. 4: {pos4}, POS. 5: {pos5}, ÚLTIMO: {ultimo}")

# Tentativa de consultar um valor em uma posição inexistente
# pos7 = lista.peek(7)

# Mais dois carros para aumentar a lista
lista.insert(3, "Corcel")
lista.append("Brasília")
print(lista)

# Removendo o primeiro elemento da lista
removido = lista.remove(0)
print(lista)
print("Removido da primeira posição:", removido)

# Removendo o último elemento da lista
removido = lista.pop()
print(lista)
print("Removido da última posição:", removido)

# Removendo o nodo da posição 3
removido = lista.remove(3)
print(lista)
print("Removido da posição 3:", removido)

# Removendo o nodo da posição 1
removido = lista.remove(1)
print(lista)
print("Removido da posição 1:", removido)