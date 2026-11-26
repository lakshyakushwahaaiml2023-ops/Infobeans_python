'''20. Ticket Booking System
Problem Statement

Ticket prices differ by seat category.

Create:

abstract class Ticket

Child:

SilverTicket
GoldTicket
PlatinumTicket'''

from abc import ABC, abstractmethod

class Ticket(ABC):

    @abstractmethod
    def __str__(self):
        return f"{self.__name} --> {self.__price}"


class GoldTicket(Ticket):
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        
    def __str__(self):
        return f"{self.__name} --> {self.__price}"

class PlatinumTicket(Ticket):
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"{self.__name} --> {self.__price}"

class VIPTicket(Ticket):
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"{self.__name} --> {self.__price}"

class Booking:

    def __init__(self):
        self.__seat = None

    def bookSeat(self, seat):
        if seat == "Gold":
            self.__seat = GoldTicket("Gold", 199)
        if seat == "Platinum":
            self.__seat = PlatinumTicket("Platinum", 299)
        if seat == "VIP":
            self.__seat = VIPTicket("VIP", 499)

    def viewSeat(self):
        print(self.__seat)

b = Booking()
b.bookSeat("Gold")
b.viewSeat()
b.bookSeat("Platinum")
b.viewSeat()
b.bookSeat("VIP")
b.viewSeat()
