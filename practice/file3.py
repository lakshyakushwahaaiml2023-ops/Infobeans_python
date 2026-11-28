import pickle

class Employee:
    def __init__(self, name, emp_id, salary, department):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        self.department = department

    def __str__(self):
        return f"Employee Name: {self.name} | Employee ID: {self.emp_id} | Salary: {self.salary} | Department: {self.department}"
    
    

def write():
    try:
        with open("employee.pkl", "a+b") as f:
            emp1 = Employee("Lakshya", 1001, 50000, "AI-ML")
            emp2 = Employee("Diksha", 1002, 60000, "Data Science")
            pickle.dump(emp1, f)
            pickle.dump(emp2, f)
            print("Employee data saved successfully...")

    except OSError as e:
        print(e)

def read():
    try:
        with open("employee.pkl", "rb") as f:
            while True:
                e = pickle.load(f)
                print(e)
    except EOFError as e:
        print("End of file reached...")
    except OSError as e:
        print(e)

write()
read()