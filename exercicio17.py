# Escreva um programa em Python para contar o número 4 em uma lista fornecida.

def contador():

    lista = input("Digite números separados por vírgulas: ")
    lista = lista.split(",")
    lista = [int(x) for x in lista]

    contar = 0

    for i in lista:
        if i == 4:
            contar = contar + 1
    return f" Repetição: {contar}" 

print(contador())


