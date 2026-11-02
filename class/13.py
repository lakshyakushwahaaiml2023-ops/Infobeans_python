'''11. Write a Java program to create a class called "Library" with a collection of books and methods to add and remove books.
'''

class Book:
    def __init__(self, name, isbn, author):
        self.__name = name
        self.__isbn = isbn
        self.__author = author

    def __str__(self):
        return f"Book Name: {self.__name}\nAuthor: {self.__author}\nISBN: {self.__isbn}"

class Library:
    __collection = {}
    __count_books = 0

    def add_books(self, name, isbn, author):
        Library.__count_books += 1
        b1 = Book(name, isbn, author)
        Library.__collection[name] = b1
        print("Book Added to the collection!")

    def remove_book(self, name):
        if name not in Library.__collection:
            print("{name} is not available in the Library Collection!")
        else:
            print(f"{name} removed from the collection!")
            Library.__collection.pop(name)
            Library.__count_books -= 1

    @classmethod
    def view_collection(cls):
        print(f"Total Books : {cls.__count_books}")
        for value in cls.__collection.values():
            print(value)
            print("="*20)


l = Library()
l.add_books("Harry Potter", 10001, "JK Rowling")
l.add_books("The Alchemist", 10002, "Paulo Coelho")
l.add_books("Atomic Habits", 10003, "James Clear")
l.add_books("Rich Dad Poor Dad", 10004, "Robert Kiyosaki")
l.add_books("The Psychology of Money", 10005, "Morgan Housel")
l.add_books("Think and Grow Rich", 10006, "Napoleon Hill")
l.add_books("Wings of Fire", 10007, "APJ Abdul Kalam")
l.add_books("The Great Gatsby", 10008, "F. Scott Fitzgerald")
l.add_books("1984", 10009, "George Orwell")

l.view_collection()

l.remove_book("Wings of Fire")
l.remove_book("The Great Gatsby")

l.view_collection()