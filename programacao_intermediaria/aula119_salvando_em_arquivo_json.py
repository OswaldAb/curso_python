import json
import os

pessoas = [
    {
        "nome": "Osvaldo",
        "sobrenome": "Alves",
        "idade": 22,
        "peso": 1.73
    }
]

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'arquivo-python.json')


with open(SAVE_TO, 'w') as file:
    json.dump(pessoas, file, indent=2)