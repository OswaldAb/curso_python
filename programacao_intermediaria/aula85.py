
lista = []

for x in range(3):
    for y in range(3):
        lista.append((x, y))

lista.clear()

lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
    ]

print(lista)

# lista = [
#     [x for y in range(5)]
#     for x in range(3)
#     ]

# print(lista)