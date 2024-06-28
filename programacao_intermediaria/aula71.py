

'''
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
'''
x, y, *resto = 1, 2, 3 , 4 # desempacotamento
# print(x, y, resto)

# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0
    for numero in args:
        total += numero

    return total

numeros = 1,2,3,4,5,6

resultado = soma(*numeros)
print(resultado)

print(sum(numeros))