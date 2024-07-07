from itertools import zip_longest
# def zipper(lista_1, lista_2):
#     size_max = min(len(lista_1), len(lista_2))

#     return [
#         (lista_1[i], lista_2[i])
#         for i in range(size_max)
#     ]

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

# print(zipper(cidades, estados))
print(*zip(cidades, estados))
print(*zip_longest(cidades, estados, fillvalue='Sem cidade'))