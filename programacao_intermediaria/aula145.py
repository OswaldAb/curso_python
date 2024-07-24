# Positional-Only Parametres (/)
# Tudo antes da barra deve ser apenas posicional

# def soma(x, y, /, z=0):
#     return x + y + z

# print(soma(1, 2))
# print(soma(1, 2, z=2))


# Keyword-Only Argumentos (*)
# * soziho ! não suga ! valores

def soma(a, b, *, c):
    print(a, b, c)

soma(1, 2, c=3)