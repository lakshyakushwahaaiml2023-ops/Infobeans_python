'''5. Banking System

Parent:

BankAccount

Child:

SavingsAccount
CurrentAccount

Implement withdrawal rules.'''

from abc import ABC, abstractmethod

class BankAccount(ABC):

    @abstractmethod
    def withdraw(self):
        pass

class SavingsAccount(BankAccount):

    def withdraw(self, amnt):
        print(f"{amnt} Withdrawed from Savings account...")

class CurrentAccount(BankAccount):

    def withdraw(self, amnt):
        print(f"{amnt} Withdrawed from Current account...")


s = SavingsAccount()
s.withdraw(10000)
