from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, agency, account, balance=0):
        self.agency = agency
        self.account = account
        self.balance = balance
    
    @abstractmethod
    def withdrawl(self, value): # sacar, retirar
        ...

    def deposit(self, value):
        self.balance += value
        self.details(f'(Deposito {value})')

    def details(self, msg=''): 
        print(f'Seu saldo é R$ {self.balance:.2f} {msg}')
        print('---')


class SavingsAccount(Account):
    def withdrawl(self, value):
        balance_after_withdrawl = self.balance - value

        if balance_after_withdrawl >= 0:
            self.balance -= value
            self.details(f'Saque {value}')
            return self.balance
        
        print('Não foi possivel sacar o valor desejado.')
        self.details(f'(Saque negado {value})')


class CurrentAccount(Account):
    def __init__(self, agency, account, balance=0, limit=0):
        super().__init__(agency, account, balance)
        self.limit = limit

    def withdrawl(self, value):
        balance_after_withdrawl = self.balance - value
        limit_max = -self.limit

        if balance_after_withdrawl >= limit_max:
            self.balance -= value
            self.details(f'Saque {value}')
            return self.balance
        
        print('Não foi possivel sacar o valor desejado.')
        print(f'Seu limite é {-self.limit:.2f}')
        self.details(f'(Saque negado {value})')
        

if __name__ == '__main__':
 
    account = CurrentAccount(111, 22, 0, 10)
    account.withdrawl(10)
    account.withdrawl(5)

