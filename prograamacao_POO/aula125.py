# atributos de Classe

class Pessoa:
    ano_atual = 2024

    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    def get_ano_nascimento(self):
        return 2024 - self.age
    

p1 = Pessoa('Osvaldo', 22)
p2= Pessoa('Miguel', 10)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())