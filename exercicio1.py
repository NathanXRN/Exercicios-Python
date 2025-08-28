# Escreva um programa em Python para exibir a data e a hora atuais.

import datetime 

now = datetime.datetime.now()

print("Current date and time: ")

print(now.strftime("%Y-%m-%d %H:%M:%S"))