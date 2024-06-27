
# argumentos nomeados e não nomeados

def soma(x, y, z): # (parametros)
    print(f'{x=} {y=} {z=} | x + y + z = {x + y + z}')

soma(1, 2, 3) # argumento posicional 
soma(y=2, z=3, x=1) # argumento nomeado