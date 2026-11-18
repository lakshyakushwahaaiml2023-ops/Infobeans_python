'''9. Library Management

Parent:

LibraryItem

Derived:

Book
Magazine
Newspaper

Implement borrowing system.'''

class LibraryItem:

    def __init__(self, name, cat):
        self.__name = name
        self.__cat = cat
        self.__status = "Available"

    def borrow(self):
        if self.__status == "Available":
            print("Issued succesfully...")
            self.change_status()
        else:
            print("Item already issued...")

    def return_book(self):
        print("Item Returned successfully...")
        self.change_status()

    def change_status(self):
        if self.__status == "Available":
            self.__status = "Issued"
        else:
            self.__status = "Available"

    def __str__(self):
        return f"{self.__cat} --> {self.__name} --> {self.__status}"


class Book(LibraryItem):

    def __init__(self, name):
        super().__init__(name, "Book")

class Magazine(LibraryItem):

    def __init__(self, name):
        super().__init__(name, "Magazine")

class NewsPaper(LibraryItem):

    def __init__(self, name):
        super().__init__(name, "NewsPaper")


class LMS:

    def __init__(self):
        self.__items = {}

    def add_item(self, name, cat):
        match cat:
            case "Magazine":
                self.__items[name] = Magazine(name)
            case "NewsPaper":
                self.__items[name] = NewsPaper(name)
            case "Book":
                self.__items[name] = Book(name)
            case _:
                print("Enter a valid category...")
     

    def borrow(self, name):
        if name not in self.__items:
            print("Item not available...")
        else:
            self.__items[name].borrow()

    def viewItems(self):
        for i in self.__items.values():
            print(i)


l = LMS()
l.add_item("Harry Potter", "Book")
l.add_item("Times of India", "NewsPaper")
l.add_item("Times Now", "Magazine")
l.viewItems()
l.borrow("Harry Potter")
l.borrow("Wings of Fire")
l.viewItems()

            
