'''54. Vehicle Parking Fee System
Problem Statement

Parking fees vary by vehicle type.

Create:

abstract class Vehicle

Child classes:

Bike
Car
Bus

Rules:

Bike → ₹10/hour
Car → ₹30/hour
Bus → ₹50/hour'''

from abc import ABC, abstractmethod

class Vehicle(ABC): 
    @abstractmethod
    def parking_fee():
        pass

class Bike(Vehicle):
    def parking_fee(self, hours):
        print("Total Parking Fee: ", 10 * hours, " Rs.")

class Car(Vehicle):
    def parking_fee(self, hours):
        print("Total Parking Fee: ", 30 * hours, " Rs.")

class Bus(Vehicle):
    def parking_fee(self, hours):
        print("Total Parking Fee: ", 50 * hours, " Rs.")

class Parking:
    def calc_fee(self, type,  hrs):
        if type == "Bike":
            b = Bike()
            b.parking_fee(hrs)
        elif type == "Car":
            c = Car()
            c.parking_fee(hrs)
        else:
            b = Bus()
            b.parking_fee(hrs)
p = Parking()
p.calc_fee("Car", 12)

