# Classes decoradoras (Decorator classes)

def dobra(funcao):
    def interno(*args, **kwargs):
        print('Vou te decorar.')
        result = funcao(*args, **kwargs)
        print('Te decorei.')
        return result * 2
    return interno


@dobra
def soma(x, y):
    return x + y



res = soma(2,3)
print(res)