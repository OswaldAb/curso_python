# __new__ e __init__

class A:
    def __new__(cls):
        print('Antes de criar a instancia')
        instancia = super().__new__(cls)
        print('Depois')
        instancia.x = 123
        return instancia

    def __init__(self):
        print('Sou o __init__.')

    def __repr__(self):
        return f'A()'


a = A()
print(a.x)