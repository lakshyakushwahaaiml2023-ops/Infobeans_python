'''4. Student Management

Base class Person.

Derived:

Student
Teacher

Add role-specific methods.'''

from abc import ABC, abstractmethod

class Person(ABC):

    @abstractmethod
    def role(self):
        pass

class Student(Person):

    def role(self):
        print("Student studies in class...")

class Teacher(Person):

    def role(self):
        print("Teacher teaches in class...")

t = Teacher()
t.role()