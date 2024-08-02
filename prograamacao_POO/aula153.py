# __call__


class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self):
        print('Chamando: ', self.phone)

    
call_1 = CallMe(18997945262)

call_1()