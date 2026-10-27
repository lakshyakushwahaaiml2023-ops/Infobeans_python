'''
6. Shopping Cart and Checkout
Intermediate
Concepts: Loops, conditions, functions, lists, dictionaries
Requirements
•	Store products and prices.
•	Allow customers to add items and quantities.
•	Calculate item-wise and total costs.
•	Apply discounts based on purchase value.
•	Generate a final bill.
Bonus: Implement removing an item and checking product availability.
'''

products = {
    "Apple": 100,
    "Banana": 40,
    "Mango": 80,
    "Orange": 60,
    "Grapes": 120,
    "Watermelon": 50,
    "Pineapple": 90,
    "Papaya": 70,
    "Strawberry": 150,
    "Kiwi": 30,
    "Milk": 60,
    "Bread": 40,
    "Butter": 55,
    "Cheese": 120,
    "Eggs": 80,
    "Rice": 70,
    "Wheat Flour": 45,
    "Sugar": 50,
    "Salt": 20,
    "Cooking Oil": 150,
    "Biscuits": 30,
    "Chips": 20,
    "Chocolate": 50,
    "Ice Cream": 100,
    "Coffee": 180,
    "Tea": 120,
    "Soap": 35,
    "Shampoo": 110,
    "Toothpaste": 60,
    "Detergent": 90
}
def check_availability(product):
    if product not in products:
        print("------Oops!!!!-----")
        print("----Out of Stock----")
        return False
    return True

def add_product(cart):
    product = input("Enter product name : ")
    if check_availability(product):
        quantity = int(input("Enter quantity: "))
        cart[product] = quantity
    
def remove_product(cart):
    product = input("Enter product name to remove: ")
    cart.pop(product)

def view_cart(cart,bill):
    for key,value in cart.items():
        print(f"{key} ==> {value}")
    print(f"Total Amount ==> {calc_total(cart,bill)}")

def calc_total(cart,bill):
    for key in cart:
        bill += products[key]*cart[key]

    return bill

def discount(bill):
    if bill > 500 and bill < 1000:
        bill = bill * 0.95
    elif bill > 1000 and bill < 2000:
        bill = bill * 0.90
    elif bill > 2000:
        bill = bill * 0.85
    else:
        bill = bill

    return bill

def shopping_cart():
    cart = {}
    bill = 0
    print("---------WelCome--------")
    while True:
        print("1. Add Product")
        print("2. Remove Product")
        print("3. View Cart")
        print("4. Calculate Total")
        print("5. Exit")
        choice = int(input("Enter your choice (1 - 4): "))
        if choice == 1:
            add_product(cart)
        elif choice == 2:
            remove_product(cart)
        elif choice == 3:
            view_cart(cart,bill)
        elif choice == 4:
            bill = calc_total(cart,bill)
            print(f"Total Amount ==> {bill}")
            bill = discount(bill)
            print(f"After Discount Amount ==> {bill}")
        elif choice == 5:
            print("---------Thank - You--------")
            print("-------Happy - Shopping-------")
            break

shopping_cart()