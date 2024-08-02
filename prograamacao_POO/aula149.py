# Context Manager com classes

# Ex:
# with open('./149.txt', 'w', encoding=utf8) as file:
#     ...

class MyOpen:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self._file = None

    def __enter__(self):
        print('Abrindo arquivo...')
        self._file = open(self.file_path, self.mode)
        return self._file

    def __exit__(self, class_exception, exception_, traceback_):
        print('Fechando arquivo...')
        self._file.close()

        print(class_exception)
        print(exception_)
        print(traceback_)

        return True  # tratei a eceção

instancia = MyOpen('./aula149.txt', 'w')

with instancia as file:
    file.write('linha1\n')
    file.write('linha2\n', 45)
    file.write('linha3\n')
    print('WITH...', file)