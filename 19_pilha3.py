"""
Programa simples que verifica o balanceamento de parênteses em
expressões matemáticas usando pilha
"""
from lib.stack import Stack

pilha = Stack()

expr = "(2 * (3 + 4) - (5 / 3) + 1) - 2"


for pos in range(len(expr)):
    # 1ª PARTE: percorrer a expressão e EMPILHAR as posições
    #           onde são encontrados caracteres de abre parêntese       
    if expr[pos] == "(": pilha.push(pos)

    # 2ª PARTE: ao encontrar um caractere de fecha parêntese,
    #           desempilha
    elif expr[pos] == ")":
        pos_emp = pilha.pop()
        print(f"Parêntese aberto na posição {pos_emp} foi fechado na posição {pos}.")

print(pilha)