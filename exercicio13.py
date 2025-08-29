# Escreva um programa em Python para calcular a soma de três números fornecidos. Se os valores forem iguais, retorne três vezes a soma.

def calculadora_soma():

    num1 = int(input("Digite o valor: "))
    num2 = int(input("Digite o valor: "))
    num3 = int(input("Digite o valor: "))


    if num1 == num2 == num3:
        resultado = (num1 + num2 + num3) * 3
  
    else:
        resultado = num1 + num2 + num3 
        
    return resultado

resultado = calculadora_soma()
print(f"Resultado: {resultado}")