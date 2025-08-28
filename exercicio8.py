# Escreva um programa em Python que aceite um inteiro (n) e calcule o valor de n+nn+nnn

n = int(input("Digite um valor (n):"))

n1 = int(f"{n}")
n2 = int(f"{n}{n}")
n3 = int(f"{n}{n}{n}")

resultado = n1 + n2 + n3

print(f"n + nn + nnn = {n1} + {n2} + {n3} = {resultado}")