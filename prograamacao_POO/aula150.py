from contextlib import contextmanager

@contextmanager
def my_open(file_path, mode):
    try:
        print('Abrindo arquivo...')
        file = open(file_path, mode, encoding='utf8')
        yield file
    except Exception as e:
        print('Ocorreu um erro.')
    finally:
        print('Fechando arquivo')
        file.close()

with my_open('./aula150.txt', 'w') as file:
    file.write('linha 1\n')
    file.write('linha 2\n', 2)
    file.write('linha 3\n')