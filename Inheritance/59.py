'''9. Food Billing System
Problem Statement

Restaurants apply different GST percentages.

Create:

abstract class FoodItem

Child:

VegFood
NonVegFood
Beverage

Rules:

Veg → 5%
NonVeg → 12%
Beverage → 18%'''

from abc import ABC, abstractmethod

class FoodItem(ABC):
    @abstractmethod
    def gst(self, price):
        pass

class Veg(FoodItem):
    def gst(self, price):
        return price * 0.05

    def get_cat(self):
        return "Veg"

class NonVeg(FoodItem):
    def gst(self, price):
        return price * 0.12

    def get_cat(self):
        return "Non-Veg"

class Bevarage(FoodItem):
    def gst(self, price):
        return price * 0.18
    
    def get_cat(self):
        return "Beverage"

food = [Veg(),
        NonVeg(),
        Bevarage()
        ]
price = 120

for item in food:
    print(f"{item.get_cat()} --> Price: {price} --> GST: {item.gst(price): .2f}")
