'''Q5. OOP Programming Question: Product Management System
Intermediate Level
 10 Marks


Problem Statement:

Develop a Product Management System using Python OOP concepts.

Create a class named Product with the following attributes:
- product_id
- product_name
- category
- price
Requirements
1. Create a Product class with an appropriate constructor.
2. Create at least 5 product objects with different prices.
3. Store all product objects inside a list.
4. Implement a method display_product() to display product details.
5. Find and display the product having the second-highest price.
6. Display all products whose price is greater than ₹10,000.
7. Calculate and display the average price of all products.
8. Product must be unique on the basis of id'''

class Product:
    def __init__(self, pid, pname, cat, price):
        self.__pid = pid
        self.__pname = pname
        self.__cat = cat
        self.__price = price

    def __str__(self):
        return f"{self.__pid} | {self.__pname} | {self.__cat} | {self.__price}"

    def get_price(self):
        return self.__price

    def __lt__(self, other):
        return self.__price < other.__price

    def __hash__(self):
        return hash(self.__pid)

    def __eq__(self, id):
        return self.__pid == id

class PMS:
    def __init__(self):
        self.__products = []

    def add_product(self, pid, pname, cat, price):
        p = Product(pid, pname, cat, price)
        if p in self.__products:
            print("Product ID already exists!!!")

        else:
            self.__products.append(p)
            print("Product added successfully...")

    def display_product(self, pid):
        for product in self.__products:
            if product == pid:
                print(product)
                break
        else:
            print("Product not found with given Product ID...")

    def second_highest_price(self):
        self.__products.sort()
        if len(self.__products) >= 2:
            print("Second highest cost product: ", self.__products[-2])
        else:
            print("There are not enough products...")

    def view_all_products(self):
        print("Product list: ")
        for product in self.__products:
            print(product)

        print(f"Average cost: {PMS.average(self.__products)}")

    def filter(self, price):
        print("Products having price more than ", price)
        for product in self.__products:
            if product.get_price() >= 10000:
                print(product)

    @staticmethod
    def average(products):
        summ = 0
        count = 0
        for product in products:
            summ += product.get_price()
            count += 1
        return summ/ count
        

p = PMS()
p.add_product(101, "Bottle", "Utensils", 1000)
p.add_product(102, "Laptop", "Electronics", 120000)
p.add_product(103, "Leather Jacket", "Clothing", 5000)
p.add_product(104, "Gaming Phone", "Electronics", 25000)
p.add_product(105, "Water purifier", "Gadgets", 12000)
print()
p.display_product(105)
p.display_product(110)
print()
p.second_highest_price()
print()
p.view_all_products()
print()
p.filter(10000)