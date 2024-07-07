
def somar_listas(lista_1, lista_2):
    intervalo_maximo = min(len(lista_1), len(lista_2))

    return [
        x + y
        for x,y in zip(lista_1, lista_2)
    ]

l1 = [1,2,3,4,5,6,7]
l2 = [1,2,3,4,]

print(f'{somar_listas(l1, l2)=}')