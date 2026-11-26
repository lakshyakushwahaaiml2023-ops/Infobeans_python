'''
78. Transport Ticket Pricing
Problem Statement

Transport fares differ.

Create:

Bus
Train
Flight'''

from abc import abstractmethod

class Transport:
    @abstractmethod
    def calculate_fare(self):
        pass

class Bus(Transport):
    def calculate_fare(self):
        print("Bus Fare = 500")

class Train(Transport):
    def calculate_fare(self):
        print("Train Fare = 1000")

class Flight(Transport):
    def calculate_fare(self):
        print("Flight Fare = 5000")

trans = [Bus(), Train(), Flight()]
for t in trans:
    t.calculate_fare()