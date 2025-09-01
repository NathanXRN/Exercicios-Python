# Escreva um programa em Python para calcular o valor de 'a' elevado a 'b' usando recursão.

def expo_num(num1, num2):

    if num2 == 0:
        return 1
    
    elif num1 == 0:
        return 0
    
    elif num2 == 1:
        return num1
    
    else:
        return num1 * expo_num(num1, num2 - 1)
    
print(expo_num(3,4))