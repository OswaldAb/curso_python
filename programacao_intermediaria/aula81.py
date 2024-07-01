
'''
funções lambda
'''
# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.

# lista = [1,3,5,2,7,6]
# lista.sort()
# print(lista)

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

'''
def ordena(item):
    return item['sobrenome'] # print(item['nome'])

lista.sort(key=ordena)
'''

def exibir(lista):
    for item in lista:
        print(item)
    print()


# lista.sort(key=lambda item: item['nome']) # função lambda

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)




