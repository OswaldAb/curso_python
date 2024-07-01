# Empacootamento e desempacotamento

a, b = 1, 2
a, b = b, a
# print(a, b)

# pessoa = {
#     'nome': 'Osvaldo',
#     'sobrenome': 'Alves'
# }

# a, b  = pessoa.items()
# print(a, b)

# (a1, a2), (b1, b2)= pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for key, value in pessoa.items():
#     print(key, value)

pessoa = {
    'nome': 'Osvaldo',
    'sobrenome': 'Alves'
}

dados_pessoa = {
    'idade': 22,
    'altura': 1.7
}

pessoa_completa = {
    **pessoa,
    **dados_pessoa
}

# print(pessoa_completa)


def mostra_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS', args)

    for key, value in kwargs.items():
        print(key, value)

mostra_argumentos_nomeados(1,2,3,4, nome='Joana', qualquer=123)
print()
mostra_argumentos_nomeados(**pessoa_completa)