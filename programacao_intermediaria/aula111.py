from functools import partial
from types import GeneratorType

def print_iter(iterator):
    print(*iterator, sep='\n')
    print()

def aumenta_preco(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_dez_porcento = partial(
    aumenta_preco, porcentagem=1.1
)
        

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# novos_produtos = [
#     {**produto,
#         'preco': aumenta_preco(produto['preco'], 1.1)}
#     for produto in produtos
# ]
# novos_produtos = [
#     {**produto,
#         'preco': aumentar_dez_porcento(produto['preco'])}
#     for produto in produtos
# ]

def muda_preco_de_produto(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(
            produto['preco']
            )
    }

novos_produtos = map(
    muda_preco_de_produto, produtos
)

# novos_produtos = (x for x in produtos)

print_iter(produtos)
print_iter(novos_produtos)


print(novos_produtos)
print(isinstance(novos_produtos, GeneratorType))
print(hasattr(novos_produtos, '__iter__'))
print(hasattr(novos_produtos, '__next__'))