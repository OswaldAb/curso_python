
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório'
}

dc = {
    key: value.upper()
    if isinstance(value, str) else value
    # key: value
    # if isinstance(value, (int, float)) else value.upper()
    for key, value in produto.items()
}

print(dc)