
# Exercicio 1

'''
numero = input('Digite um número inteiro: ')

numero_int = 0
converteu = None
par_ou_impar = 'impar'

try:
    numero_int = int(numero)
    converteu = True
except:
    converteu = None

if converteu is None:
    print('Você não digitou um número inteiro.')
    
else:

    if (numero_int % 2) == 0:
        par_ou_impar = 'par'
        
    print(f'O número é {par_ou_impar}')
'''

# Exercicio 2

'''
hora = input('Digite a hora: ')

hora_int = 0
converteu = None

try:
    hora_int = int(hora)
    converteu = True
except:
    converteu = None

if converteu is None:
    print('Você não digitou um número')

else:

    dia = 0 <= hora_int <= 11
    tarde  = 12 <= hora_int <= 17
    noite  = 18 <= hora_int <= 23

    if dia:
        print('Boa dia!')

    elif tarde:
        print('Boa tarde!')

    elif noite:
        print('Boa noite!')

    else:
        print('Hora invalida.')
'''


# Exercicio 3

'''
first_name = input('Informe o seu primeiro nome: ')

size_name = len(first_name)

if size_name <= 4:
    print('Seu nome é curto.')

elif 4 < size_name <= 6:
    print('Seu  nome é normal.')

else:
    print('Seu nome é grande')
'''




