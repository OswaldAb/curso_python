
cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']


def zipper(*args):
    x, y, *_ = args    
    lista = []

    size = len(x) if (len(x) < len(y)) else len(y)
    for i in range(size):
        lista.append((x[i], y[i]))

    return lista

print(zipper(cidades, estados))