
# exibir os indices da lista

lista = ['Maria', 'Helena', 'Luiz']
# i = 0
# for nome in lista:
#     print(f'{i} {nome}')
#     i += 1

indices = range(len(lista))

for indice in indices:
    print(f'{indice} {lista[indice]}')