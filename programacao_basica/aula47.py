
palavra_secreta = 'melancia'.lower()
palavra = ''
tentativas = 0

while True:

    letra_digitada = input('Digite uma letra: ').lower()
    tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!\n')
        continue

    if bool(letra_digitada) == False:
        print('Você não digitou nada!\n')
        continue

    for letra_secreta in palavra_secreta:
        if letra_digitada == letra_secreta:
            palavra += letra_digitada
        else:
            palavra += '*'
        


    print(f'palavra: {palavra} , tentativas: {tentativas}\n')