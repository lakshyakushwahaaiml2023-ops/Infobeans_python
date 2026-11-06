'''4. Student Grade System
Problem

Create a student result management system.

Requirements

Each student should have:

roll number
name
marks in 3 subjects
Functionalities
Calculate total marks
Calculate percentage
Assign grade:
A → 90+
B → 75+
C → 50+
Fail otherwise
Track total students
Concepts Practiced
instance methods
conditional logic in classes
object-based calculations'''

class Student:
  __count = 0
  
  def __init__(self, rn, name, m1, m2, m3):
    Student.__count += 1
    self.__rollno = rn
    self.__name = name
    self.__marks1 = m1
    self.__marks2 = m2
    self.__marks3 = m3
    self.__total = m1 + m2 + m3
    self.__perc = Student.calc_perc(m1, m2, m3)
    self.__grade = Student.calc_grade(self.__perc)

  @staticmethod
  def calc_perc(m1, m2, m3):
    return (m1 + m2 + m3)/3

  @staticmethod
  def calc_grade(perc):
    match perc:
      case p if perc >= 90:
        return "A"
      case p if perc >= 75:
        return "B"
      case p if perc >= 50:
        return "C"
      case p if perc < 50:
        return "Fail"
        
  @classmethod
  def total_studs(cls):
    return cls.__count

  def __str__(self):
    return f"Roll Number: {self.__rollno} | Name: {self.__name} | Total Marks: {self.__total} | Percentage: {self.__perc : .2f} | Grade: {self.__grade}"


s1 = Student(1, "Atul", 78, 89, 94)
s2 = Student(2, "Aaradhya", 58, 69, 34)
s3 = Student(3, "Akhil", 50, 45, 24)
s4 = Student(4, "Aarav", 10, 20, 30)
s5 = Student(5, "Arya", 55, 60, 50)
s6 = Student(6, "Lakshya", 100, 100, 100)
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)
print(f"Total Students: {Student.total_studs()}")
