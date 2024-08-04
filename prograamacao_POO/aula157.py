# Enum -> enumeração
import enum

# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])
class Direcoes(enum.Enum):
    ESQUERDA = 1
    DIREITA = 2

print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA)
print(Direcoes(1).name, Direcoes['ESQUERDA'].value, Direcoes.ESQUERDA)

def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção Invalida!')

    
    print(f'Movendo para {direcao.name}')

mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)