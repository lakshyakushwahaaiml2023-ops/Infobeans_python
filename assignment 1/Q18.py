units = int(input("Enter the number of electricity units utilized: "))

cost = 0

for i in range(1,units+1):
    if(i <= 50):
        cost = cost + 0.50
    elif(i > 50 and i <= 150):
        cost = cost + 0.75
    elif(i > 150 and i <= 250):
        cost = cost + 1.20
    elif(i > 250):
        cost = cost + 1.50

cost = cost + cost/5

print(f"Final electricity bill: {cost}")