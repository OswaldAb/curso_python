
# split e join com list e string

# split -> divide uma string ou list
# join _> une uma string ou list

frase = '  Olha só que,   coisa interessante  '

# lista_palavras = frase.split() # divide a string por espaço
lista_frases = frase.split(',') # divide a string por virgula (,)

'''
strip -> corta os espaço do inicio e fim
rstrip -> remove os espaços do fim
lstrip -> remove os espaços do inicio
'''

nova_lista_frases = list()

for i, frase in enumerate(lista_frases):
    nova_lista_frases.append(lista_frases[i].strip()) 

print(lista_frases)
print(nova_lista_frases)

# frases_unidas = '-'.join('abc')
frases_unidas = ', '.join(nova_lista_frases)

print(frases_unidas)