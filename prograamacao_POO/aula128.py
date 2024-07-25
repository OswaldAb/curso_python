# Metodos de classes + factories (fábricas)

class Pessoa:
    ano = 2024 # Atributo da classe

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')


    @classmethod
    def criar_com_50_anos(cls, name):
        return cls(name, 50)
    

    @classmethod
    def criar_sem_nome(cls, age):
        return cls('Anonimo(a)', age)


p1 = Pessoa('Osvaldo', 22)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa.criar_sem_nome(20)
print(p3.name, p3.age)
print(p2.name, p2.age)
# print(Pessoa.ano)
# Pessoa.metodo_de_classe()


