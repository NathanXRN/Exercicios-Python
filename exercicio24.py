# Escreva um programa em Python para resolver a sequência de Fibonacci usando recursão.

def recursive_fibonacci(num):

    if num == 1 or num == 2:
        return 1
    else:
        return recursive_fibonacci(num - 1) + recursive_fibonacci(num - 2)

print(recursive_fibonacci(7))