# Sistema bancario
from abc import ABC, abstractmethod

class Conta(ABC): # class abstras

    @abstractmethod
    def sacar(self): ...


class Pessoa(ABC):
    def __init__(self, nome):
        self._nome = nome
        self._idade = None

        def nome(self):
            return self._nome


class Cliente(Pessoa):
    ...

class ContaCorrente(Conta): ...

class ContaPoupanca(Conta): ...