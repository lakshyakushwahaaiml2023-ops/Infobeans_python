'''7. Food Delivery System

Classes: Restaurant, Menu, Customer, Order, DeliveryPartner, Payment
- Place and track orders.
- Assign delivery partners.
- Manage order states.
- Calculate delivery charges.'''

class FDS:
    def __init__(self):
        self.__menu = {}
        self.__restraunts = {}
        self.__orders = {}
        self.__customers = {}

class Restraunt:
    def __init__(self, name, loc):
        self.__name = name
        self.__location = loc
        self.__items = {}

class Dish:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

class Order:
    def __init__(self, id, user):
        self.__orderId = id
        self.__user = user

    