# Escreva um programa em Python para obter a soma de um inteiro não negativo usando recursão.

def sumDigits(num):

    if num == 0:
        return 0 
    else:
        return num % 10 + sumDigits(int(num / 10))

print(sumDigits(345))
print(sumDigits(45))