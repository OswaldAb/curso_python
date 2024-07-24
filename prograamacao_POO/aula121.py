# Metodos em instancias de Classes Python

class Carro:
    def __init__(self, name):
        self.name = name  # fusca.name = 'Fuaca'

    def acelerar(self):
        print(f'{self.name} está acelerando...')


fusca = Carro('Fusca')
print(fusca.name)
fusca.acelerar()

celta = Carro(name='Celta')
print(celta.name)
celta.acelerar()