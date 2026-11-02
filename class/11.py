'''9. Write a Java program to create a class called "Employee" with a name, salary, a
nd hire date attributes, and a method to calculate years of service.
'''

from datetime import date

class Employee:
    def __init__(self, n, s):
        self.__name = n
        self.__salary = s
        self.__joinDate = date.today()

    def set_hire_date(self):
        day = int(input("Day: "))
        mon = int(input("Month: "))
        year = int(input("Year: "))
        self.__joinDate = date(year, mon, day)

    def calc_yos(self):
        years = date.today().year - self.__joinDate.year
        if (date.today().month, date.today().day) < (self.__joinDate.month, self.__joinDate.day):
            years -= 1
        return years

    def view_details(self):
        print(f"Name: {self.__name}")
        print(f"Salary: {self.__salary} Rs")
        print(f"Joining Date: {self.__joinDate}")
        print(f"Years of Service: {self.calc_yos()}")

e1 = Employee("Lakshya", 100000)
e1.set_hire_date()
e1.view_details()