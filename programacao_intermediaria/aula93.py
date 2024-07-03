# Try, except, else e finaly

a = 18
b = 0

try:
    print(b[0])
    c = a / b
except ZeroDivisionError:
    print('Dividiu por zero')
except NameError:
    print('Variavel não esta definido')
except Exception:
    print('Erro desconhecido')

print('Continua')