
'''
Higher order function -> funções que podem receber e/ou retornar funções
first-class function -> funções que são tratadas como outros tipos de dados comum
funções de alta ordem
'''


def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args): # recebe a função e *args
    return funcao(*args) # retorna a função executada


v = executa(saudacao, 'Bom dia!', 'Osvaldo')
print(v)