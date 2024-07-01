
lista_1 = [1,2,3,4,5,3,3,3,1]

set_1 = set(lista_1)

lista_2 = list(set_1)

print(lista_2)


for value in set_1:
    print(f'valor: {value}')