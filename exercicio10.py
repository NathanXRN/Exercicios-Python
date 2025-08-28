# Escreva um programa em Python para calcular o número de dias entre duas datas.

from datetime import date

datas = (2014, 7, 2), (2014, 7, 11)

data1 = date(datas[0][0], datas[0][1], datas[0][2])
data2 = date(datas[1][0], datas[1][1], datas[1][2])

calculo_entre_datas = data2 - data1

numero_de_dias = calculo_entre_datas.days

print(f"Diferença: {numero_de_dias} dias")