'''1. Employee Management System
Problem

Create an Employee class to manage employee details.

Requirements

Each employee should have:

employee id
name
department
salary
Functionalities
Display employee details
Increase salary by percentage
Count total employees created using a class variable

Create employee object from a string:

"101-Rahul-IT-50000"

using a class method.

Concepts Practiced
constructor
instance variables
class variables
class method
instance methods'''

class Employee:

  __obj_count = 0
  __employees = {}
  
  def __new__(cls, id, n, d, s):
    obj = super().__new__(cls)
    obj.__empid = id
    obj.__name = n
    obj.__department = d
    obj.__salary = s
    return obj

  @classmethod
  def create_obj(cls, details):
    id, name, dep, sal = details.split('-')
    if id not in Employee.__employees:
      obj = Employee(id, name, dep,int(sal))
      Employee.__employees[id] = obj
      Employee.__obj_count += 1
      return obj
    else:
      print("Employee ID already exists!!!!")


  def __str__(self):
    return f"Employee ID: {self.__empid} | Name: {self.__name} | Department: {self.__department} | Salary: {self.__salary}"

  def increase_sal(self, perc):
    self.__salary += self.__salary * perc / 100

  @classmethod
  def show_total_objects(cls):
    return cls.__obj_count


e1 = Employee.create_obj("101-Lakshya-AIML-120000")
e2 = Employee.create_obj("102-Rahul-IT-50000")
e3 = Employee.create_obj("103-Karan-DS-65000")
print(e1)
print(e2)
print(e3)
print(Employee.show_total_objects())
