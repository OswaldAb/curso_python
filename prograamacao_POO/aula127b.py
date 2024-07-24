import json
from aula127 import Pessoa, fazer_dump

# fazer_dump()

dados_pessoa = None

with open('./aula127.json', 'r') as file:
    dados_pessoa = json.load(file)


p1 = Pessoa(**dados_pessoa[0])
p2 = Pessoa(**dados_pessoa[1])
p3 = Pessoa(**dados_pessoa[2])

print(
    f'Nome: {p1.name} \nidade: {p1.age} \npeso: {p1.weight}'
    )
print(
    f'Nome: {p2.name} \nidade: {p2.age} \npeso: {p2.weight}'
    )
print(
    f'Nome: {p3.name} \nidade: {p3.age} \npeso: {p3.weight}'
    )

print(__name__)