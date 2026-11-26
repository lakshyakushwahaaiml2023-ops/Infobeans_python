'''56. Exam Evaluation System
Problem Statement

Marks are evaluated differently.

Create:

abstract class Exam

Child:

MCQExam
PracticalExam
VivaExam

Each calculates grades differently.'''

from abc import ABC, abstractmethod

class Exam(ABC):
    @abstractmethod
    def calc_grade():
        pass

class MCQExam(Exam):
    __max_marks = 60

    def calc_grade(self, marks):
        match marks:
            case m if m >= 54:
                print("A Grade...")
            case m if m >= 45:
                print("B Grade...")
            case m if m >= 39:
                print("C Grade...")
            case m if m >= 32:
                print("D Grade...")
            case m if m >= 27:
                print("E Grade...")
            case m if m < 27:
                print("Fail...")
            case _:
                print("Enetr valid marks between 0 - 60...")

class PracticalExam(Exam):
    __max_marks = 30

    def calc_grade(self, marks):
        match marks:
            case m if m >= 27:
                print("A Grade...")
            case m if m >= 24:
                print("B Grade...")
            case m if m >= 21:
                print("C Grade...")
            case m if m >= 18:
                print("D Grade...")
            case m if m >= 15:
                print("E Grade...")
            case m if m < 15:
                print("Fail...")
            case _:
                print("Enetr valid marks between 0 - 30...")

class VivaExam(Exam):
    __max_marks = 10

    def calc_grade(self, marks):
        match marks:
            case m if m >= 9:
                print("A Grade...")
            case m if m >= 8:
                print("B Grade...")
            case m if m >= 7:
                print("C Grade...")
            case m if m >= 6:
                print("D Grade...")
            case m if m >= 5:
                print("E Grade...")
            case m if m < 5:
                print("Fail...")
            case _:
                print("Enetr valid marks between 0 - 10...")
                
v = VivaExam()
v.calc_grade(7)