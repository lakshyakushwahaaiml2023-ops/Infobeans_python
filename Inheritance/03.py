'''3. Employee Management

Base class Employee.

Derived:

Developer
Tester
HR

Calculate salaries differently.'''

from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def role(self):
        pass

class Developer(Employee):

    def role(self):
        print("Role: Developer!!!")

class Tester(Employee):

    def role(self):
        print("Role: Tester!!!")

class HR(Employee):

    def role(self):
        print("Role: HR!!!")

h = HR()
h.role()