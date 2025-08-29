# Escreva um programa em Python que retorne uma string com n (inteiro não negativo) cópias de uma determinada string.

def retornar(text, n):

    resultado = ""

    for i in range(n):
        resultado = resultado + text 

    return resultado

print(retornar('abc', 2))
print(retornar('rondo', 3))