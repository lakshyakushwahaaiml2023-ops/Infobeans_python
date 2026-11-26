'''23. Banking Withdrawal System
Problem Statement

Withdrawal rules vary by account type.

Create:

abstract class Account

Child:

SavingsAccount
CurrentAccount'''

from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(Account):

    def __init__(self, balance):
        self.__balance = balance

    def withdraw(self, amount):
        if amount > 10000:
            return "Withdrawal limit exceeded for Savings Account"
        if amount > self.__balance:
            return "Insufficient balance in Savings Account"
        else:
            return f"Withdrew {amount} from Savings Account"

class CurrentAccount(Account):

    def __init__(self, balance):
        self.__balance = balance

    def withdraw(self, amount):
        if amount > 50000:
            return "Withdrawal limit exceeded for Current Account"
        if amount > self.__balance:
            return "Insufficient balance in Current Account"
        else:
            return f"Withdrew {amount} from Current Account"

acc = [SavingsAccount(120000), CurrentAccount(500000)]

for i in acc:
    print(i.withdraw(100000))