
# Calculadora com while

while True:

    numero_1 = input('\nDigite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ')

    numero_1_int = 0
    numero_2_float = 0

    converteu = None

    try:
        numero_1_int = int(numero_1)
        numero_2_float = int(numero_2)
        converteu = True
        
    except:
        converteu = None


    if converteu is None:
        print('Você digitou valores invalidos!')

    else:
        resultado = numero_1_int * numero_2_float
        print(f'{numero_1_int} * {numero_2_float} = {resultado}')

    continuar = input('Deseja continuar (s)im / (n)ão: ').lower().startswith('s')
    
    if continuar is False:
        break