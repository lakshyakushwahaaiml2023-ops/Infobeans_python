marks = int(input("Enter percentage: "))
match marks:
    case m if m > 90:
        print("Grade A")
    case m if m > 80:
            print("Grade B")
    case m if m >= 60:
            print("Grade C")
    case m if m < 60:
            print("Grade D")