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
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        return func(a,b)
    return wrap

def greater_first(func):
    def wrap():
        if a < b:
            a, b = b, a
        return func(a,b)
    return wrap


@take_input
def add(a,b):
    return a + b

@greater_first
@take_input
def sub(a,b):
    return a - b

@take_input
def mul(a,b):
    return a * b

@greater_first
@take_input
def div(a,b):
    return a / b

@greater_first
@take_input
def mod(a,b):
    return a % b

@greater_first
@take_input
def sub(a,b):
    return a ** b

@greater_first
@take_input
def floor_div(a,b):
    return a // b



def calculator():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Floor Division")
    print("8. Exit")

    choice = int(input("Enter your choice (1 - 9): "))

    match choice:
        case 1:
            print("Addition : ", add())
            calculator()
        case 2:
            print(f"Difference : {sub()}")
            calculator()
        case 3:
            print(f"Multiplication : {mul()}")
            calculator()
        case 4:
            print(f"Division : {div()}")
            calculator()
        case 5:
            print(f"Modulus : {mod()}")
            calculator()
        case 6:
            print(f"Power : {pow()}")
            calculator()
        case 7:
            print(f"Floor Division : {floor_div()}")
            calculator()
        case 8:
            return
calculator()



