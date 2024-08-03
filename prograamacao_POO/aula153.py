# __call__


class CallMe:
    def __init__(self, phone):
        self.phone  = phone

    def __call__(self, *args, **kwargs):
        print('Chamando: ', self.phone)



call_1 = CallMe('9948596231')

print(call_1)
print('_' * 50 + '\n')
call_1()