'''8. Online Food Delivery

Parent:

FoodItem

Derived:

Pizza
Burger
Sandwich

Calculate total bill.'''


class FoodItem:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"{self.__name} --> {self.__price}"


class Pizza(FoodItem):
    def __init__(self, price):
        super().__init__("Pizza", price)
   

class Burger(FoodItem):
    def __init__(self, price):
        super().__init__("Burger", price)

class Sandwich(FoodItem):
    def __init__(self, price):
        super().__init__("Sandwich", price)


class Order:
    def __init__(self):
        self.__items = []

    def add_item(self):
        while True:
            print("1. Pizza: 299 Rs.")
            print("2. Burger: 59 Rs.")
            print("3. Sandwich: 100 Rs. ")
            print("4. Exit-> Confirm Order")
            choice = int(input("Enter your choice..."))

            match choice:
                case 1:
                    self.__items.append(Pizza(299))
                    print("Added")
                case 2:
                    self.__items.append(Burger(59))
                    print("Added")
                case 3:
                    self.__items.append(Sandwich(99))
                    print("Added")
                case 4:
                    bill = Order.generate_bill(self.__items)
                    print("Your total bill: ", bill)
                    break
                case _:
                    print("Enter a valid choice...")

    @staticmethod
    def generate_bill(items):
        bill = 0
        for item in items:
            print(item)
            bill += item.get_price()

        return bill


o = Order()
o.add_item()
