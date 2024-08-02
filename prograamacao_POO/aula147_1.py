
class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        # class_name = self.__class_.__name__
        class_name = type(self).__name__
        return f'{class_name} (x={self.x!r} y={self.y!r} z={self.z!r})'
        
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Ponto(new_x, new_y)
    
    def __gt__(self, other):
        result_self = self.x + self.y
        result_other = other.x + other.y
        return result_self > result_other




if __name__ == '__main__':
    p1 = Ponto(1, 2)
    p2 = Ponto(3, 2)
    # p3 = p1 + p2 # __add__
    p3 = p1 > p2  # __gt__ 

    print(p3)