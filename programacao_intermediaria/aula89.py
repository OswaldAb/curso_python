
'''
hasattr -> checa se o tipo tem determinado metodo
getattr -> executa o metodo do tipo
'''
valor = 'OSVALDO'
metodo = 'lower'

if hasattr(valor, metodo): # valor tem o metodo

    print(f'Existe {metodo=}')

    print(
        valor,
        getattr(valor, metodo)())

else:
    print(f'Não existe o {metodo=}')