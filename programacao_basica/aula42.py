
frase = 'O Python é uma linguagem de programação '\
    'multipadigma. '\
    'Python foi criado por Guido Van Russen.'.lower()


i = 0 # contador do while
letra_predominante = '' # salva a letra que mais aparece
conta_letra_predominante = 0 # salva a qtd de vezes que a letra predominante apareceu

while i < len(frase):
    
    letra_atual = frase[i]
    

    if letra_atual ==  ' ':
        i += 1
        continue

    # letra atual apareceu mais vezes que a letra predominante
    if frase.count(letra_atual) > conta_letra_predominante:
        letra_predominante = letra_atual
        conta_letra_predominante = frase.count(letra_predominante)
    
    i += 1

  


print('A letra que apareceu mais vezes foi '
      f'"{letra_predominante}" que apareceu '
      f'{conta_letra_predominante}x')