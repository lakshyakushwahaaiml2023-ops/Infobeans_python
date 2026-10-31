'''8. Write a Java program to create class called "TrafficLight" with attributes for color and duration, 
and methods to change the color and check for red or green.
'''
import time

class TrafficLight:
    def __init__(self):
        self.__color = "Red"
        self.__duration = 0

    def change_color(self):
        if self.__color == "Red":
            self.__color = "Yellow"
        elif self.__color == "Yellow":
            self.__color = "Green"
        elif self.__color == "Green":
            self.__color = "Red"

    def set_duration(self, d):
        self.__duration = d

    def working(self):
        count = 0
        while count <= 5:
            self.change_color()
            print(self.__color,"...")
            print()
            for sec in range(1, self.__duration + 1):
                print(sec, end = " ")
                time.sleep(1)
            print()
            
            count += 1
        print(self.__color,"...")

t1 = TrafficLight()
t1.set_duration(5)
t1.working()