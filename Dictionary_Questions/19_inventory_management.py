inventory = {}

while True:
    print("Add stock => 1")
    print("Sell stock => 2")
    print("Show Inventory => 3")
    print("Exit => 4")

    choice = int(input("Enter your choice (1 - 4) : "))

    match choice:
        case 1:
            item = input("Item name: ")
            qty = int(input("Item quantity: "))
            inventory[item] = inventory.get(item, 0) + qty
        case 2:
            item = input("Item name: ")
            qty = int(input("Item quantity: "))
            inventory[item] -= qty
        case 3:
            print("="*20)
            for i in inventory.items():
                print(i)
            print("="*20)
        case 4:
            break
        case _:
            print("Enter a valid choice!!")