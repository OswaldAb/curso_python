
lista = ['Maria', 'Helena', 'Luiz']

lista.append('João')

# lista_enumerada = enumerate(lista)
# for item in lista_enumerada:
#     print(item)

# for item in enumerate(lista):
#     print(item)

# for item in enumerate(lista):
#     indice, nome = item
#     print(f'{indice} {nome}')

for indice, nome in enumerate(lista):
    print(indice, nome)