# Escreva um programa em Python para testar se uma letra passada é uma vogal ou não

def is_vogal(char):

    vogal = 'aeiou'

    return char in vogal 

print(is_vogal("c"))
print(is_vogal("a"))