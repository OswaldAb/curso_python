import sys
# Genarator expression, Iterables e Iterators em python
# Todo Generator é um iterator mas o iterator não é um generator

iterable = ['Eu', 'Tenho', '__iter__'] 
iterator  = iterable.__iter__() # tem __iter__ e __next__

lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))
print(
    sys.getsizeof(lista),
    sys.getsizeof(generator)
    )

# print(next(generator))
# print(next(generator))
print(len(generator))

for n in generator:
    print(n)

