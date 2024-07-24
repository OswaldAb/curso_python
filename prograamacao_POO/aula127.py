import json

class Pessoa:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight


p1 = Pessoa('Osvaldo', 22, 75.04)
p2 = Pessoa('Grabriela', 18, 60.74)
p3 = Pessoa('Milena', 25, 69.04)

dados_pessoa = [vars(p1), p2.__dict__, vars(p3)]

print(__name__)

def fazer_dump():
    with open('./aula127.json', 'w') as file:
        json.dump(dados_pessoa, file, indent=2)

if __name__ == '__main__':
    fazer_dump()