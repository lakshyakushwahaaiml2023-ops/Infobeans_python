'''12. University System
Person
Student(Person)
GraduateStudent(Student)

Add thesis information.'''

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

class Student(Person):
    def __init__(self, name, age, enrid, branch):
        super().__init__(name, age)
        self.__enrid = enrid
        self.__branch = branch

    def __str__(self):
        return f"{self.get_name()} | {self.get_age()} | {self.__enrid} | {self.__branch}"

    def get_enrid(self):
        return self.__enrid

    def get_branch(self):
        return self.__branch

class Graduate(Student):
    def __init__(self, name, age, enrid, branch, p_year, thesisTitle, researchDomain):
        super().__init__(name, age, enrid, branch)
        self.__p_year = p_year
        self.__jobStatus = thesisTitle
        self.__rd = researchDomain

    def __str__(self):
        return f"{super().__str__()} | {self.__p_year} | {self.__jobStatus} | {self.__rd}"


p = Person("Lakshya", 22)
print(p)

s = Student("Lakshya", 22, "0818CL231039", "AIML")
print(s)

g = Graduate("Lakshya", 22, "0818CL231039", "AIML", 2027, "PINN", "Deep Learning")
print(g)