
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        if self._motor is not None:
            return self._motor.nome
        return self._motor        
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def fabricante(self):
        if self._fabricante is not None:
            return self._fabricante.nome
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante
    

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

m1 = Motor('K20A')
m2 = Motor('H22A')

f1 = Fabricante('Honda')
f2 = Fabricante('Ford')

c1 = Carro('Civic')
c1.motor = m1
c1.fabricante = f1

c2 =  Carro('Fiesta')
c2.motor = m2
c2.fabricante = f2


print(
    f'Carro: {c1.nome} \n' \
    f'Motor: {c1.motor} \n' \
    f'Fabricante: {c1.fabricante} \n'
)

print(
    f'Carro: {c2.nome} \n' \
    f'Motor: {c2.motor} \n' \
    f'Fabricante: {c2.fabricante} \n'
)
