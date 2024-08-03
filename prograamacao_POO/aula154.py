# Classes decoradoras (Decorator classes)

class Multiplicar:
    def __init__(self, func):
        self.func = func
        self._multiplicador = 10

    def __call__(self, *args):
        result = self.func(*args)
        return result * self._multiplicador


@Multiplicar
def soma(x, y):
    return x + y

res = soma(2, 2)
print(res)





# def dobra(funcao):
#     def interno(*args, **kwargs):
#         print('Vou te decorar.')
#         result = funcao(*args, **kwargs)
#         print('Te decorei.')
#         return result * 2
#     return interno


# @dobra
# def soma(x, y):
#     return x + y

# print(soma(2,3))