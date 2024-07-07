# Funções decoradoras e decorators
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decradores são usados para fazer o python usar as funções
# decoradora em outras funções

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        print('Ok, agora vocẽ foi decorada')
        return result
    return interna


def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param dever ser uma string.')

inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)