'''10. Movie Ticket Booking

Parent:

Ticket

Derived:

GoldTicket
PlatinumTicket
VIPTicket

Apply pricing logic.'''

class Ticket:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"{self.__name} --> {self.__price}"

    def get_price(self):
        return self.__price

class GoldTicket(Ticket):
    def __init__(self):
        super().__init__("Gold", 199)

class PlatinumTicket(Ticket):
    def __init__(self):
        super().__init__("Platinum", 299)

class VIPTicket(Ticket):
    def __init__(self):
        super().__init__("VIP", 599)

class Booking:

    def __init__(self):
        self.__seat = None

    def bookSeat(self, seat):
        if seat == "Gold":
            self.__seat = GoldTicket()
        if seat == "Platinum":
            self.__seat = PlatinumTicket()

        if seat == "VIP":
            self.__seat = VIPTicket()

    def viewSeat(self):
        print(self.__seat)

b = Booking()
b.bookSeat("Gold")
b.viewSeat()
b.bookSeat("Platinum")
b.viewSeat()
b.bookSeat("VIP")
b.viewSeat()
