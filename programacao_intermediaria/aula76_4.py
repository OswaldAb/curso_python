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

pessoa1 = {
    'nome': 'Osvaldo',
    'sobrenome': 'Alves de Brito',
}

# print(pessoa1['nome'])
# print(pessoa1.get('nome'))

# nome = pessoa1.pop('nome')
# print(pessoa1)
# print(nome)

# print(pessoa1)
# ultimo_item = pessoa1.popitem()
# print(ultimo_item)

print(pessoa1)

pessoa1.update({
    'nome': 'novo valor',
    'idade': 22
})

pessoa1.update(cidade='Piacatu', estado='São Paulo')

tupla = ('Rua', 'Jardim'),
pessoa1.update(tupla)

print(pessoa1)
