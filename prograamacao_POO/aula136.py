# Composição


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero)) # crio a instacia endereco 
        # dentro da classe Clinte, quando a instancia cliente deixar de existir a 
        # instancia endereço também sera excluida da memória

    def listar_enderecos(self):
        print()
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('Apagando: ', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('Apagando: ', self.rua, self.numero)

cliente = Cliente('Osvaldo')
cliente.inserir_endereco('Av Brasil, ', 120)
cliente.inserir_endereco('Av Vendrame, ', 21)
cliente.listar_enderecos()

# del cliente

print('############## Aqui termina o código')