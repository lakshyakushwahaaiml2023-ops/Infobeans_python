'''68. Report Card Generator
Problem Statement

Different grading systems exist.

Create:

abstract class Student

Child:

SchoolStudent
CollegeStudent

Each generates grades differently.'''

from abc import ABC, abstractmethod

class Student(ABC):
    @abstractmethod
    def generate_grade(self):
        pass

class SchoolStudent(Student):

    def __init__(self, u1_perc, u2_perc, half_yearly_perc, yearly_perc):
        self.__u1 = u1_perc
        self.__u2 = u2_perc
        self.__half_yearly = half_yearly_perc
        self.__yearly = yearly_perc

    def generate_grade(self):
        total = (self.__u1 + self.__u2 + self.__half_yearly + self.__yearly) / 4
        if total >= 90:
            return "A+"
        elif total >= 80:
            return "A"
        elif total >= 70:
            return "B"
        elif total >= 60:
            return "C"
        else:
            return "D"
class CollegeStudent(Student):

    def __init__(self, mid_sem_perc, end_sem_perc, external_perc):
        self.__sem1 = mid_sem_perc
        self.__sem2 = end_sem_perc
        self.__sem3 = external_perc

    def generate_grade(self):
        total = (self.__sem1 + self.__sem2 + self.__sem3) / 3
        if total >= 90:
            return "A+"
        elif total >= 80:
            return "A"
        elif total >= 70:
            return "B"
        elif total >= 60:
            return "C"
        else:
            return "D"

studs = [SchoolStudent(90, 80, 70, 60), CollegeStudent(90, 80, 70)]
for stud in studs:
    print(stud.generate_grade())