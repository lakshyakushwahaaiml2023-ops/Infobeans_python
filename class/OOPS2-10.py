'''10. Company Department System
Problem

Create:

Department
Employee

classes.

Requirements

Each department:

has department name
stores employee objects
Functionalities
Add employee to department
Display all employees
Calculate total department salary
Concepts Practiced
object composition
object interaction
storing objects in lists'''

class Department:
  def __init__(self, dep_name):
    self.__dept_name = dep_name
    self.__employees = []

  def add_employee(self, empid, name, salary):
    e = Employee(empid, name, salary)
    if e in self.__employees:
      print("Employee with same credentials already exists!!!")
    else:
      self.__employees.append(e)
      print("Employee added succesfully to department")

  def total_salary(self):
    sum = 0
    for employee in self.__employees:
      sum += employee.get_salary()
    return sum

  def show_employees(self):
    print("\n====================================\n")
    print(f"Department: {self.__dept_name} : ")
    for employee in self.__employees:
      print(employee)

class Employee:
  def __init__(self, empid, name, sal):
    self.__empid = empid
    self.__name = name
    self.__salary = sal

  def __str__(self):
    return f"{self.__empid} | {self.__name} | Salary: {self.__salary}"

  def get_salary(self):
    return self.__salary

  def __hash__(self):
    return hash(self.__empid, self.__name)

  def __eq__(self, other):
    return (self.__empid, self.__name) == (other.__empid, other.__name)


d = Department("AIML")
d.add_employee(1001, "Lakshya", 120000)
d.add_employee(1002, "Diksha", 200000)
d.show_employees()
print(f"Total salary: {d.total_salary()}")
d1 = Department("IT")
d1.add_employee(2001, "Ishant", 90000)
d1.add_employee(2002, "Riya", 150000)
d1.show_employees()
print(f"Total salary: {d1.total_salary()}")
