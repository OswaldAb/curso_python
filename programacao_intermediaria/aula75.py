
# Exercicio
# Crie funçãoes que duplicam, triplicão e quadruplicão
# o número recebido como parametro

def criar_multiplicador(fator1):
    def multiplicar(fator2):
        return fator1 * fator2

    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)

print(f'duplica {duplicar(2)}')
print(f'triplica {triplicar(2)}')
print(f'Quadripica {quadriplicar(2)}')