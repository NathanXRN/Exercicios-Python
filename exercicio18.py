# Escreva um programa em Python para obter n cópias (inteiro não negativo) dos 2 primeiros caracteres de uma determinada string. 
# Retorne n cópias da string inteira se o comprimento for menor que 2.

def copia(text, n):

    if len(text) > 2:
        resultado = text[:2] * n 
    return f"Resultado: {resultado}"

print(copia("gelatina",4)) 