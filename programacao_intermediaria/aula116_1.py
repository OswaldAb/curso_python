import os

file_path = '/home/osvaldo/Meu_Repositorio/curso_python/programacao_intermediaria/aula116.txt'

with open(file_path, 'w',  encoding='utf8') as file:
    file.write('Osvaldo Alves de Brito')

os.remove(file_path) # os.unlink(file_path)