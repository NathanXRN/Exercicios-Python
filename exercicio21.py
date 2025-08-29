# Escreva um programa em Python para imprimir todos os números pares de uma determinada
#  lista de números na mesma ordem e parar de imprimir qualquer número após 237 na sequência.

numeros = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958.743
    ]

lista_imprimir = []

for num in numeros:
    if num == 237:
        print(num)
        break
    elif num % 2 == 0:
        lista_imprimir.append(num)
print(lista_imprimir)