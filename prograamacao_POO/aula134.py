
# Associação

# Neste código a classe escritor tem umseter que pode ser associado a uma outra classe

class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None  # protected

    @property  # Getter
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter  # Setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo.'


escritor = Escritor('Osvaldo')
caneta = FerramentaDeEscrever('Caneta')
maquina_de_escrever = FerramentaDeEscrever('Maquina de escrever')

escritor.ferramenta = caneta
escritor.ferramenta = maquina_de_escrever # escritor troca para maquina de escrever

print(caneta.escrever())
print(maquina_de_escrever.escrever())

print(escritor.ferramenta.escrever())