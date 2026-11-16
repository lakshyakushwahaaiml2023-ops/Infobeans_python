from abc import ABC, abstractmethod
class Animal(ABC):
    @property
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    sound = "Barking"

d = Dog()
print(d.sound)
    