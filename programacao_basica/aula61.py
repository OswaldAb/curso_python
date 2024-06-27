
while True:
    cpf_digitado = input('Digite o seu CPF: ') \
    .replace('.', '').replace('-', '')

    tamanho_cpf = len(cpf_digitado)
    cpf_apenas_numero = cpf_digitado.isdigit()
    cpf_valido = ''
    soma_digito_1 = 0
    soma_digito_2 = 0
    digito_1 = 0
    digito_2 = 0

    digitos_repetidos = cpf_digitado[0] * tamanho_cpf

    if digitos_repetidos == cpf_digitado:
        print('CPF invalido!')

    elif bool(cpf_digitado) == False:
        print('Você não digitou nada!')

    elif tamanho_cpf != 11:
        print('CPF invalido!')

    elif cpf_apenas_numero == False:
        print('Digite apenas numeros!')

    else:    
        cpf_valido = cpf_digitado[:9]

        j = 0 # contador
        for i in range(10, 1, -1):
            soma_digito_1 += i * int(cpf_valido[j])
            j += 1

        resultado = (soma_digito_1 * 10) % 11
        digito_1 = 0 if resultado > 9 else resultado
        cpf_valido += str(digito_1)

        j=0
        for i in range(11, 1, -1):
            soma_digito_2 += i * int(cpf_valido[j])
            j += 1

        resultado = (soma_digito_2 * 10) % 11
        digito_2 = 0 if resultado > 9 else resultado

        cpf_valido += str(digito_2)

        if cpf_valido == cpf_digitado:
            print('CPF é valido!')
        else:
            print('CPF é invalido!')



