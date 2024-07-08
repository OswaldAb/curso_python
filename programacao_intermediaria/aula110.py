from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def ordena(item):
    return item['nota']

grupos = groupby(
    sorted(
        alunos, key=ordena
        ), 
        key=ordena
    )

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(f'{aluno['nome']},', end=' ')
    print()