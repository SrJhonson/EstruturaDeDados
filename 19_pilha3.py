"""
Programa simples que verifica o balanceamento de parênteses em
expressões matemáticas usando pilha
"""
from lib.stack import Stack

pilha = Stack()

expr = "(2 * ((3 + 4) - (5 / 3) (+ 1) - 2"


for pos in range(len(expr)):
    # 1ª PARTE: percorrer a expressão e EMPILHAR as posições
    #           onde são encontrados caracteres de abre parêntese       
    if expr[pos] == "(": pilha.push(pos)

    # 2ª PARTE: ao encontrar um caractere de fecha parêntese,
    #           desempilha
    elif expr[pos] == ")":
        #A pilha não pode estar vazia quando for encontrado um fecha parentese
        if pilha.is_empty():
            print(f"Erro: parentese fechado na posição {pos} não tem o abre correspondente")
        else:
            pos_emp = pilha.pop()
            print(f"Parêntese aberto na posição {pos_emp} foi fechado na posição {pos}.")

print(pilha)

# Processa eventuais sobras na pilha após o termino da análise da expressão
while not pilha.is_empty():
    pos = pilha.pop()
    print(f"Erro: parentese aberto na posição {pos} não tem o fecha correspondente")