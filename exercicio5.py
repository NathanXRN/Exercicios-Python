# Escreva um programa em Python que aceite um nome de arquivo do usuário e imprima a extensão do arquivo.

nome_do_arquivo = 'exemplo.csv'

nome_do_arquivo = nome_do_arquivo.split(".")

extensao_do_arquivo = nome_do_arquivo[1]

print(extensao_do_arquivo)