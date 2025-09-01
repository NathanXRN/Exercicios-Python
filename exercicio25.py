# Escreva um programa em Python para obter a soma de um inteiro não negativo usando recursão.

def digitos_soma(num):

    if len(num) == 1:
        return num[0]
    else:
        return num[0] + digitos_soma(num[1:])
    
print(digitos_soma(345))