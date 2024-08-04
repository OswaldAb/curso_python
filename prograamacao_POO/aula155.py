
# object -> MyClass -> instancia


# class Foo(object):  # Isso é uma classe -> herda de object por padrão

"""
Foo = type('Foo', (object,), {})

f = Foo()  # Isso é a instancia da classe Foo
# print(isinstance(f, Foo))
print(type(f))
print(type(Foo))
"""

def my_repr(self):
    return f'{type(self).__name__} ({self.__dict__})'


class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('METACLASS NEW')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 1234
        cls.__repr__ = my_repr
        return cls

class Pessoa(object, metaclass=Meta):
    def __new__(cls, *cargs, **kwargs):
        print('MEU NEW')
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self, nome):
        print('MEU INIT')
        self.nome = nome

p1 = Pessoa('Osvaldo')
print(p1.attr)
print(p1)











