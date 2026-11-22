'''33. Smart Home Devices

Methods:

turn_on()
turn_off()

Implement:

SmartFan
SmartLight
SmartAC'''

from abc import ABC, abstractmethod

class SmartDevice:
  @abstractmethod
  def turn_on():
    pass

  @abstractmethod
  def turn_off():
    pass

class SmartFan(SmartDevice):
  def turn_on(self):
    print("Fan turned on...")

  def turn_off(self):
    print("Fan turned off...")

class SmartLight(SmartDevice):
  def turn_on(self):
    print("Light turned on...")

  def turn_off(self):
    print("Light turned off...")

class SmartAC(SmartDevice):
  def turn_on(self):
    print("AC turned on...")

  def turn_off(self):
    print("AC turned off...")

fan = SmartFan()
fan.turn_on()

light = SmartLight()
light.turn_on()

ac = SmartAC()
ac.turn_on()
    
