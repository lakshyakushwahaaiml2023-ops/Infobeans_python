class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

e1 = Employee("John", 30)
e2 = Employee("John", 30)
print(e1 == e2)
print(Employee.mro())