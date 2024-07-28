# Property  - getter no modo Pythônico
# Getter - metodo para obter um atributo
# Código cliente -> código que usa o seu código


# class Caneta:
#     def __init__(self, cor):
#         self.cor_tinta = cor

#     def get_cor(self): # getter
#         print('Get cor')
#         return self.cor_tinta


# caneta = Caneta('Azul')

# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())


class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 1 + 2
    
    @property
    def cor_tubo(self):
        return 'black'


caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tubo)
print(caneta.cor_tampa)

