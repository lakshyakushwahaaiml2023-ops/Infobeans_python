cost = float(input("Enter price of bike: "))
match cost:
    case p if(p > 100000):
        print("Road Tax: ",15*p/100)
    case p if(p > 50000):
        print("Road Tax: ",p/10)
    case p if(p <= 50000):
        print("Road Tax: ",p/20)