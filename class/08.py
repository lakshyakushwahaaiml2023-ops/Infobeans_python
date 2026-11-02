'''6. Write a Java program to create a class called "Employee" with a name, job title, and salary attributes, 
and methods to calculate and update salary.
'''

class Employee:
    def __init__(self, n, s, j):
        self.__name = n
        self.__salary = s
        self.__job_title = j

    def calc_salary(self):
        if self.__job_title == "Manager":
            self.__salary = 100000
        if self.__job_title == "Employee":
            self.__salary = 25000
        if self.__job_title == "CEO":
            self.__salary = 150000
        if self.__job_title == "Owner":
            self.__salary = 250000

    def update_salary(self, sal):
        self.__salary = sal

    def view_details(self):
        print(f"Name: {self.__name}")
        print(f"Job title: {self.__job_title}")
        print(f"Salary: {self.__salary} Rs")

e1 = Employee("Lakshya", 120000, "Manager")
e1.view_details()
e1.calc_salary()
e1.view_details()
e1.update_salary(150000)
e1.view_details()