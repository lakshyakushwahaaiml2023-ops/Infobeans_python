'''
2. Student Result Management System
Beginner
Concepts: Conditions, loops, functions
Requirements
•	Input marks for five subjects.
•	Calculate total, percentage, and grade.
•	Check whether the student passed or failed.
•	Validate that each mark is between 0 and 100.
•	Create functions such as calculate_total(), calculate_percentage(), and calculate_grade().
Bonus: Accept results for multiple students and calculate the class average
'''

students = {}

def take_name(func):
    def wrap():
        name = input("Enter name of the student: ")
        return func(name)
    return wrap

def take_marks(func):
    def wrap(name):
        phy = int(input("Enter marks in physics: "))
        chem = int(input("Enter marks in chemistry: "))
        maths = int(input("Enter marks in maths: "))
        eng = int(input("Enter marks in english: "))
        comp = int(input("Enter marks in computer: "))
        marks = [phy, chem, maths, eng, comp]

        for i in marks:
            if i < 0 or i > 100:
                print("Enter valid marks (0 - 100)!!")
                return 

        return func(name, marks)
    return wrap

def calc_total(marks):
    sum = 0
    for i in marks:
        sum += i
    return sum

def calc_percetage(total):
    return total / 5

def calc_grade(perc):
    match perc:
        case p if p < 30:
            return "F"
        case p if p < 50:
            return "D"
        case p if p < 60:
            return 'C'
        case p if p < 80:
            return "B"
        case p if p >= 80:
            return "A"

def check_pass_fail(marks, grade):
    if grade == "F":
        return "Fail"
    for  i in marks:
        if i < 30:
            return "Fail"
    return "Pass"


@take_name
@take_marks
def SMS(name, marks):
    total = calc_total(marks)
    perc = calc_percetage(total)
    grade = calc_grade(perc)
    status = check_pass_fail(marks, grade)

    students[name] = {
        "marks" : marks,
        "total" : total,
        "percentage" : perc,
        "grade" : grade,
        "status" : status
    }

num = int(input("Enter number of students: "))
for i in range(num):
    SMS()

for key, value in students.items():
    print("==============================================================")
    print(key)
    for elements, vals in value.items():
        print(f"{elements} : {vals}")
    print("==============================================================")



    
    