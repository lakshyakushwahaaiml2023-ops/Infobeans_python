'''35. Messaging Application

Methods:

send_message()

Implement:

WhatsApp
Telegram
Signal'''

from abc import ABC, abstractmethod

class Message(ABC):
  @abstractmethod
  def send_message():
    pass

class Whatsapp(Message):
  def send_message(self):
    print("Message sent via Whatsapp...")

class Telegram(Message):
  def send_message(self):
    print("Message sent via Telegram...")

class SMS(Message):
  def send_message(self):
    print("Message sent via SMS...")

w = Whatsapp()
w.send_message()
