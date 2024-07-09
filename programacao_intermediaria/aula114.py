
# Funções recursivas

# def recursiva(start=0, end=10):
#     # Caso base
#     if  start >= end:
#         return start
#     # Caso recursivo
#     # contar até o final
#     start += 1
#     return recursiva(start, end)

# print(
#     recursiva()
# )

def fatorial(n):
    if n <= 1:
        return 1
    
    return n * fatorial(n - 1)
    
    

    return fatorial(n)

print(fatorial(5))

