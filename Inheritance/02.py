'''2. Vehicle System

Create parent class Vehicle.

Child classes:

Car
Bike
Bus

Add methods:

start()
stop()'''

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car starts...")

    def stop(self):
        print("Car Stops...")

class Bike(Vehicle):

    def start(self):
        print("Bike starts...")

    def stop(self):
        print("Bike Stops...")

class Bus(Vehicle):

    def start(self):
        print("Bus starts...")

    def stop(self):
        print("Bus Stops...")

c = Car()
c.start()
c.stop()
