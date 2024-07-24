
string = 'Osvaldo' # str

class Pessoa: # classe chamada pessoa
    def __init__(self, name, last_name):  # inicializador da classe
        self.name = name
        self.last_name = last_name

# p1 = Pessoa()
# p1.name = 'Osvaldo'
# p1.last_name = 'Alves'

p1 = Pessoa('Osvaldo', 'Alves')
p2 = Pessoa('Camila', 'Santos')



print(p1.name, p1.last_name)
print(p2.name, p2.last_name)