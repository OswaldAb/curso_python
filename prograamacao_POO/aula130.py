# method vs @classmethod vs @staticmethod

# method - self, metodo de instancia
# @classmethod - cls, metodo de classe
# @staticmethod - metodo estático (xself, xcls)


class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user
    
    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    

    @staticmethod
    def soma(x, y):
        return x + y
   

    
# c1 = Connection()
# c1.set_user('Osvaldo')
# c1.set_password('123')
# print(c1.user)
# print(c1.password)

c2 = Connection.create_with_auth('Osvaldo', 'senha')
print(c2.user, c2.password)
print(Connection.soma(2, 3))