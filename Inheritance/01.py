'''1. Animal Sound System

Create parent class Animal and child classes:

Dog
Cat
Cow

Override sound() method.'''
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Barks...")

class Cat(Animal):
    def sound(self):
        print("Meowwww...")

class Cow(Animal):
    def sound(self):
        print("Mooooo...")

s = Dog()
s.sound()
s = Cat()
s.sound()
s = Cow()
s.sound()