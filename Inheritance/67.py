'''67. Smart Appliance Controller
Problem Statement

Different appliances behave differently.

Create:

abstract class Appliance

Child:

Fan
AC
WashingMachine
'''

from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def get_power_consumption(self):
        pass

class Fan(Appliance):
    def get_power_consumption(self):
        return "Fan --> Power Consumption: 75W"
    
class AC(Appliance):
    def get_power_consumption(self):
        return "AC --> Power Consumption: 1500W"

class WashingMachine(Appliance):
    def get_power_consumption(self):
        return "Washing Machine --> Power Consumption: 500W"

apps = [Fan(), AC(), WashingMachine()]
for app in apps:
    print(app.get_power_consumption())