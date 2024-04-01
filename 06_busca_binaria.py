comps = 0     #contador de comparações

def busca_binaria(lista, val):
    """
    ALGORITIMO DE BUSCA BINARIA
    Dados uma lista, que deve estar PREVIAMENTE ORDENADA, e um valor de busca, divide a lista em duas partes, procurando pelo valor de busca
    apenas na metade onde o valor de busca poderia estar. Novas subdivisões são feitas até que se encontre o valor de busca ou que reste apenas 
    uma sublista vazia, quando então se conclui que o valor de busca não existe na lista
    """
    #Declaramos que queremos usar a variavel global comps
    #inicializamos na linha 1
    global comps
    comps = 0
    
    ini = 0                     #Posição inicial da lista 
    fim = len(lista) -1         #Posição final da lista
    
    
    while ini <= fim:
        #Calculando o meio da lista
        meio = (ini + fim) // 2   #divisão inteira
        #Verifica se o valor que está no meio da lista
        #É igual ao valor de busca, em caso afirmativo,
        #Retornamos a posição do meio, pois o valor de busca foi encontrado
        if val == lista [meio]:
            comps += 1
            return meio
        #Senão, se o valor de busca é menor do que o valor do meio
        #Reinicia a busca na metade esquerda da (sub)lista
        elif val < lista[meio]:
            comps += 2
            fim = meio -1
            
        #Por fim, se o valor de busca é MAIOR do que o valor do meio, 
        # reinicia a busca na metade direita
        # da (sub) lista
        else:
            comps +=2
            ini = meio +1
    
    #CUIDADO COM A IDENTAÇÃO AQUI
    #Se chegamos a este ponto, é pq o valor não existe na lista
    return -1

import sys
sys.dont_write_bytecode = True
#Testes com nomes
from time import time

from data.nomes_completos import nomes

hora_ini = time()
resultados1 = busca_binaria(nomes, "EDSON PEREIRA")
hora_fim = time()
print(f"EDSON PEREIRA encontrado na posição {resultados1}")
print(f"Comparações: {comps}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")

hora_ini = time()
resultados2 = busca_binaria(nomes, "MARIA FERREIRA")
hora_fim = time()
print(f"MARIA FERRERIA encontrado na posição {resultados2}")
print(f"Comparações: {comps}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")


hora_ini = time()
resultados3 = busca_binaria(nomes, "VALDIR SILVA")
hora_fim = time()
print(f"VALDIR SILVA encotrado na posição {resultados3}")
print(f"Comparações: {comps}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")


hora_ini = time()
resultados4 = busca_binaria(nomes, "GILCINEIA GARCIA")
hora_fim = time()
print(f"GILCINEIA GARCIA encontrado na posição {resultados4}")
print(f"Comparações: {comps}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")
