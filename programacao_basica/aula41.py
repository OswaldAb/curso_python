
'''
O else do while só funciona se o break não for acionado'''
string = 'Osvaldo Alves'
contador = 0
while contador < len(string):
    
    print(string[contador])
    
    if ' ' == string[contador]:
        break
    
    contador += 1

else:
    print('A string não contem espaço!')