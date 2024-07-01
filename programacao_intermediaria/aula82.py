
def executa(funcao, *args):
    return funcao(*args)


# def soma(x, y):
#     return x + y

print(executa(lambda  x, y: x + y, 2, 3))
# print(executa(soma, 2, 3))



# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica

# duplica = cria_multiplicador(2)

duplica = executa(
    lambda x: lambda y: x * y, 2
)

print(duplica(9))

print(
    executa(
        lambda *args: sum(args),
        1,2,3,3,3,3,3,10
    )
)