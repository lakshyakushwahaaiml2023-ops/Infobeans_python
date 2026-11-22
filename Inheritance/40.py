'''40. AI Chatbot System

Methods:

reply()

Implement:

SupportBot
SalesBot'''

from abc import ABC, abstractmethod

class AI(ABC):
  @abstractmethod
  def reply():
    pass

class SupportBot(AI):
  def reply(self):
    print("Hello... support bot here...")

class SalesBot(AI):
  def reply(self):
    print("Hello... sales bot here...")

s = SupportBot()
s.reply()
print()
s = SalesBot()
s.reply()
