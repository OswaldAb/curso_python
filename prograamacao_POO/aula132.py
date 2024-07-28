# Getter -> obtem valor
# Setter -> define valor


class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None

    @property # Getter
    def cor(self):
        return self._cor
    
    @cor.setter # Seter
    def cor(self, cor):
        self._cor = cor

    @property # Getter
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter # Setter
    def cor_tampa(self, cor):
        self._cor_tampa = cor

# caneta = Caneta('Blue')
# caneta.cor = 'Pink'

caneta = Caneta('Azul')
caneta.cor_tampa = 'Red'

print(caneta.cor_tampa)





