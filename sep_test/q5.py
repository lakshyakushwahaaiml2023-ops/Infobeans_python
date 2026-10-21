high = float('-inf')
low = float('inf')
res = []
sum = 0
num_stud = 0

while True:
    print("1. Enter student marks")
    print("2. Display average marks")
    print("3. Display highest marks")
    print("4. Display lowest marks")
    print("5. Display result")
    print("6. Exit")

    choice = int(input("Enter your choice(1 - 6): "))
    

    match choice:
        case 1: 
            num_stud +=1
            python = int(input("Enter marks in python: "))
            db = int(input("Enter marks in database: "))
            prog = int(input("Enter marks in programming: "))
            highest = max(python, db, prog)
            lowest = min(python, db, prog)
            avg = (python + db + prog)/3
            if high < highest:
                high = highest
            if low > lowest:
                low = lowest
            sum += python + db + prog
            if python < 40 or db < 40 or prog < 40 or ((sum*100)/300) < 50 :
                res.append("Fail")
            else:
                res.append("Pass")
        case 2:
            print(f"Average marks of {num_stud} students: {sum / num_stud}")
        case 3:
            print(f"Highest marks: {high}")
        case 4:
            print(f"Lowest marks: {low}")
        case 5:
            k = 1
            for i in res:
                print(f"Student {k}: {i}")
                k+=1
        case 6:
            break
        case _:
            print("Invalid choice. Please enter a valid choice (1 - 6).")