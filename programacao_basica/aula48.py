
# Listas em Python 
# Tipo list - Mutável
# Metodos úteis: append, insert, pop, del, clear, extend, +


# string = 'ABCDE'

'''

lista = [123, True, 'Osvaldo Alves', 1.2, []] # lista = list()

print(lista)
print(lista[2])

lista[2] = 'Luiz Otávio'

print(lista)
print(lista[2])

'''

'''

lista = [10, 20, 30, 40]
lista[2] = 300 # insere valor no indice
print(lista[2])

del lista[2] # deleta valor do indice
print(lista[2])

lista.append(50) # adiciona valor no final da lista
print(lista)

lista.pop() # remove o ultimo valor da lista
print(lista)

lista.pop(1)
print(lista)

'''

'''
lista = [10, 20, 30, 40]

lista.append('Osvaldo')

print(lista)
lista.pop()
# lista.clear()
print(lista)

lista.insert(0, 'valor 1')
print(lista[5])
'''

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b # extende a lista
lista_a.extend(lista_b)

print(lista_a)
