a = int(input("Enter a number (a): "))
b = int(input("Enter a number (b): "))

op = input("Enter a operation (+, <>, =): ")
if(op not in "+<>="):
    print("Not a valid operator")

match op:
    case '+':
        print("a + b : ", a+b)
    case '<':
        print("a < b : ", a<b)
    case '>':
        print("a > b : ", a>b)
    case '=':
        print("a = b : ", a==b)