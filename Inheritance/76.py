'''76. Water Bill Calculator
Problem Statement

Water charges vary by usage type.

Create:

Residential
Commercial
Agricultural
'''

from abc import ABC, abstractmethod

class WaterBill:
    @abstractmethod
    def calculate_bill(self):
        pass

class Residential(WaterBill):
    def calculate_bill(self):
        print("Residential Water Bill = 1000 per 1000 liters")

class Commercial(WaterBill):
    def calculate_bill(self):
        print("Commercial Water Bill = 5000 per 1000 liters")

class Agricultural(WaterBill):
    def calculate_bill(self):
        print("Agricultural Water Bill = 2000 per 1000 liters")

water_bills = [Residential(), Commercial(), Agricultural()]
for bill in water_bills:
    bill.calculate_bill()