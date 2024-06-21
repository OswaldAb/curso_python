
# Operadores in  e not in
# strings são iteráveis

"""
0 1 2 3 4 5 6
O s v a l d o
-7-6-5-4-3-2-1
"""
# nome = 'Osvaldo'

# print(nome)

# print('a' in nome) # 'a' está em nome
# print('x' in nome) # 'x' está in nome
# print('z' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('O que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}.')

else:
    print(f'{encontrar} não está em {nome}.')