# funções decoradoras e decoradores 

def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name} ({class_dict})'
        return class_repr

def add_repr(cls):
    cls.__repr__ = my_repr
    return cls


def my_planeta(metodo):
    def interna(self, *args, **kwargs):
        result = metodo(self, *args, **kwargs)

        if 'Terra' in result:
             result = 'Você está em casa.'
        return result
    return interna

@add_repr
class Time:
     def __init__(self, nome):
         self.nome = nome
         

@add_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @my_planeta
    def falar_nome(self):
            return f'O planeta é {self.nome}'


brasil = Time('Brasil')
portugual = Time('Portugual')

terra = Planeta('Terra')
marte = Planeta('Marte')


print(brasil)
print(portugual)

print(terra)
print(marte)


print(terra.falar_nome())
print(marte.falar_nome())