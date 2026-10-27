'''
8. Employee Attendance and Salary Calculator
Intermediate
Concepts: Conditions, loops, functions, dictionaries
Requirements
•	Enter employee details and days present.
•	Calculate attendance percentage.
•	Calculate salary based on days worked.
•	Apply a bonus or deduction according to attendance rules.
•	Generate an employee summary.

'''


employee_data = {}
TOTAL_DAYS = 30
DAILY_SALARY = 1000


def get_name(func):
    def wrap():
        name = input("Enter employee name: ").strip()
        return func(name)
    return wrap


def get_attendance(func):
    def wrap(name):
        att = int(input("Enter days present (0-30): "))

        if att < 0 or att > TOTAL_DAYS:
            print("Invalid attendance. Enter days between 0 and 30.")
            return

        return func(name, att)
    return wrap


@get_name
@get_attendance
def add_employee(name, att):
    employee_data[name] = {
        "days_present": att,
        "attendance": 0,
        "salary": 0,
        "bonus_multiplier": 1
    }
    print("Employee data added!")


@get_name
def calc_attendance(name):
    if name not in employee_data:
        print("Name not available in database")
        return

    att = employee_data[name]["days_present"]
    percentage = (att / TOTAL_DAYS) * 100

    employee_data[name]["attendance"] = percentage
    print(f"Attendance: {percentage:.2f}%")


@get_name
def calc_salary(name):
    if name not in employee_data:
        print("Name not available in database")
        return

    days = employee_data[name]["days_present"]
    salary = days * DAILY_SALARY

    employee_data[name]["salary"] = salary
    print(f"Salary of {name}: Rs {salary}")


@get_name
def calc_bonus(name):
    if name not in employee_data:
        print("Name not available in database")
        return

    days = employee_data[name]["days_present"]

    if days > 24:
        multiplier = 1.20
    elif days >= 17:
        multiplier = 1.05
    elif days >= 11:
        multiplier = 1.00
    else:
        multiplier = 0.75

    base_salary = days * DAILY_SALARY
    final_salary = base_salary * multiplier

    employee_data[name]["bonus_multiplier"] = multiplier
    employee_data[name]["salary"] = final_salary

    print(f"Salary after bonus/deduction: Rs {final_salary:.2f}")


@get_name
def employee_summary(name):
    if name not in employee_data:
        print("Name not available in database")
        return

    data = employee_data[name]

    print("\n--- Employee Summary ---")
    print(f"Name: {name}")
    print(f"Days Present: {data['days_present']}")
    print(f"Attendance: {data['attendance']:.2f}%")
    print(f"Salary: Rs {data['salary']:.2f}")
    print(f"Bonus Multiplier: {data['bonus_multiplier']}")


def EMS():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Enter Employee Data")
        print("2. Calculate Attendance")
        print("3. Calculate Salary")
        print("4. Bonus / Deduction")
        print("5. Employee Summary")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice < 1 or choice > 6:
            print("Enter a valid choice (1-6)")
            continue

        if choice == 1:
            add_employee()
        elif choice == 2:
            calc_attendance()
        elif choice == 3:
            calc_salary()
        elif choice == 4:
            calc_bonus()
        elif choice == 5:
            employee_summary()
        elif choice == 6:
            print("Exited")
            break


EMS()
print(employee_data)
