# Herança

# Associação - um objeto usa outro objeto
# Agregação - um objeto tem outro objeto
# Composição - um objeto é dono de outro objeto

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    ...


class Aluno(Pessoa):
    ...


c1 = Cliente('Osvaldo', 'Alves')
a1 = Aluno('Maria', 'Helena')

c1.falar_nome_classe()
a1.falar_nome_classe()

help(Cliente)