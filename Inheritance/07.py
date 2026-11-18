'''7. Shopping Cart System

Base:

Product

Derived:

Electronics
Grocery
Clothing

Apply discounts.'''

from abc import ABC, abstractmethod

class Product(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_cat(self):
        pass

    @abstractmethod
    def get_discount(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def __str__(Self):
        pass

class Electronics(Product):

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_cat(self):
        return "Electronics"

    def get_discount(price):
        return price * 0.85

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"{self.__name} --> Electronics --> {self.__price} --> Category Discount: {Electronics.get_discount(self.__price)}"

class Grocery(Product):

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_cat(self):
        return "Grocery"

    def get_discount(price):
        return price * 0.90

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"{self.__name} --> Grocery --> {self.__price} --> Category Discount: {Grocery.get_discount(self.__price)}"

class Clothing(Product):

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_cat(self):
        return "Clothing"

    def get_discount(price):
        return price * 0.80

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"{self.__name} --> Clothing --> {self.__price} --> Category Discount: {Clothing.get_discount(self.__price)}"


e = Electronics("Laptop", 90000)
print(e)
g = Grocery("Pulses", 120)
print(g)
c = Clothing("Shirt", 1500)
print(c)