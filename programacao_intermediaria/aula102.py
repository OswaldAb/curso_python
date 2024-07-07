# def fora(x):
#     a = x

#     def dentro():
#         return a # free var (variavel livre)
#     return dentro

# dentro = fora(10)

# print(dentro())

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar('a')

print(c('b'))
print(c('c'))
print(c('d'))