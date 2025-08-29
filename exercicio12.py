# Escreva um programa em Python para testar se um número está entre 100 e 1000 ou 2000.

def condition_near(num):
    
    distancia_de_1000 = abs(1000 - num)
    distancia_de_2000 = abs(2000 - num)

    near_1000 = distancia_de_1000 <= 100
    near_2000 = distancia_de_2000 <= 100

    print(f"Número: {num} ")
    print(f"Distância de 1000: {distancia_de_1000} ")
    print(f"Distância de 2000: {distancia_de_2000} ")
    print(f"Próximo de 1000: {near_1000} ")
    print(f"Próximo de 2000: {near_2000} ")
    print(f"Resultado: {near_1000 or near_2000}")

    return near_1000 or near_2000

test_numbers = [1000, 900, 800, 1100, 1150, 2000, 1900, 2100, 2200, 1500]

for num in test_numbers:
    print(condition_near(num))
