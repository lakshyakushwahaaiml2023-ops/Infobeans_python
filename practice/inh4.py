from abc import ABC, abstractmethod

class A(ABC):

    @abstractmethod
    def func(self):
        print("A called")

class B(A):
    def func(self):
        print("B called")

a = B()
a.func()

'''- Abstract calss is used to provide partial implementation
- cannot create objects of abstract calss
- abstract class is always a base class
- to use abstract class we need a child class and override 
  all abstract method in child class'''