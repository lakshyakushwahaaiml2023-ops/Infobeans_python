'''13. Write a Java program to create a class called "Inventory" with a collection of products and 
methods to add and remove products, and to check for low inventory.
'''

class Inventory:
    __products = {}

    def add_product(self, id, name,price, qnty):
        if id in Inventory.__products:
            Inventory.__products[id].add_quantity(qnty)
            print("Qunatity added!!")
        else:
            p1 = Product(id, name, price, qnty)
            Inventory.__products[id] = p1
            print("Project added in inventory!!")

    def remove_product(self, id):
        if id in Inventory.__products:
            Inventory.__products.pop(id)
            print("Product removed!!")
        else:
            print("Product not found in inventory!!")

    def view_products(self):
        print("Products in Inventory:")
        for product in Inventory.__products.values():
            print(product)

class Product:
    def __init__(self, id, name, price, qnty):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__quantity = qnty

    def add_quantity(self, qnty):
        self.__quantity += qnty

    def display(self):
        print(f"Product ID : {self.__id}")

    def __str__(self):
        return f"\nID: {self.__id}\nName: {self.__name}\nPrice {self.__price} Rs"


i1 = Inventory()
i1.add_product(101, "Apple", 100, 20)
i1.add_product(102, "Grapes", 50, 12)
i1.add_product(103, "Banana", 30, 10)
i1.view_products()