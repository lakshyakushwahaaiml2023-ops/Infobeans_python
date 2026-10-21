a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator: ")

match op:
    case '+': print(f"Result: {a+b}")
    case '-': print(f"Result: {a-b}")
    case '*': print(f"Result: {a*b}")
    case "/": print(f"Result: {a/b}")
    case _ : print("Invalid operator")
    