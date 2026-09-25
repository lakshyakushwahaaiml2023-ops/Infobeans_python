sal = int(input("Enter the salary: "))
yr = int(input("Enter the year of service: "))
if yr > 5:
    bonus = sal/20
    print("This is the net bonus: ",bonus)
else:
    print("There is no bonus")