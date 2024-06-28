
def mutiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero

    return total

# def par_ou_impar(numero):
    # if numero % 2 == 0:
    #     return f'{numero} é par'
    # return f'{numero} é impar'

def par_ou_impar(numero):
    return  f'{numero} é {'par' if (numero % 2) == 0 else 'impar'}.'

valores = 1,2,3,4,5

result = mutiplicacao(*valores)
print(result)

print(par_ou_impar(1001))
print(par_ou_impar(2))
print(par_ou_impar(23))

print(par_ou_impar(10))

