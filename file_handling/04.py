
class Student:
    def __init__(self, name, branch, roll_no):
        self.__name = name
        self.__branch = branch
        self.__roll_no = roll_no

    def get_details(self):
        return f"{self.__name} | {self.__branch} | {self.__roll_no}\n"


class College:
    def __init__(self, name, location):
        self.__name = name
        self.__location = location
        self.__students = {}
        self.__count = 0

    def get_students(self):
        return self.__students.copy()

    def add_student(self, name, branch, roll_no):
        s = Student(name, branch, roll_no)

        self.__count += 1
        self.__students[name] = self.__count

        try:
            with open("students.txt", "a") as f:
                f.write(s.get_details())

        except OSError:
            print("Error while writing to file...")

    def view_detail(self, name):
        try:
            with open("students.txt", "r") as f:
                lines = f.readlines()

                index = self.__students[name] - 1
                print(lines[index], end="")

        except FileNotFoundError:
            print("File not found...")

        except KeyError:
            print("Student not found...")

        except IndexError:
            print("Student record not found...")


c = College("IIST", "Indore")

c.add_student("Riya", "AIML", "0818CL231055")


c.view_detail("Lakshya")
c.view_detail("Diksha")
