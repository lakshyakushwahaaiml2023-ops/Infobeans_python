'''
7. Write a Java program to create a class called "Bank" with a collection of accounts and methods to add 
and remove accounts, and to deposit and withdraw money. Also define a class called "Account" to maintain account 
details of a particular customer.
'''

class Account:
    def __init__(self):
        self.__acno = ""
        self.__name = ""
        self.__money = 0

    def set_details(self, acno, name):
        self.__acno = acno
        self.__name = name

    def withdrawAmnt(self, amnt):
        if amnt > self.__money:
            print("Insufficient Balance")
        else:
            self.__money -= amnt
            print(f"Amount of {amnt} Rs withdrawn")

    def depositAmnt(self, amnt):
        self.__money += amnt
        print(f"Amount of {amnt} Rs deposited")

    def balance_enquiry(self):
        print(f"Account Number: {self.__acno}")
        print(f"Account Holder: {self.__name}")
        print(f"Current Balance: {self.__money}")
        print("="*40)


class Bank:
    def __init__(self):
        self.__accounts = {}

    def add_account(self, acno, name):
        if acno in self.__accounts:
            print("Account number already exists in the records")
        else:
            a1 = Account()
            a1.set_details(acno, name)
            self.__accounts[acno] = a1
            print("Account added to the Bank")

    def remove_account(self, acno):
        if acno not in self.__accounts:
            print(f"there is no account associated with Account Number : {acno}")
        else:
            print("Account removed from the bank")
            self.__accounts.pop(acno)

    def withdraw(self, acno, amnt):
        if acno not in self.__accounts:
            print(f"there is no account associated with Account Number : {acno}")
        else:
            self.__accounts[acno].withdrawAmnt(amnt)

    def deposit(self, acno, amnt):
        if acno not in self.__accounts:
            print(f"there is no account associated with Account Number : {acno}")
        else:
            self.__accounts[acno].depositAmnt(amnt)

    def view_account(self, acno):
        if acno not in self.__accounts:
            print(f"there is no account associated with Account Number : {acno}")
        else:
            print(self.__accounts[acno].balance_enquiry())
        print(self.__accounts)

b1 = Bank()
b1.add_account(1001, "Lakshya")
b1.deposit(1001, 12000)
b1.withdraw(1001, 123)
b1.view_account("Lakshya")           