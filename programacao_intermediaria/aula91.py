# introdução a generator function em python
# generator = (n for n in range(10))

# def generator(n=0, maximum=10):
#     yield 1 # Pausa
#     print('Continuando...')
#     yield 2 # Pausa
#     print('Mais uma vez...')
#     yield 3
#     print('Vou terminar')
#     return 'Acabou' # StopIterator

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return

gen = generator(10, 13)
for n in gen:
    print(n)

