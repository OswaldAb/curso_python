import random
import sys

# Gerando CPF

cpf = str(random.randint(100000000, 999999999))

cpf_valido = cpf[:9]

soma_digito_1 = 0
soma_digito_2 = 0

j = 0 # contador
for i in range(10, 1, -1):
    soma_digito_1 += i * int(cpf_valido[j])
    j += 1

resultado = (soma_digito_1 * 10) % 11
digito_1 = 0 if resultado > 9 else resultado
cpf_valido += str(digito_1)

j=0
for i in range(11, 1, -1):
    soma_digito_2 += i * int(cpf_valido[j])
    j += 1

resultado = (soma_digito_2 * 10) % 11
digito_2 = 0 if resultado > 9 else resultado

cpf_valido += str(digito_2)

print(f'CPF gerado: {cpf_valido}')



