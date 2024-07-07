# Funções decoradoras e decoratores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decradores são usados para fazer o python usar as funções
# decoradora em outras funções
# Decoradores são "Syntax Sugar" (Açucar sintático)

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        print('Ok, agora vocẽ foi decorada')
        return result
    return interna

# @criar_funcao
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param dever ser uma string.')

# inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string('123')
print(invertida)