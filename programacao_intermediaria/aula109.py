# Combinations, Permutations e Product - Itertools
# combinação - Ordem não importa - iteravel
# permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product

def mostrar_iter(iterator):
    print(*iterator, sep='\n')
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Leticía',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm'],
]

# mostrar_iter(combinations(pessoas, 2))
# mostrar_iter(permutations(pessoas, 2))
mostrar_iter(product(pessoas, *camisetas))