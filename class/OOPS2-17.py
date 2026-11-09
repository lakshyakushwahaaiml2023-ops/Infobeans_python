'''17. Electricity Bill System
Problem

Generate electricity bill.

Requirements

Consumer should contain:

consumer id
units consumed
Functionalities
Calculate bill
Add surcharge using static method
Display bill summary'''

class Consumer:
  def __init__(self, c_id, c_name):
    self.__consumer_id = c_id
    self.__c_name = c_name
    self.__units = 0

  def add_units(self, units):
    self.__units += units

  def get_units(self):
    return self.__units

  def __str__(self):
    return f"{self.__consumer_id} : {self.__c_name} --> {self.__units} units"

class EBS:
  __cost_per_unit = 14
  __surcharge = 5
  
  def __init__(self):
    self.__consumers = {}

  def add_consumer(self, c_id, c_name):
      if c_id not in self.__consumers:
        self.__consumers[c_id] = Consumer(c_id, c_name)
        print("Consumer added!!!")
      else:
        print("Consumer already exists with given consumer ID!!!")

  def calculate_bill(self, c_id):
    if c_id not in self.__consumers:
      print("Consumer does not exists in data!!!")
      return None
    else:
      units = self.__consumers[c_id].get_units()
      bill = units * EBS.__cost_per_unit
      final = EBS.calculate_surcharge(bill, EBS.__surcharge)
      return f"{bill} + 5% Surcharge --> Final Amount: {final : .2f}"

  @staticmethod
  def calculate_surcharge(bill, sur):
    return bill + (bill * sur)/100

  def add_units(self, c_id, units):
    if c_id not in self.__consumers:
      print("Consumer does not exists in data!!!")
    else:
      self.__consumers[c_id].add_units(units)
      print("Units succesfully added in users usage!!!")

  def view_summary(self, c_id):
    if c_id not in self.__consumers:
      print("Consumer does not exists in data!!!")
    else:
      print(f"{self.__consumers[c_id]} --> {self.calculate_bill(c_id)}")

e = EBS()
e.add_consumer(1001, "Lakshya")
e.add_consumer(1002, "Diksha")
e.add_consumer(1003, "Krishna")
e.add_units(1001, 40)
e.add_units(1002, 70)
e.add_units(1003, 60)
e.add_units(1005, 40)
e.view_summary(1001)
e.view_summary(1002)
e.view_summary(1003)
e.view_summary(1006)
