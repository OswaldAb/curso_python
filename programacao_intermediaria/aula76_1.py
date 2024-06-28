
pessoa = {} # criando dicionario vazio

chave = 'nome_completo'

pessoa[chave] = 'Osvaldo Alves' # criando uma chave no dicionario
pessoa['sobrenome'] = 'de Brito'

print(pessoa)

del pessoa['sobrenome'] # excluindo chave e valor da pessoa

pessoa['sobrenome'] = 'de Brito'

if pessoa.get('sobrenome') is None:
    print('A chave não existe')

else:
    print(pessoa['sobrenome'])
# try:
#     print(pessoa['sobrenome'])
# except KeyError:
#     print('Indice inexistente!')