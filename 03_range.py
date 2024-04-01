# range() é uma função que gera uma fatia de números, é muito usado em associação com listas

# 1) range() com *UM* PARAMETRO
# gera uma faixa numerica que vai de 0 (zero) ate o valor do parametro -1:
for num in range(10):
    print(num)


# Traço separador 
print("-" * 60)

# 2) range() com *DOIS* parametros 
#   1 parametro -> Valor inicial da faixa
#   2 parametro -> Valor final da faixa (Não incluido)

for x in range(10, 16):
    print(x)

# Traço separador 
print("-" * 60)

# 3) range() com *TRES* parametros
#   1 parametro -> valor inicial da faixa
#   2 parametro -> valor final da faixa (Não incluido)
#   3 parametro -> passo(intervalo entre um numero e outro)

for n in range(1, 22, 3): # De 1 a 21 contando de 3 em 3
    print(n)
    
# Traço separador 
print("-" * 60)

# range() com passo negativo
for i in range(10,0,-1): #Contagem regressiva de 10 a 1
    print(i)