'''
42. E-Commerce Order Processing

Implement:

products
orders
payment methods
delivery system'''

class EMS:
    def __init__(self):
        self.__products = {}
        self.__orders = []

    def add_product(self, pid, pname, cat, price):
        if pid in self.__products:
            print("Product ID already in database...")
        else:
            self.__products[pid] = Product(pid, pname, cat, price)
            print("Product added...")

    def view_product(self):
        print("\n---Product List---")
        for product in self.__products.values():
            print(product)
        print("=" * 60)

    def order_item(self, pid):
        if pid not in self.__products:
            print("There is no product with given Product ID...")
        else:
            self.__orders

class Product:
    def __init__(self, pid, pname, cat, price):
        self.__pid = pid
        self.__pname = pname
        self.__cat = cat
        self.__price = price

    def __str__(self):
        return f"{self.__pid} | {self.__pname} | {self.__cat} | {self.__price} Rs"

    def get_price(self):
        return self.__price

class Order:
    pass

class Delivery:
    pass

class Payment:
    pass

e = EMS()
