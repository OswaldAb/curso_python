
# texto = 'Python'

# i = 0
# text_size = len(texto)

# while i < text_size:
#     print(texto[i])

#     i += 1

texto = 'Python'
novo_texto = ''

# Para cada letra no texto imprima letra
for letra in texto:
    print(letra)
    novo_texto += f'*{letra}'

print(novo_texto + '*')