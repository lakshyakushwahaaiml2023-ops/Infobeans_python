result = {}
topper = None

while True:
    print("Add student data => 1")
    print("Show student data => 2")
    print("Show all students marks => 3")
    print("Exit => 4")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            name = input("Enter name: ")
            phy = float(input("Enter marks in Physics: "))
            chem = float(input("Enter marks in Chemistry: "))
            maths = float(input("Enter marks in Maths: "))
            avg = (phy + chem + maths)/3
            if topper is None:
                topper = name
            else:
                if result[topper]["Average"] < avg:
                    topper = name
            match avg:
                case m if  m > 80:
                    grade = "A"
                case m if m >=60:
                    grade = "B" 
                case m if m >=50:
                    grade = "C"
                case m if m >= 45:
                    grade = "D"
                case m if m >= 25:
                    grade = "E"
                case m if m < 25:
                    grade = "F"
            result[name] = {"Physics" : phy, "Chemistry" : chem, "Maths" : maths, "Average" : avg, "Grade" : grade}
        case 2:
            name = input("Enter name for details: ")
            if name in result:
                print(result[name])
            else:
              print("No result found for ", name)
        case 3:
            print("="*50)
            for key, value in result.items():
                print(f"{key} : {value}")
            print("="*50)
            print(f"Topper : {topper} => Average : {result[topper]["Average"]}")
        case 4:
            break