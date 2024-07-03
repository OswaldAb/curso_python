
try:
    print('Abrir arquivo')
except NameError:
    print('Tratar erro')
except ZeroDivisionError as error:
    print('Tratar erro')


try:
    print('Abrir arquivo')
finally: # depende apenas de try
    print('Fechar arquivo')


try:
    print('Tenta executar')
except:
    print( 'Tratar erro')
else:
    print('Se não houver erro')
finally: # depende apenas de try
    print('Fechar arquivo')