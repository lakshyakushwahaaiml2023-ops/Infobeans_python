'''12. Write a Java program to create a class called "Airplane" with a flight number, destination, 
and departure time attributes, and methods to check flight status and delay.
'''
from datetime import date
class Time:
    def __init__(self, hr, min):
        self.__hr = hr
        self.__min = min

    def set_time(self, hr, min):
        self.__hr = hr
        self.__min = min

    def add_mins(self, mins):
        self.__min = mins + self.__min
        if self.__min >= 60:
            self.__hr += 1
            self.__min -= 60

    def __str__(self):
        return f"{self.__hr} : {self.__min}"


class Airplane:
    def __init__(self, f_no, dest):
        self.__f_no = f_no
        self.__dest = dest
        self.__dep_time = Time(0,0)
        self.__status = "on time"

    def set_dept_time(self, hr, min):
        self.__dep_time.set_time(hr, min)

    def check_status(self):
        print(f"Flight Number: {self.__f_no}")
        print(f"Flight Destination: {self.__dest}")
        print(f"Departure Time: {self.__dep_time}")
        print(f"Flight Status: {self.__status}")

    def delay(self, mins):
        if mins != 0:
            self.__dep_time.add_mins(mins)
            self.__status = "Delayed"


    def __hash__(self):
        return self.__f_nos

    def __eq__(self, other):
        if self.__f_no != other.__f_no:
            return False
        return True

    
bucket = set()

a1 = Airplane(1001, "New York")
a1.set_dept_time(11, 30)
a1.check_status()
a1.delay(31)
a1.check_status()
