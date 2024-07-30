# Herança multipla

# mixins = Uma classe que não faz parte da familia

class A:
    ...
    def quem_sou(self):
        print('A')


class B(A):
    ...
    # def quem_sou(self):
        # print('B')


class C(A):
    ...
    # def quem_sou(self):
    #     print('C')


class D(B, C):
    ...
    # def quem_sou(self):
    #     print('D')

d = D()
d.quem_sou()

print(D.mro())

