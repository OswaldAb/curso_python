# public é acessado dentro e fora da classe
# protected é acessado apenas dentro da classe e de suas classes filhas
# private é acessado apenas pela propia classe ? name mangling

class Foo:
    def __init__(self):
        self.public = 'Isso é publico' # publico
        self._protected = 'Isso é protegido' # protegido
        self.__private = 'Isso é privado' # privado


f = Foo()
print(f'{f._Foo__private}')
