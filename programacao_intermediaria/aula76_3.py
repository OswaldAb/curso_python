import copy
'''
Metodos uteis
len - quantidade de chaves
keys - iterável com as chaves
values - iteravel com os valores
items - iteravel com chaves e valores
setdefault - adiciona valor se a chave nção existir
copy - retorna uma copia rasa (shallow copy)
get - obtem uma chave
pop - apaga um item com a chave especifica (del)
popitem - apaga o ultimo item adicionado
update - atualiza um dicionario com o outro
'''

pessoa = {
    'nome': 'Osvaldo',
    'sobrenome': 'Alves de Brito',
    'idade': 22 ,
    'endereco': [0,1,2],
}

# pessoa2 = pessoa.copy() # copia rasa
pessoa2 = copy.deepcopy(pessoa)
pessoa2['nome'] = 'Rogerio'

pessoa2['endereco'][2] = 333

print(pessoa)
print(pessoa2)






