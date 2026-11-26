'''7. Cab Fare Calculator
Problem Statement

Cab fares differ based on ride type.

Create:

abstract class Ride

Child:

MiniRide
SedanRide
SUVRide

Rules:

Mini → ₹10/km
Sedan → ₹15/km
SUV → ₹20/km'''

from abc import ABC, abstractmethod

class Ride(ABC):
    @abstractmethod
    def fare_calc():
        pass

class MiniRIde(Ride):
    __fare = 10

    def fare_calc(self, dist):
        return MiniRIde.__fare * dist

class Sedan(Ride):
    __fare = 15

    def fare_calc(self, dist):
        return Sedan.__fare * dist

class SUV(Ride):
    __fare = 20

    def fare_calc(self, dist):
        return SUV.__fare * dist

m = MiniRIde()
print("Total Fare: ", m.fare_calc(12), " Rs.")
print()
m = Sedan()
print("Total Fare: ", m.fare_calc(12), " Rs.")
print()
m = SUV()
print("Total Fare: ", m.fare_calc(12), " Rs.")