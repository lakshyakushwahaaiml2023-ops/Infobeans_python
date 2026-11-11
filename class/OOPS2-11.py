'''11. E-Commerce Product System
Problem

Create product system for online store.

Requirements

Each product should have:

product name
price
category
Functionalities
Apply GST using static method
Apply category discount
Display final price
Concepts Practiced
static methods
calculations
reusable logic'''

class Product:
  
  __gst = 18
  
  def __init__(self, pname, price, cat):
    self.__pname = pname
    self.__price = price
    self.__cat = cat
    self.__after_cat_disc = Product.cat_disc(self.__price, self.__cat)
    self.__after_gst_price = Product.add_gst(self.__after_cat_disc, Product.__gst)
    

  @staticmethod
  def add_gst(price, gst):
    price += price * gst / 100
    return price

  @staticmethod
  def cat_disc(price, cat):
    if cat in {"Fashion", "Apparel"}:
      return price * 0.7
    elif cat in {"Home", "Kitchen", "Furniture"}:
      return price * 0.65
    elif cat in {"Books", "Media", "Toys", "Electronics", "Gadgets"}:
      return price * 0.85
    elif cat in {"Beauty", "Personal Care"}:
      return price * 0.8
    else:
      return price

  def __str__(self):
    return f"{self.__pname} | {self.__cat}\nOriginal price: {self.__price} Rs | After Category Discount: {self.__after_cat_disc:.2f} Rs\nAfter GST: {self.__after_gst_price:.2f} Rs\n"

p1 = Product("Men's Levi Bootcut Jeans", 2379, "Fashion")
print(p1)
p2 = Product("HP Pavillion 15", 67690, "Electronics")
print(p2)
