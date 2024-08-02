
class MyError(Exception):
    ... 

class OtherError(Exception):
    ... 

def levantar():
    exception_ = MyError('a', 'b', 'c')
    raise exception_

try:
    levantar()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error)
    print()
    exception_ = OtherError('Vou lançar denovo.')
    raise exception_ from error