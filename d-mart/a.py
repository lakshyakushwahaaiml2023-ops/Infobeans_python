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

print("=" * 75)
print(f"{'D-Mart':^75}")

print(f"{'Name: ' + name:<45}{'Date: ' + date.today().strftime('%d/%m/%Y'):>30}")

print("-" * 75)

print(f"{'Item Name':<15}{'Quantity':>10}{'Price':>10}{'Total':>10}{'After-Discount':>20}")

print("-" * 75)

for i in items:
    print(f"{i[0]:<15}{i[1]:>10}{i[2]:>10}{i[3]:>10}{i[4]:>20.2f}")

print("-" * 75)

print(f"{'':<45}{'A.P.':>10}{'D.P.':>15}")
print(f"{'':<45}{ap:>10.2f}{dp:>15.2f}")

print(f"{'Gift: ' + gift:<45}{0:>10.2f}{0:>15.2f}")

print(f"{'Carry Bag: ' + bag:<45}{bag_c:>10.2f}{bag_c:>15.2f}")

print(f"{'GST (10%)':<45}{gst:>10.2f}{gst:>15.2f}")

print("-" * 75)

print(f"{'':<45}{ap + gst:>10.2f}{dp + gst:>15.2f}")

print()
print(f"{'Thank You!!':^75}")
print(f"{'To Visit':^75}")
print(f"{'D-Mart':^75}")

print("=" * 75)