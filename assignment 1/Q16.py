maths = int(input("Enter marks in Maths: "))
physics = int(input("Enter marks in Physics: "))
chemistry = int(input("Enter marks in Chemistry: "))
biology = int(input("Enter marks in Biology: "))
computer = int(input("Enter marks in Computer: "))

perc = (maths + physics + biology + chemistry + computer)/5

print(f"Percentage : {perc}%")

match perc:
    case p if(p >= 90):
        print("Grade A")
    case p if(p >= 80):
            print("Grade B")
    case p if(p >= 70):
            print("Grade C")
    case p if(p >= 60):
            print("Grade D")
    case p if(p >= 40):
            print("Grade E")
    case p if(p < 40):
            print("Grade F")