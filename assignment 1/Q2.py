quant = int(input("Enter quantity: "))
cost = quant*100
if cost >= 1000:
    cost = 9*cost/10  
    print(cost)
else:
    print(cost)