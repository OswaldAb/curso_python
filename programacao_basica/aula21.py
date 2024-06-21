
# Operador lógico and (e)

entrar = input('[E]ntrar [S]air: ')
senha_ditada = input('Senha: ')

senha_permitida = '123456'

if  entrar == 'E' and senha_ditada == senha_permitida:
    print('Entrar')

else:
    print('Sair')