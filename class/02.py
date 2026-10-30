'''
Employee Record System
Create a class Employee with private fields: id, name, and salary.
Use setter methods to assign values. Add a method to display employee details.
'''

class Employee:
    def __init__(self):
        self.__name = ""
        self.__id = ""
        self.__salary = 0

    def set_id(self):
        id = input("Enter employee id: ")
        self.__id = id
    def set_name(self):
        name = input("Enter employee name: ")
        self.__name = name
    def set_salary(self):
        sal = int(input("Enter employee salary: "))
        self.__salary = sal

    def show_details(self):
        print(f"ID: {self.__id}\nName: {self.__name}/nSalary: {self.__salary} Rs")

e1 = Employee()
e1.set_id()
e1.set_name()
e1.set_salary()
e1.show_details()
