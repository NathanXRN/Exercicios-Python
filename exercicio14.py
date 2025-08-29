# Escreva um programa em Python para obter uma string recém-gerada a partir de uma string fornecida onde "Is" foi adicionado à frente.
#  Retorne a string inalterada se a string fornecida já começar com "Is".

def new_string(text):
    if len(text) >= 2 and text[:2] == "Is":
        return text 
    else:
        return "Is" + text 
    
print(new_string("Array"))
print(new_string("IsEmpty"))