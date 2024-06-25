
name = 'Osvaldo Alves' # Iteraveis

new_name = ''
size_name = len(name)
contador = 0

while contador < size_name:

    new_name += f'*{name[contador]}'
    contador += 1

new_name += '*'

print(new_name)

