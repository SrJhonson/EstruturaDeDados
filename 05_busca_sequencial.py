def busca_sequencial(lista, val):
    """
    Função que realiza uma busca sequencial em uma lista procurando por val.
    se val for encontrado, retorna a posição de val na lista. 
    Caso contrário, retorna o valor convencional -1.
    """
    #Percorre a lista do inicio ao fim usando range() e len()
    #(é necessário ter acesso ás posições dos elementos)
    for pos in range(len(lista)):
        #Encontrou val; retorna a posição onde foi encontrado
        if val == lista[pos]: return pos
    #<---   CUIDADO COM A IDENTAÇÃO AQUI!!
    # Percorre toda a lista e não encontrou val: retorna -1
    return -1
###############################################################################

#lista de numeros para testar
nums = [9,21,33,12,0,18,-3,30,-15,6,3,27]

#testes

pos30 = busca_sequencial(nums, 30)
print(f"Elemento 30 encontrado na posicao {pos30}")

pos_menos15 = busca_sequencial(nums, -15)
print(f"Elemento -15 encontrado na posicao {pos_menos15}")

pos19 = busca_sequencial(nums, 19)
print(f"Elemento 19 encontrado na posicao {pos19}")

print("-" * 40)

###################################################################################

import sys
sys.dont_write_bytecode = True
#Testes com nomes
from time import time

from data.nomes_completos import nomes

hora_ini = time()
resultados1 = busca_sequencial(nomes, "EDSON PEREIRA")
hora_fim = time()
print(f"EDSON PEREIRA encontrado na posição {resultados1}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")

hora_ini = time()
resultados2 = busca_sequencial(nomes, "MARIA FERREIRA")
hora_fim = time()
print(f"MARIA FERRERIA encontrado na posição {resultados2}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")

hora_ini = time()
resultados3 = busca_sequencial(nomes, "VALDIR SILVA")
hora_fim = time()
print(f"VALDIR SILVA encotrado na posição {resultados3}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")

hora_ini = time()
resultados4 = busca_sequencial(nomes, "GILCINEIA GARCIA")
hora_fim = time()
print(f"GILCINEIA GARCIA encontrado na posição {resultados4}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")