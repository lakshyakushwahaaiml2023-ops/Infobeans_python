'''55. Online Shopping Discount System
Problem Statement

Different customer types receive different discounts.

Create:

abstract class Customer

Child:

RegularCustomer
PremiumCustomer
VIPCustomer

Rules:

Regular → 5%
Premium → 10%
VIP → 20%'''

from abc import ABC, abstractmethod

class Customer(ABC):
    @abstractmethod
    def calc_discount():
        pass

class RegularCustomer(Customer):
    def calc_discount(self, price):
        return price * 0.95

class PremiumCustomer(Customer):
    def calc_discount(self, price):
        return price * 0.90

class VIPCustomer(Customer):
    def calc_discount(self, price):
        return price * 0.80

while True:
    print("1. Regular Customer")
    print("2. Premium Customer")
    print("3. VIP Customer")
    print("4. Exit")
    try:
        choice = int(input("Enter your choice..."))
        assert choice <= 4 and choice >= 1
    except ValueError as e:
        print("Try again... choose between 1 - 4...")

    except AssertionError as e:
        print("Try again... choose between 1 - 4...")
    else:
        if choice == 1:
            r = RegularCustomer()
            print(f"Discounted price: {r.calc_discount(10000)}")
        if choice == 2:
            r = PremiumCustomer()
            print(f"Discounted price: {r.calc_discount(10000)}")
        if choice == 3:
            r = VIPCustomer()
            print(f"Discounted price: {r.calc_discount(10000)}")

        if choice == 4:
            break