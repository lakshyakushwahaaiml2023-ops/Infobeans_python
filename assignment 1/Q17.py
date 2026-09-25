sal = float(input("Enter your salary: "))
match sal:
    case s if(s <= 10000):
        print(f"Basic Salary: {sal} + HRA: {sal/5} + DA: {(sal*4)/5} = {sal + (sal/5) + (sal*4)/5}" )
    case s if(s <= 20000):
            print(f"Basic Salary: {sal} + HRA: {sal/4} + DA: {(sal*9)/10} = {sal + (sal/4) + (sal*9)/10}")
    case s if(s > 20000):
            print(f"Basic Salary: {sal} + HRA: {(sal*3)/10} + DA: {(sal*95)/100} = {sal + (sal*3)/10 + (sal*95)/100}" )