'''69. Courier Service Pricing
Problem Statement

Pricing depends on package type.

Create:

abstract class Courier

Child:

NormalCourier
ExpressCourier
SameDayCourier'''

from abc import ABC, abstractmethod

class Courier(ABC):
    @abstractmethod
    def get_price(self):
        pass

class NormalCourier(Courier):
    def get_price(self):
        return "Normal Courier --> Price: 50Rs"

class ExpressCourier(Courier):
    def get_price(self):
        return "Express Courier --> Price: 100Rs"

class SameDayCourier(Courier):
    def get_price(self):
        return "Same Day Courier --> Price: 200Rs"

couriers = [NormalCourier(), ExpressCourier(), SameDayCourier()]
for courier in couriers:
    print(courier.get_price())  