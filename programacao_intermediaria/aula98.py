 # Recarregar modulos
import importlib

import aula98_m

for i in range(10):
    importlib.reload(aula98_m)

print(aula98_m.variavel)