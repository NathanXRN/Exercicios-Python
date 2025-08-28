# Escreva um programa em Python que aceite uma sequência de números separados por vírgulas do usuário 
# e gere uma lista e uma tupla desses números.

numeros = input("Digite números separados por vírgulas: ")

lista = numeros.split(",")

tupla = tuple(lista)

print(lista)
print(tupla)