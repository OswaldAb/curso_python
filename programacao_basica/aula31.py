

# v1 = 'a'
# v2 = 'b'
# print(id(v1))
# print(id(v2))

condicao  = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Falça algo')

else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no if')

# print(passou_no_if, passou_no_if is None)
# print(passou_no_if, passou_no_if is not None)