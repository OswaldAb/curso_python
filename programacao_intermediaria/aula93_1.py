
a = 20
b = 'b'
division = 0
# division = a / b



try:
    division = a / b
except ZeroDivisionError as error:
    print('Erro:', error)
except (TypeError, NameError) as error:
    print('Erro:', error.__class__.__name__)
    print('Descrição::', error)