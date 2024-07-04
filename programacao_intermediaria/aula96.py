# Modúlosadrão do python (import, from, as e *)

# import sys # importa o modulo inteiro

# # sys.exit()
# print(sys.platform)

# ----------------------------------------

# from sys import exit, platform

# print(123)
# # exit()
# print(platform)

# ----------------------------------------

# import sys as s

# print(s.platform)
# s.exit()

# --------------------------------------

# from sys import platform as pf, exit as ex

# print(pf)
# ex()
# print(123)

# ------ Má platica de programação ------
from sys import *

print(platform)
exit()