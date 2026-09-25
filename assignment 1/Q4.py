marks = float(input("Enter the marks: "))
match marks:
    case m if  m > 80:
            print("Your grade is A")
    case m if m >=60:
            print("Your grade is B") 
    case m if m >=50:
              print("Your grade is C")
    case m if m >= 45:
                print("Your grade is D")
    case m if m >= 25:
                print("Your grade is E")
    case m if m < 25:
                print("Your grade is F")
