# Escreva um programa em Python que imprima o calendário de um determinado mês e ano.

import calendar

ano = int(input("Digite o ano desejado: "))
mes = int(input("Digite o mês desejado: "))

print(calendar.month(ano, mes))