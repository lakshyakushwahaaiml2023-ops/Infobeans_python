'''3. Online Shopping Cart
Problem

Create a shopping cart system.

Requirements

A cart should:

store customer name
maintain list of products
maintain total bill
Functionalities
Add product
Remove product
Calculate final amount
Apply discount using static method
Track total carts created
Concepts Practiced
list inside object
object interaction
static method
class variable'''

class Product:
  def __init__(self, name, price, qnty):
    self.__name = name
    self.__price = price
    self.__qnty = qnty

  def get_price(self):
    return self.__price * self.__qnty

  def __str__(self):
    return f"{self.__name} | {self.__price} Rs | X{self.__qnty} --> Total: {self.__price * self.__qnty} Rs"

  def add_quantity(self, qnty):
    self.__qnty += qnty
    
class Cart:
  __count = 0
  def __init__(self, cname):
    Cart.__count += 1
    self.__name = cname
    self.__products = {}

  @classmethod
  def total_carts(cls):
    print(f"Total carts formed: {cls.__count}")

  def add_product(self, pname, price, qnty):
    if pname in self.__products:
      self.__products[pname].add_quantity(qnty)
    else:
      self.__products[pname] = Product(pname, price, qnty)

  def remove_product(self, pname):
    if pname in self.__products:
      self.__products.pop(pname)
      print(f"{pname} removed from cart!!")
    else:
      print(f"No product found of given name: {pname}!!!")

  def calc_bill(self):
    sump = 0
    print(f"\nCustomer Name: {self.__name}")
    for item in self.__products.values():
      print(item)
      sump += item.get_price()

    print(f"Total Amount: {sump} Rs")
    print(f"After Discount: {Cart.calc_disc(sump)} Rs\n")

  @staticmethod
  def calc_disc(bill):
    if bill >= 5000:
      bill = bill * 0.7
    elif bill >= 3000:
      bill = bill * 0.8
    elif bill >= 1500:
      bill = bill * 0.9
      
    return bill

c1 = Cart("Lakshya Kushwaha")
c1.add_product("Toothpaste", 120, 2)
c1.add_product("Lux Soap", 70, 10)
c1.add_product("Markers", 25, 3)
c1.add_product("Rosemary Oil", 210, 1)
c1.add_product("Pentonic Blue Pen", 10, 20)
c1.add_product("Ghee 1Kg", 890, 1)
c1.add_product("Markers", 25, 3)
c1.calc_bill()
Cart.total_carts()
