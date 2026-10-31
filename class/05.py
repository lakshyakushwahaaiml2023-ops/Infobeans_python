'''3. Write a Java program to create a class called "Rectangle" with width and height attributes.
 Calculate the area and perimeter of the rectangle.
'''

class Rectangle:
    def __init__(self, l, b):
        self.__length = l
        self.__breadth = b

    def calc_area(self):
        print(f"Area of Rectangle: {self.__breadth * self.__length} sq m")

    def calc_peri(self):
        print(f"Perimeter of Rectangle: {2 * (self.__breadth + self.__length)} m")

    def view_details(self):
        print(f"Length of Rectangle: {self.__length} m")
        print(f"Breadth of Rectangle: {self.__breadth} m")
        self.calc_peri()
        self.calc_area()

r1 = Rectangle(10, 15)

r1.view_details()