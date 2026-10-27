'''
1. Smart Calculator
Beginner
Concepts: if-elif-else, while, functions
Requirements
•	Display a menu for addition, subtraction, multiplication, division, and modulus.
•	Take two numbers from the user.
•	Use separate functions for each operation.
•	Handle division by zero.
•	Repeat until the user selects Exit.
Bonus: Add power and floor division operations.
'''



def take_input(func):
    def wrap():
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        return func(a, b)
    return wrap


def greater_first(func):
    def wrap(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return wrap


@take_input
def add(a, b):
    return a + b


@take_input
def sub(a, b):
    return a - b


@take_input
def mul(a, b):
    return a * b

@take_input
def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

@take_input
def mod(a, b):
    if b == 0:
        return "Cannot perform modulus by zero"
    return a % b


@take_input
def power(a, b):
    return a ** b


@take_input
def floor_div(a, b):
    if b == 0:
        return "Cannot perform floor division by zero"
    return a // b


def calculator():
    while True:
        print("\n--- Smart Calculator ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Power")
        print("7. Floor Division")
        print("8. Exit")

        choice = int(input("Enter your choice (1-8): "))

        match choice:
            case 1:
                print("Addition:", add())

            case 2:
                print("Subtraction:", sub())

            case 3:
                print("Multiplication:", mul())

            case 4:
                print("Division:", div())

            case 5:
                print("Modulus:", mod())

            case 6:
                print("Power:", power())

            case 7:
                print("Floor Division:", floor_div())

            case 8:
                print("Calculator closed.")
                break

            case _:
                print("Invalid choice. Please try again.")


calculator()