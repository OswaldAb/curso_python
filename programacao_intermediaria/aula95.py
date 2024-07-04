
def nao_aceito_zero(n):
    if n == 0:
        raise ZeroDivisionError('Não é possivel dividor por zero!')
    return True

def deve_ser_numerico(n):
    if not isinstance(n, (int, float)):
        raise TypeError('Você deve digitar numero int ou float!')

def divide(a, b):
    deve_ser_numerico(a)
    nao_aceito_zero(a)
    nao_aceito_zero(b)
    return a / b

print(divide(20, 0))
