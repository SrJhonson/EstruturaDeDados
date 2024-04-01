frutas = ["laranja", "maçã", "uva", "pera","mamão","abacate","amora"]
#para percorrer uma lista e exibir apenas seus elementos,
#usamos a estrutura for..in, como já visto no arquvio 02

for f in frutas:
    print(f)
    
print("-" *40)

# Percorrer uma lista em orderm inversa: revered()

for x in reversed(frutas):
    print(x)
    
print("-" * 40)

# No entanto, frequentemente precisamos exibir, alem do valor do elemento, tambem sua posição
# Nesse caso, devemos usar a função for..in combinado com as funções range() e len()

for pos in range(len(frutas)):
    print(pos, ":",frutas[pos])
    
print("-" * 40)
#As vezes é necessário percorrer a lista de tras para a frente, mas tendo acesso tambem á posição
# dos elementos, para isso, usamos a estrutura for..in len() e range() com tres parametros

for i in range(len(frutas) -1, -1, -1):
    print(i, ":", frutas[i])