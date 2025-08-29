# Escreva um programa em Python para calcular a diferença entre um número dado e 17.
#  Se o número for maior que 17, retorne o dobro da diferença absoluta.

def diferenca(num):
    if num > 17:
        return (num - 17) * 2
    else:
        return 17 - num
    
print(diferenca(22))
print(diferenca(14))