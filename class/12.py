'''
10. Write a Java program to create a class called "Student" with a name, grade, and courses attributes, 
and methods to add and remove courses.
'''

class Course:
    def __init__(self, c_name, c_duration):
        self.__c_name = c_name
        self.__c_duration = c_duration
        self.__students = []

    def add_student(self, name):
        self.__students.append(name)

    def view_students(self):
        i = 1
        print(f"Students Enrolled in {self.__c_name}: ")
        for student in self.__students:
            print(f"{i}. {student}")
            i += 1

    def __str__(self):
        return f"Course Name: {self.__c_name}\nCourse Duration: {self.__c_duration}\n"
        

class Student:
    def __init__(self, n, g):
        self.__name = n
        self.__grade = g
        self.__courses = {}

    def enroll_course(self, c_name, c_duration):
        if c_name in self.__courses:
            print(f"Already enrolled in this course!!")
        else:
            print(f"Enrolled into {c_name} for {c_duration} months")
            c = Course(c_name, c_duration)
            self.__courses[c_name] = c
            c.add_student(self.__name)

    def view_courses(self):
        i = 1
        print(f"{self.__name} enrolled in these courses: ")
        for course in self.__courses.keys():
            print(f"{1}. {course}")
            i += 1

    def __str__(self):
        return f"Name: {self.__name}\nGrade: {self.__grade}\n"

s1 = Student("Lakshya", "ITEP-20")
s2 = Student("Diksha", "ITEP-20")
print(s1)       
print(s2) 