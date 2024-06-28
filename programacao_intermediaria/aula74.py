
'''
Closure e funções que retorna outras funções
'''

def criar_saudacao(saudacao):

    def saudar(nome): 
        return f'{saudacao}, {nome}!'
    
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

# print(falar_bom_dia('Osvaldo'))
# print(falar_boa_noite('Luiz'))

for nome in ['Osvaldo', 'Rogério', 'Ezequiel', 'Ana']:
    print(falar_bom_dia(nome))