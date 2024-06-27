
'''
Cuidadocom dados mutaveis

= copia valor (imutáveis)
= aponta para o mesmo valor na memoria
'''

lista_a = ['Osvaldo', 'Alves']
lista_b = lista_a # lista_b aponta para o endereço de memória da lista_a
lista_c = lista_a.copy() # lista_c copia os valores da lista_a

lista_a[0] = 'Outra coisa'

print(lista_a)
print(lista_b)
print(lista_c)

