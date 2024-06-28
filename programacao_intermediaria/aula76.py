
'''
dict - dicionários (mutável)
par de chave e valor

'''

# dicionario
# pessoa = dict(
#     nome='Osvaldo',
#     sobrenome='Alves de Brito'
#     )

pessoa = {
    'nome': 'Osvaldo',
    'sobrenome': 'Alves de Brito',
    'idade': 18,
    'altura': 1.8,
    'Enderecos': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 321},
    ],
}

# print(pessoa['nome'])
# print(pessoa['Enderecos'][0])

for chave in pessoa:
    print(chave, pessoa[chave])