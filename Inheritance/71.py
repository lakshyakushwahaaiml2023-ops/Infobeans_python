'''71. Online Subscription Plans
Problem Statement

Streaming app has multiple subscription plans.

Create:

abstract class Subscription

Child:

BasicPlan
StandardPlan
PremiumPlan

Each has different:

price
screen limits'''

from abc import ABC, abstractmethod

class Subscription(ABC):
    @abstractmethod
    def limits(self):
        pass

class BasicPlan(Subscription):
    def limits(self):
        return f"Price: 199Rs | Screen Limits: 2 devices"

class StandardPlan(Subscription):
    def limits(self):
        return f"Price: 449Rs | Screen Limits: 4 devices"

class PremiumPlan(Subscription):
    def limits(self):
        return f"Price: 999Rs | Screen Limits: 6 devices"

devs = [BasicPlan(), StandardPlan(), PremiumPlan()]
for plan in devs:
    print(plan.limits())