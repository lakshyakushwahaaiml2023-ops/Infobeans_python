'''29. Insurance Premium Calculator
Problem Statement

Insurance premium varies.

Create:

HealthInsurance
CarInsurance
LifeInsurance

instead of only large architectures.'''

from abc import ABC, abstractmethod

class Insurfance:
    @abstractmethod
    def calculate_premium(self):
        pass

class HealthInsurance(Insurfance):
    def calculate_premium(self):
        print("Health Insurance Premium = 5000")

class CarInsurance(Insurfance):
    def calculate_premium(self):
        print("Car Insurance Premium = 10000")

class LifeInsurance(Insurfance):
    def calculate_premium(self):
        print("Life Insurance Premium = 15000")

ins = [HealthInsurance(), CarInsurance(), LifeInsurance()]
for i in ins:
    i.calculate_premium()