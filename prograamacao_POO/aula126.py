# __dict__ e vars para atributos e instancias

class Pessoa:
    ano_atual = 2024

    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    def get_ano_nascimento(self):
        return 2024 - self.age
    

dados = {'name': 'Osvaldo', 'age': 22}
p1 = Pessoa(**dados)

# print(p1.__dict__)
# print(vars(p1))