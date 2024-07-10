# Manipulação de arquivos em python

# file_path = '/home/osvaldo/Meu_Repositorio/curso_python/programacao_intermediaria/aula116.txt'
# caminho_arquivo = '/aula116.txt'

# file = open(file_path, 'w')

# file.close()

# with open(file_path, 'w') as file:
#    file.write('Linha 1\n')
#    file.write('Linha 2\n')
#    file.writelines(
#       ('Linha 3\n', 'Linha 4\n')
#    )

# with open(file_path, 'r') as file:
# #    print(file.read())
#     # print(file.readline())
#     # print(file.readline(), end='')
#     # print(file.readline().strip())
#     # print(file.readline())
#     for line in file.readlines():
#         print(line.strip())

file_path = '/home/osvaldo/Meu_Repositorio/curso_python/programacao_intermediaria/aula116.txt'

# file = open(file_path, 'w')
# file.write('__Osvaldo__')

# file.close()

with open(file_path, 'a', encoding='utf8') as file:
    file.write('Atenção')