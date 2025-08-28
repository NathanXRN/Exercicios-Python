# Escreva um programa em Python que aceite o nome e o sobrenome do usuário e os imprima em ordem inversa, com um espaço entre eles

nome      = input("Digite o nome completo: ")

partes_nome = nome.split()

nome_reverso = partes_nome[::-1]

nome_invertido = " ".join(nome_reverso)

print(nome_invertido)





