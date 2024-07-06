# Adiar execução de funções

def somar(x, y):
    return x + y

def multiplicar(x, y):
    return x * y

def criar_funcao(funcao, x):
        def funcao_interna(y):
            return funcao(x, y)
        return funcao_interna

soma_com_cinco = criar_funcao(somar, 5)
multiplica_por_dez = criar_funcao(multiplicar, 10)

print(soma_com_cinco(10))
print(multiplica_por_dez(10))
