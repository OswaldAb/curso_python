
def parametros_decorador(nome):
    def decorador(func):
        print('Decorador:', nome)

        def nova_funcao(*args, **kwargs):
            result = func(*args, **kwargs)
            final = f'{result} {nome}'
            return final
        return nova_funcao
    return decorador

@parametros_decorador(nome='segundo')
@parametros_decorador(nome='primeiro')
def somar(x, y):
    return x + y

soma = somar(10, 8)
print(soma)