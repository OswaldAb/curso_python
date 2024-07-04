# Módulos
# primeiro mudulo executado se chama: __main__
# Você pod eimportar modulo inteiro ou parte do módulo
# o python conhece a pasta onde o __main__ está e as pastas
# abaixo dele
# Ele não reconhece a pasta e modulos acima do __main__ por
#padrão
# O python conhece todos os modulos e  pacotes presentes nos caminho de 
# sys.path

import aula97_m

# print('Este módulo se chama', __name__)
print(aula97_m.variavel_modulo)

print(aula97_m.soma(1,2,3))
