'''4. Write a Java program to create a class called "Circle" with a radius attribute. 
You can access and modify this attribute. Calculate the area and circumference of the circle.
'''

class Circle:
    def __init__(self, r):
        self.__radius = r

    def set_radius(self, r):
        self.__radius = r

    def get_radius(self):
        print(f"Radius of Circle: {self.__radius}")

    def get_circumfrence(self):
        print(f"Circumfrence: {2 * 3.17 *self.__radius} m")

    def get_area(self):
        print(f"Area of Circle: {3.14 * self.__radius * self.__radius} sq m")

c1 = Circle(12)
c1.get_radius()
c1.get_circumfrence()
c1.get_area()
print()
c1.set_radius(5)
c1.get_radius()
c1.get_circumfrence()
c1.get_area()