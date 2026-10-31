'''5. Write a Java program to create a class called "Book" with attributes for title, author, and ISBN, 
and methods to add and remove books from a collection.
'''

class Book:
    def __init__(self, n, a, i):
        self.__name = n
        self.__author = a
        self.__isbn = i

    def view_details(self):
        print(f"Book Name: {self.__name}")
        print(f"Book Author: {self.__author}")
        print(f"ISBN: {self.__isbn}")

class Collection:
    def __init__(self):
        self.__name = ""
        self.__collection = {}

    def set_name(self,n):
        self.__name = n

    def add_book(self):
        name = input("Enter Book Name: ")
        author = input("Enter Author name: ")
        isbn = input("Enter ISBN no. : ")
        b = Book(name, author, isbn)
        self.__collection[name] = b

    def remove_book(self):
        name = input("Enter Book Name to Remove: ")
        if name not in self.__collection:
            print(f"The book {name} does not exist in collection")
        else:
            print(f"Book {name} removed from the collection")
            self.__collection.pop(name)

    def view_collection(self):
        print(f"{self.__name}'s Book Collection: ")
        for book in self.__collection:
            self.__collection[book].view_details()
        print()

c1 = Collection()
c1.set_name("Lakshya")
c1.add_book()
c1.add_book()
c1.add_book()
c1.view_collection()
c1.remove_book()
c1.view_collection()