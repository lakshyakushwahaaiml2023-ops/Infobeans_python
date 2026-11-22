'''36. Payment Interface

Methods:

pay()

Implement:

PayPal
Stripe
Razorpay'''

from abc import ABC, abstractmethod

class Payment(ABC):
  @abstractmethod
  def pay():
    pass

class PayPal(Payment):
  def pay(self):
    print("Payment done via PayPal...")

class Stripe(Payment):
  def pay(self):
    print("Payment done via Stripe...")

class RazorPay(Payment):
  def pay(self):
    print("Payment done via RazorPay...")
r = RazorPay()
r.pay()
