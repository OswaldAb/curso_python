import os
palavra_secreta = 'melancia'

letras_acertadas = ''
numero_de_tentativas = 0

while True:
    palavra_formada = ''
    numero_de_tentativas += 1

    letra_digitada = input('Digite uma letra: ')

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!\n')
        continue

    if bool(letra_digitada) == False:
        print('Você não digitou nada!\n')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(f'palavra: {palavra_formada} , tentativas: {numero_de_tentativas}\n')


    if palavra_formada == palavra_secreta:
        os.system('clear') # limpa o terminal
        print('Parabens, você ganhou!'
            f'A palavra era {palavra_secreta}\n'
            f'Total de tentativas: {numero_de_tentativas}\n\n')
        
        letras_acertadas = ''
        numero_de_tentativas = 0


