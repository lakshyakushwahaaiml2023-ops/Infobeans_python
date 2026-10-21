units = int(input("Enter units: "))
bill = 0

if units < 100:
    bill += units * 5
elif units <= 200:
    bill += (100 * 5) + ((units - 100) * 7)
elif units <= 400:  
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
else:
    bill = (100 * 5) + (100 * 7) + (200 * 10) + ((units - 400) * 12)
print(f"Electricity bill: {bill} Rs")


