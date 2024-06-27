
# introdução ao desempacotamento + tuples (tuplas)

# nomes = ['Maria', 'Helena', 'Luiz']
# nome1, nome2, nome3 = nomes
# print(nome2)

# nomes = ['Maria', 'Helena', 'Luiz']
# nome1, *_ = nomes
# print(nome1, _)


nomes = ['Maria', 'Helena', 'Luiz']

_, _, nome, *resto = nomes

print(nome, resto)