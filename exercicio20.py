# Escreva um programa em Python que verifique se um valor especificado está contido em um grupo de valores.

def contido(group, num):

    for valor in group:
        if num == valor:
            return True 
    return False 

print(contido([1,2,3,5,9], 3))
print(contido([1,2,3,5,9],-4))