# LISTAS são uma estrutura de dados nativa da linguagem ptython. Elas permitem que vários valores possam ser associados a uma unica variavel 

#lista de strings
legumes = ["batata", "cenoura", "beterraba", "mandioquinha", "batata doce"]

#lista de numeros 
nums = [3, 10, -7, 12.8, -0.5]

#lista com valores de varios tipos
mistureba = ["Joaquim", 37, 1.81, 88, True]

## OPERAÇÕES SOBRE LISTA ##

#1) PERCURSO
# Percorrer uma lista signifca visitar cada um de seus itens e fazer algo com ele. 
# No exemplo abaixo, vamos dar print() em cada um dos legumes da lista

for leg in legumes:
    print(leg)
    
    
# Traço separador
print("-" * 60)

# Percorrendo a lista de numeros e printando o valor do dobro de cada item
for n in nums:
    print(n * 2)
    
# 2) Inserção de um novo elemento no *FIM* da lista append() // SEMPRE VAI PARA O FINAL DA LISTA   
nums.append(6)
legumes.append("mandioca")

print(nums)
print(legumes)

# Traço separador 
print("-" * 60)

# 3) INSERÇÃO DE UM NOVO ELEMENTO NA POSIÇÃO ESPECIFICADA: insert()
# Parametros: 
# 1- a posição onde será feita a inserção
# 2- o novo elemento a ser inserido

#Inserindo um novo elemento na QUARTA posição
legumes.insert(3, "tomate")
print(legumes)

#Inserindo um novo elemento na PRIMEIRA posição
legumes.insert(0, "milho")
print(legumes)

# Traço separador 
print("-" * 60)

# 4) Acessando valores, informando a respectiva posição
print("Elemento na QUINTA posição", legumes[4])
print("Elemento na PRIMEIRA posição", legumes[0])
print("Elemento na ULTIMA posição", legumes[-1])
print("Elemento na PENULTIMA posição", legumes[-2])

# Traço separador 
print("-" * 60)

# 5) SUBISTITUINDO VALORES EXISTENTES 
print("ANTES", legumes)

#Subistituindo o valor da posição 3 (Quarta posição)
legumes[3] = "Vagem"
#Subistituindo o valor da posição 0 (Primeira posição)
legumes[0] = "Nabo"
#Subistituindo o valor na posição -1 (Ultima posição)
legumes[-1] = "inhame"

print("DEPOIS", legumes)

# Traço separador 
print("-" * 60)

# 6) Determinando a quantidade de elementos da lista: len()
print("Quantidade de elementos da lista de legumes:", len(legumes))
print("Quantidade de elementos da lista de numeros:", len(nums))

# Traço separador 
print("-" * 60)

# 7) Removendo o ultimo elemento de uma lista: pop() (sem parametro)
print("Antes:", legumes)
removido = legumes.pop()
print("Valor removido", removido)
print("Depois", legumes)

# Traço separador 
print("-" * 60)

# 8) Removendo um elemento por sua posilçao: pop() com parametro 
removido = legumes.pop(3) #Remove o elemento da posição 4
print("Valor removido da posição 3", removido)
print(legumes)

# Traço separador 
print("-" * 60)

# 9) Removendo um elemento pelo seu valor: remove()
legumes.remove("mandioquinha") # não retorna valor
print ("Valor removido", removido)
print (legumes)

# Traço separador 
print("-" * 60)

# 10) Juntando e (Concatenando) duas listas: extend()

mais_legumes = ["abobrinha","quiabo","jilo","cabotia","cara"]

legumes.extend(mais_legumes)
print(legumes)

# Traço separador 
print("-" * 60)

# 11) Fatiano uma lista
#   Falar significa copiar um pedaço da lista (uma subistituta)
#   Para uma nova lista

# Criar uma sublista que contém os elementos das posições 2 e 5
# (Posição 6 NÃO ENTRA)
sublista2_5 = legumes[2:6]
print("sublista de 2 a 5:", sublista2_5)
# Traço separador 
print("-" * 60)

# Cria uma sublista que contem elementos desde o inicio até a posição 6 (posição 7 NÃO entra)
sublista_inicio_6 = legumes[:7]
print("Sublista do inicio até a posição 6: ", sublista_inicio_6)
# Traço separador 
print("-" * 60)

# Cria uma sublista que contem os elementos da posição 4 até o final
sublista_4_fim = legumes[4:]
print("Sublista da posição 4 até o final:", sublista_4_fim)
# Traço separador 
print("-" * 60)