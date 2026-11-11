'''18. School Classroom System
Problem

Create classroom system.

Requirements

Classroom should:

maintain student objects
maintain class teacher
Functionalities
Add student
Remove student
Display class strength
Concepts Practiced
object aggregation
collections of objects'''

class Student:
  def __init__(self, rn, name):
    self.__rn = rn
    self.__name = name

  def __str__(self):
    return f"{self.__rn} | {self.__name}"

class Teacher:
  def __init__(self, name, sub):
    self.__name = name
    self.__sub = sub

  def __str__(self):
    return f"{self.__sub} | {self.__name}"

class CMS:
  def __init__(self, grade, section):
    self.__grade = grade
    self.__sec = section
    self.__students = {}
    self.__teachers = {}

  def add_student(self, rn, name):
    if rn in self.__students:
      print("Student already exists with given roll number!!!")
    else:
      self.__students[rn] = Student(rn, name)
      print("Student Added Succesfully into system!!!")

  def remove_student(self, rn):
    if rn in self.__students:
      self.__students.pop(rn)
      print("Student removed from data!!!")
    else:
      print("No student with given roll number exists!!!")

  def add_teacher(self, sub, name):
    self.__teachers[sub] = Teacher(name, sub)
    print("Teacher data updated succesfully!!!")

  def view_class(self):
    print(f"\nClass: {self.__grade} {self.__sec}")
    print("\nTeachers: ")
    for teacher in self.__teachers.values():
      print(teacher)
    print("\nStudents: ")
    for student in self.__students.values():
      print(student)

  def class_strength(self):
    print(f"Class Strength: {len(self.__students)}")

s = CMS("ITEP", "20")
s.add_teacher("English", "Ms. Sonia Samadhiya")
s.add_teacher("Python", "Mr. Pawan Sahu")
s.add_teacher("Phoenetics", "Capt. B.J. Singh")

s.add_student(1, "Lakshya")
s.add_student(2, "Diksha")
s.add_student(3, "Smruti")
s.add_student(4, "Riya")
s.add_student(5, "Kapil")
s.add_student(6, "Prabhat")
s.add_student(7, "Farhan")
s.add_student(8, "Gourav")
s.add_student(9, "Tanisha")
s.add_student(10, "Monty")
s.view_class()
s.class_strength()  
