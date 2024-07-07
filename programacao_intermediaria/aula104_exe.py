
def criar_funcao(func):
    def executa(*args, **kwargs):
        for arg in args:
            is_numeric(arg)
        return func(*args, **kwargs)
    return executa


def is_numeric(param):
    if not isinstance(param, (int, float)):
        raise TypeError('Deve ser número.')


@criar_funcao
def somar(*args):
    result = 0
    for n in args:
        result += n
    return result

# soma_e_checa_parametro = criar_funcao(somar)
result = somar(1,2,3,4,5,'7',6,7,8,)
print(result)