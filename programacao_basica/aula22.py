
# Operador lógico or (ou)

entrar = input('[E]ntrar [S]air: ')
senha_ditada = input('Senha: ')

senha_permitida = '123456'

if  (entrar == 'E' or entrar == 'e') and senha_ditada == senha_permitida:
    print('Entrar')

else:
    print('Sair')

# senha = input('Senha: ') or 'Sem senha'
# print(senha)