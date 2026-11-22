'''31. Drawable Interface

Interface:

draw()

Implement:

Circle
Rectangle
Line'''

from abc import ABC, abstractmethod

class Shape:
  
  @abstractmethod
  def draw(self):
    pass

class Circle(Shape):
  def draw(self, radius):
    print("Circle: ")
    
    for i in range(-radius, radius + 1):
      for j in range(-radius, radius + 1):
        if abs(i*i + j*j - radius*radius) <= radius:
          print("*", end=" ")
        else:
          print(" ", end=" ")

      print()
class Rectangle(Shape):
  def draw(self, l, b):
    print("Rectangle: ")
    for i in range(l):
      for j in range(b):
        if j == 0 or j == b-1:
          print("|", end = "")
        elif i ==0 or i == l-1:
          print("-", end = "")
        else:
          print(" ", end="")
      print()

class Line(Shape):
  def draw(self, length):
    print("Line: ", end = " ")
    print("-" * length)

l = Line()
l.draw(8)
print()
r = Rectangle()
r.draw(10, 9)
print()
c = Circle()
c.draw(5)
