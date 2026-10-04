from datetime import date

name = input("Enter your name: ")
gen = input("Enter your gender (M/F): ")

items = []
k = 0

while True:
    print("1. New Item\n2. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item_name = input("Item Name: ")
        item_cost = int(input("Enter cost: "))
        item_qty = int(input("Quantity: "))
        k+=1
        total = 0
        if k == 1 and item_qty >= 4:
            total = (item_cost * item_qty)*0.95
        elif k == 5:
            total = (item_qty * item_cost)*0.9
        elif k == 10:
            total = (item_qty * item_cost)*0.85
        else: 
            total = (item_qty * item_cost)
        items.append([item_name, item_qty, item_cost, item_cost*item_qty, total])
    elif choice == 2:
        break
    else:
        print("Enter a valid choice!!")
bag = input("Do you want a bag (Y/N): ")
bag_c = 0.00
if bag == 'Y':
    bag_c = 10
else:
    bag_c = 0.00

ap = bag_c
dp = None

for i in items:
    ap += i[4]
if ap > 10000:
    dp = ap * 0.85
elif ap < 10000 and ap >= 5000:
    dp = ap * 0.90
else:
    dp = ap

gift = None

if gen == 'M':
    gift = "Cadburry"
else:
    gift = "Leather Wallet"

gst = ap * 0.1
    
print(" "*23,"D-Mart")
print(f"Name: {name}                            Date: {date.today()}")
print("-"*58)
print("Item Name    Quantity    Price    Total    After-Discount")
for i in items:
    print(i[0], " "*10, i[1], " "*7, i[2], " "*5, i[3], " "*5, i[4])
print("-"*58)
print(" "*34, "A.P.       D.P.")
print(" "*34, f"{ap}       {dp}")
print(f"Gift: {gift}!!", " "*21, "0.00       0.00")
print()
print(f"Carry Bag: {bag}", " "*19, f"{bag_c}      {bag_c}")
print("GST (10%): ", " "*22, f"{gst}     {gst}")
print("-"*58)
print(" "*34, f"{ap + gst}       {dp + gst}")
print(" "*20, "Thank You!!")
print(" "*21, "To Visit")
print(" "*22, "D- Mart")