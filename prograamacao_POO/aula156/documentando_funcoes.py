"""
Este é um módulo de exemplo

Este módulo contém funções e exemplos de documentação de funções
A função soma vocẽ já conhece bastante.
"""

variavel_1 = 1

def soma(x: int | float, y: int | float) -> int | float:
    """
    Soma x e y

    :param x: Número 1
    :type x: int or float
    :param y: Número 2
    :type y: int or float

    :return: A soma entre x e y
    :rtype: int or float
    """
    return x + y

def multiplicar(
        x: int | float,
        y: int | float,
        z: int | float | None = None
) -> int | float:
    
    """Multiplica x, y e/ou z

    Multiplica x e y.  Se z for envido multiplica x, y e z."""

    if z is not None:
        return x * y * z
    return x * y