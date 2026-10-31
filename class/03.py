'''1. Write a Java program to create a class called "Person" with a name and age attribute. 
Create two instances of the "Person" class, set their attributes using the constructor, and print their name and age.
'''
class Person:
    def __init__(self, n, a):
        self.__name = n
        self.__age = a

    def print_d(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print()

p1 = Person("Lakshya", 21)
p2 = Person("Diksha", 21)

p1.print_d()
p2.print_d()
    