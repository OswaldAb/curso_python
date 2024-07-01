
'''
List comprehension em Python,
é uma forma rapida para criar listas
a partir de interaveis
'''

# print(list(range(10)))

# lista = list()
# for numero in range(10):
#     lista.append(numero)
# print(lista)

# lista = list(numero for numero in range(10))
lista = [
    numero * 2
    for numero in range(10)
]
print(lista)