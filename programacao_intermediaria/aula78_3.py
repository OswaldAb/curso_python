
'''
Operadores com set()

set1 | set2 -> une (union)
set1 & set2 -> intersecção (itens presentes em ambos) (intersection)
set1 - set2 -> diferença
set1 ^ set2 -> itens que não estão em ambos (simetrica)
'''

s1 = {1, 2, 3}
s2 = {2, 3, 4}

# União
# s3 = s1.union(s2)
# s3 = s1 | s2

# Intersecção
# s3 = s1.intersection(s2)
# s3 = s1 & s2

# Diferença retona o item que esta presente apenas no set da esquerda 'A ordem importa'
# s3 = s1.difference(s2)
# s3 = s1 - s2
# s3 = s2 - s1

# Simetrica
# s3 = s1.symmetric_difference(s2)
s3 = s1 ^ s2


print(s3)