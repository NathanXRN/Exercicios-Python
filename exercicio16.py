# Escreva um programa em Python que determine se um número fornecido (aceito pelo usuário) é par ou ímpar
#  e imprima uma mensagem apropriada para o usuário.

def verificador():

    num = int(input("Digite um número: "))

    if num % 2 == 0:
        mensagem = f"Esse número {num} é par"
    else:
        mensagem = f"Esse número é ímpar"
    
    return mensagem


print(verificador())