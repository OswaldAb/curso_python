
class Animal:

    def __init__(self, name):
        self.name = name

    def comendo(self, alimento):
        return f'{self.name} está comendo {alimento}'
    
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)

leao = Animal(name='Leão')

print(leao.name)
print(leao.comendo('maçã'))
print(leao.executar('pão de milho'))