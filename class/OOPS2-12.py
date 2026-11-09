'''
12. Car Rental System
Problem

Create a car rental platform.

Requirements

Each car:

car number
model
rental price per day
availability
Functionalities
Rent car
Return car
Calculate rent amount
Prevent renting unavailable cars
'''

class Date:
  def __init__(self, day = 1, month =1, year = 1):
    self.__day = day
    self.__month = month
    self.__year = year

  @classmethod
  def make_date(cls, date):
    day, month, year = date.split('-')
    return cls(int(day), int(month), int(year))

  def __sub__(self, other):
    yd = self.__year - other.__year
    md = self.__month - other.__month
    dd = self.__day - other.__day
    if yd != 0:
      dd += 365 * yd
    if md != 0:
      dd += 30 * md
    return dd

  def __str__(self):
    return f"{self.__day}-{self.__month}-{self.__year}"

class Car:
  def __init__(self, c_num, model, price):
    self.__c_num = c_num
    self.__model = model
    self.__price = price
    self.__availability = "Available"
    self.__hire_date = None
    self.__return_date = None

  def change_status(self):
    if self.__availability == "Booked":
      self.__availability = "Available"
    else:
      self.__availability = "Booked"

  def set_hire_date(self, date):
    self.__hire_date = Date.make_date(date)

  def set_return_date(self, date):
    self.__return_date = Date.make_date(date) 
    
  def get_status(self):
    return self.__availability

  def dates(self):
    return self.__hire_date, self.__return_date

  def __str__(self):
    return f"Car Num: {self.__c_num}, Model = {self.__model}, Price/day = {self.__price} ==> {self.__availability}"

  def get_price(self):
    return self.__price

class CRS:
  def __init__(self):
    self.__cars = {}

  def view_cars(self):
    for car in self.__cars.values():
      print(car)

  def add_car(self, c_num, model, price):
    self.__cars[c_num] = Car(c_num, model, price)
    print("Car added succesfully!!")

  def rent_car(self, c_num, date):
    if c_num not in self.__cars:
      print("There is no car with this number!!!")
    else:
      if self.__cars[c_num].get_status() == "Available":
        self.__cars[c_num].change_status()
        self.__cars[c_num].set_hire_date(date)
        print("Car hired succesfully!!!")

  def return_car(self, c_num, date):
    if c_num not in self.__cars:
      print("Car not found!")
      return

    if self.__cars[c_num].get_status() == "Available":
      print("This car is not currently rented!")
      return
    else:
      self.__cars[c_num].change_status()
      self.__cars[c_num].set_return_date(date)
      hire, ret = self.__cars[c_num].dates()
      dd = ret - hire
      price = self.__cars[c_num].get_price()
      rent = CRS.calculate_rent(dd, price)
      print(f"Car returned succesfully --> Total Bill = {rent} Rs")

  @staticmethod
  def calculate_rent(days, price):
    return days * price


c = CRS()
c.add_car(1001, "Civic", 2500)
c.add_car(1002, "City", 2000)
c.add_car(1003, "Verna", 2200)
c.rent_car(1002, "09-11-2026")
c.return_car(1002, "07-12-2026")
c.view_cars()
      
