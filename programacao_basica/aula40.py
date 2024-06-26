
# Calculadora com while

while True:

    numero_1 = input('\nDigite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ')
    operador = input('Digite um operador (+ - * /): ') or ''

    numero_1_float = 0
    numero_2_float = 0
    converteu = None
    resultado = 0

    try: # tenta converter os numeros
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        converteu = True
        
    except:
        converteu = None

    if converteu is None:
        print('\nVocê digitou valores invalidos!')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue

    if operador not in '-+/*':
        print('\nVocê digitou operador invalido!')
        continue

    match operador:
        case '-':
            resultado = numero_1_float - numero_2_float
        case '+':
            resultado = numero_1_float + numero_2_float
        case '/':
            resultado = numero_1_float / numero_2_float
        case '*':
            resultado = numero_1_float * numero_2_float
        case _:
            print('Não deveria acontecer isso!')

    print(f'{numero_1} {operador} {numero_2} = {resultado}')

    sair = input('\nDeseja sair (s)air? ').lower().startswith('s')
    
    if sair is True:
        print('Fim do programa!')
        break