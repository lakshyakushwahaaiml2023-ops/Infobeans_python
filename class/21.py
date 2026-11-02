'''18. Write a Java program to create a class called "Restaurant" with attributes for menu items, prices, and ratings, and methods to add and remove items, and to calculate average rating.'''

class Dish:
  def __init__(self, name, price):
    self.__name = name
    self.__price = price
    self.__rating = 2.5

  def view_dish(self):
    print(f"="*40)
    print(f"Dish Name: {self.__name}")
    print(f"Dish price: {self.__price} Rs")
    print(f"Rating: {self.__rating}")

  def set_rating(self, rating):
    self.__rating = rating
    print(f"Thanks for rating !!!")

  def get_rating(self):
    return self.__rating
    

class Restraunt:
  def __init__(self, name):
    print("*"*10, f"Welcome to {name}!!", "*"*10, "\n")
    self.__name = name
    self.__menu = {}

  def show_menu(self):
    print("\n", "-"*16, " Menu ", "-"*16)
    for value in self.__menu.values():
      value.view_dish()
    print("="*40)
      

  def add_dish(self, name, price):
    d = Dish(name, price)
    self.__menu[name] = d
    print(f"{name} Added to Menu!!")

  def remove_dish(self, name):
    if name not in self.__menu:
      print(f"{name} not available in menu!!")
    else:
      print(f"{name} removed from the menu!!")
      self.__menu.pop(name)

  def rate_dish(self, name, rating):
    if rating < 1 or rating > 5:
      print("Enter valid rating between (1 - 5)!!!")
    if name not in self.__menu:
      print(f"{name} not available in menu")
    else:
      self.__menu[name].set_rating(rating)

  def average_rating(self):
    if len(self.__menu) == 0:
      print("No dishes available to calculate average rating!!!")
      return
    sum = 0
    for dish in self.__menu.values():
      sum += dish.get_rating()
    print(f"Average Rating: {sum/ len(self.__menu) : .2f}")

r = Restraunt("Bhawrilal")
r.add_dish("Tandoori Chicken", 500)
r.add_dish("Kadhai Paneer", 250)
r.add_dish("Naan", 25)
r.add_dish("Salad", 100)
r.rate_dish("Naan", 3.5)
r.rate_dish("Tandoori Chicken", 5)
r.average_rating()
r.show_menu()
r.remove_dish("Naan")
r.show_menu()
r.average_rating()
<<<<<<< HEAD
  
=======
  
>>>>>>> ebba63c1d01b427f775976e66707b97feb2ba5ea
