'''
4. Restaurant Billing System
Beginner–Intermediate
Concepts: Loops, conditions, functions
Requirements
•	Display a menu with item prices.
•	Let customers select items and quantities.
•	Calculate the running bill.
•	Apply discounts based on the bill amount.
•	Calculate the final bill, including tax.
Bonus: Add coupon codes and repeat-order functionality.
'''

def take_order(bill):
    


def restraunt():
    bill = {}
    while True:
        print("1. Paneer: 250Rs")
        print("2. Raita: 50Rs")
        print("3. Cigar roll: 500Rs")
        print("4. Crispy Corn: 150Rs")
        print("Exit")

        choice = int(input("Enter your choice: "))
        if choice <1 or choice > 4:
            print("Enter a valid choice!!!")
            continue
        if choice == 1:
            take_order()        