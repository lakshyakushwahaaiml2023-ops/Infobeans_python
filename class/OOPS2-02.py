'''2. Bank Account Simulation
Problem

Design a banking system using OOP.

Requirements

Each account should contain:

account number
holder name
balance
Functionalities
Deposit money
Withdraw money
Prevent withdrawal if balance insufficient
Display account summary
Maintain bank-wide interest rate as class variable
Add static method to validate minimum balance rule
Concepts Practiced
object state management
static methods
class variables
validations'''

class Account:

  __min_bal = 2000
  
  def __init__(self, acno, name, bal):
    self.__acno = acno
    self.__name = name
    self.__bal = bal

  def deposit(self, amnt):
    self.__bal += amnt
    print("Amount Deposited Succesfully!!")
    Account.check_min(self.__bal)

  @staticmethod
  def check_min(bal):
    if bal < Account.__min_bal:
      print("Available amount is less than Minimum Monthly Active Balance!!!")
      print("Add money to avoid MAB charges!!")
  
  def withdraw(self, amnt):
    if amnt > self.__bal:
      print("Insufficient Balance!!")
      Account.check_min(self.__bal)
      return 
    self.__bal -= amnt
    print("Amount Withdrawn Succesfully!!")
    Account.check_min(self.__bal)

  def intrest(self, rate):
    self.__bal += self.__bal * rate / 100

  def __str__(self):
    return f"Account Number: {self.__acno} | Holder Name: {self.__name} | Balance: {self.__bal} Rs"

  def __hash__(self):
    return hash(self.__acno)

  def __eq__(self, other):
    return self.__acno == other.acno

    
  

class Bank:
  __intrest_rate = 10
  __accounts = {}

  def add_acc(self, acno, name, bal):
    if acno in Bank.__accounts:
      print("Account already exists with given Account number!!")
    else:
      Bank.__accounts[acno] = Account(acno, name, bal)
      print("Account added succesfully!!")

  def view_account(self, acno):
    if acno in Bank.__accounts:
      print(Bank.__accounts[acno])
    else:
      print("There is no account associated with this Account Number!!")

  def add_intrest(self, acno):
    if acno in Bank.__accounts:
      Bank.__accounts[acno].intrest(Bank.__intrest_rate)
    else:
      print("There is no account associated with this Account Number!!")

  def deposit_money(self, acno, amnt):
    if acno in Bank.__accounts:
      Bank.__accounts[acno].deposit(amnt)
    else:
      print("There is no account associated with this Account Number!!")

  def withdraw_money(self, acno, amnt):
    if acno in Bank.__accounts:
      Bank.__accounts[acno].withdraw(amnt)
    else:
      print("There is no account associated with this Account Number!!")

b1 = Bank()
b1.add_acc(101, "Lakshya", 120000)
b1.view_account(101)
b1.deposit_money(101, 12000)
b1.view_account(101)
b1.withdraw_money(101, 1200)
b1.view_account(101)
b1.add_intrest(101)
b1.view_account(101)
b1.withdraw_money(101, 143000)
b1.view_account(101)
