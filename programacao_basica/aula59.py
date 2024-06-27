string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

# primeiro, b,  *_, penultimo, ultimo = lista
# print(primeiro, penultimo, ultimo)

# Desenpacitamento em chamada de funções

for nome in lista:
    print(nome, end= ' ')

print(f'\n{'-' * 10}') # imprime linha tracejada

print(*lista) # desempacotando na chada da função
print(*string)
print(*tupla)

print(*lista, sep='\n') # desempacotando na chada da função
