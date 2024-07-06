import copy
from dados import produtos


def exibir(lista_de_produto):
    for produto in lista_de_produto:
        print(produto)
    print()


def aumetar_preco_produtos(lista_de_produtos, porcentagem=1.1):
    lista_novos_produtos = [
        {**produto, 'preco': round(produto['preco'] * porcentagem, 2)}
        for produto in lista_de_produtos
    ]
    return lista_novos_produtos


def ordenar_produtos_por_nome(lista_de_produtos):
    lista_ordenada_por_nome = sorted(
        lista_de_produtos, key=lambda item: item['nome'], reverse=True
        )
    return lista_ordenada_por_nome


def ordenar_produtos_por_preco(lista_de_produtos):
    lista_ordenada_por_preco = sorted(
        lista_de_produtos, key=lambda item: item['preco']
    )
    return lista_ordenada_por_preco
    


novos_produtos = copy.deepcopy(produtos)
novos_produtos = aumetar_preco_produtos(novos_produtos)

produtos_ordenado_por_nome = copy.deepcopy(produtos)
produtos_ordenado_por_nome = ordenar_produtos_por_nome(produtos_ordenado_por_nome)

produtos_ordenado_por_preco = copy.deepcopy(produtos)
produtos_ordenado_por_preco = ordenar_produtos_por_preco(produtos_ordenado_por_preco)

exibir(produtos)
exibir(novos_produtos)
exibir(produtos_ordenado_por_nome)
exibir(produtos_ordenado_por_preco)
