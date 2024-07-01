import pprint

def p(v):
    pprint.pprint( v, sort_dicts=False, width=40)

produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.5,}
    if produto['preco'] > 20 else {**produto} # mapeamento
    for produto in produtos
]

# print(novos_produtos)
# p(novos_produtos)

# lista = [
#     numero for numero in  range(10)
#     if numero < 5 # filtro
#     ]
# print(lista)

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.5,}
    if produto['preco'] > 20 else {**produto} # mapeamento
    for produto in produtos
    if produto['preco'] > 10
]

p(novos_produtos)

