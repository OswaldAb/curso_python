
"""
Iteraveil -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me estregue o proximo valor
iter -> me entregue o seu iterador
"""

# texto = 'Luiz'.__iter__()
# texto = iter('Osvaldo') # iterador

# # print(texto)
# print(texto.__next__())
# print(next(texto))


# Simulando for

texto = 'Osvaldo' # iteravel
iterador = iter(texto) # iterador

while True:
    try:
        letra = next(iterador)
        print(letra)

    except StopIteration:
        break
