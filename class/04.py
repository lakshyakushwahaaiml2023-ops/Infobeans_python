'''
2. Write a Java program to create a class called "Dog" with a name and breed attribute. 
Create two instances of the "Dog" class, set their attributes using the constructor and modify the attributes using the 
setter methods and print the updated values.
'''
class Dog:
    def __init__(self, n, b):
        self.__name = n
        self.__breed = b

    def set_name(self,n):
        self.__name = n

    def set_breed(self, b):
        self.__breed = b

    def view_details(self):
        print(f"Dog Name: {self.__name}")
        print(f"Dog Breed: {self.__breed}")
        print()

d1 = Dog("Eren", "Street Dog")
d1.view_details()

d1.set_breed("Chiweenie")
d1.set_name("Go-Go")
d1.view_details()