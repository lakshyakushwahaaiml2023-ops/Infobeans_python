'''11. Company Hierarchy
Person
Employee(Person)
Manager(Employee)

Display company hierarchy.'''

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
         return self.__name

    def get_age(self):
         return self.__age

    def __str__(self):
        return f"{self.__name} | {self.__age}"

class Employee(Person):
    def __init__(self, name, age, empid, sal):
        super().__init__(name, age)
        self.__empid = empid
        self.__sal = sal

    def get_empid(Self):
         return Self.__empid

    def get_sal(self):
         return self.__sal

    def __str__(self):
        return f"{self.get_name()} | {self.get_age()} | {self.__empid} | {self.__sal}"

class Manager(Employee):
    def __init__(self, name, age, empid, sal, teamSize, department):
            super().__init__(name, age, empid, sal)
            self.__teamSize = teamSize
            self.__dept = department
            

    def __str__(self):
            return f"{self.get_name()} | {self.get_age()} | {self.get_empid()} | {self.get_sal()} | {self.__teamSize} | {self.__dept}"

p = Person("Lakshya", 22)
print(p)

e = Employee("Lakshya", 22, 1001, 120000)
print(e)   

m = Manager("Lakshya", 22, 1001, 200000, 4, "AIML")
print(m)