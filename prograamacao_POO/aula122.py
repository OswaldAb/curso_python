
class Carro:

    def __init__(self, name):
        self.name = name

    def acelerar(self):
        print(f'{self.name} está acelerando...')




c1 = Carro('Fusca')
c1.acelerar()

c2 = Carro('Celta')
c2.acelerar()

Carro.acelerar(Carro('Prisma'))