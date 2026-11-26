'''74. Ride Sharing App Surge Pricing
Problem Statement

Surge pricing differs.

Create:

abstract class RidePricing

Child:

NormalTime
PeakTime
RainTime'''

from abc import ABC, abstractmethod

class RidePricing(ABC):
    @abstractmethod
    def fare_calc(self, base_price):
        pass

class NormalTime(RidePricing):

    def __init__(self, base_price):
        self.__base_price = base_price
    @property
    def fare_calc(self):
        return f"{self.__base_price * 1} Rs"

class PeakTime(RidePricing):

    def __init__(self, base_price):
        self.__base_price = base_price

    @property
    def fare_calc(self):
        return f"{self.__base_price * 1.5} Rs"

class RainTime(RidePricing):

    def __init__(self, base_price):
        self.__base_price = base_price

    @property
    def fare_calc(self):
        return f"{self.__base_price * 2.0} Rs"

times = [NormalTime(1200), PeakTime(1200), RainTime(1200)]
for i in times:
    print(i.fare_calc)