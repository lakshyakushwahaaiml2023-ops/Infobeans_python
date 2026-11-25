'''41. Cab Booking Application

Features:

User booking
Driver assignment
Fare calculation

Use:

inheritance
abstraction
polymorphism'''

class CBA:

    __price_per_km = 5.0

    def __init__(self):
        self.__drivers = {}
        self.__users = {}
        self.__bookings = {}

    def add_driver(self, name, age, l_id, c_num):
        if l_id in self.__drivers:
            print("Driver already exists...")
        else:
            self.__drivers[l_id] = Driver(name, age, l_id, c_num)
            print("Driver added succesfully...")            

    def add_user(self, name, uid):
        if uid in self.__users:
            print("User with this UID already exists...")
        else:
            self.__users[uid] = User(name, uid)
            print("User added succesfully...")

    def book_car(self, uid, dist):
        if uid not in self.__users:
            print("User ID not in database...")
        elif uid in self.__bookings:
            print("User already has an active booking...")
        else:
            l_id = None
            for driver in self.__drivers.values():
                if driver.getStatus() == "Available":
                    l_id = driver.get_lid()
                    driver.change_status()
                    break
            else:
                print("All drivers are booked...")
                return

            print("booking Successful...")
            b = Booking(uid, l_id, dist)
            self.__bookings[uid] = b
            print(f"Total Fare for {dist} km: ", b.get_fare(), " Rs")

    def return_car(self, uid):
        if uid not in self.__users:
            print("User ID not in database...")
        else:
            if uid not in self.__bookings:
                print("This user has not booked a car...")
            else:
                b = self.__bookings[uid]
                driver = self.__drivers[b.get_lid()]
                driver.change_status()
                self.__bookings.pop(uid)
                print("Trip completed...")
            

    def view_users(self):
        print("="*40)
        print("Users-->")
        for user in self.__users.values():
            print(user)
        print("="*80)

    def view_drivers(self):
        print("="*40)
        print("Drivers-->")
        for driver in self.__drivers.values():
            print(driver)
        print("="*80)

    @classmethod
    def get_price(cls):
        return cls.__price_per_km


class Driver:
    def __init__(self, name, age, l_id, c_num):
        self.__name = name
        self.__age = age
        self.__l_id = l_id
        self.__c_num = c_num
        self.__status = "Available"

    def getStatus(Self):
        return Self.__status

    def change_status(self):
        if self.__status == "Available":
            self.__status = "Booked"
        else:
            self.__status = "Available"
    def get_lid(self):
        return self.__l_id

    def __str__(self):
        return f"{self.__name} | Age: {self.__age} | License ID: {self.__l_id} | Car number: {self.__c_num} | {self.__status}"

class Booking:
    def __init__(self, user, lid, dist):
        self.__user = user
        self.__lid = lid
        self.__dist = dist
        self.__ppk = CBA.get_price()
        self.__fare = Booking.calc_fare(dist, self.__ppk)

    @staticmethod
    def calc_fare(dist, price):
        return dist * price

    def get_fare(self):
        return self.__fare

    def get_lid(self):
        return self.__lid

class User:
    def __init__(self, name, u_id):
        self.__name = name
        self.__uid = u_id

    def __str__(self):
        return f"{self.__name} | User ID: {self.__uid}"
    
c = CBA()
c.add_user("Lakshya", 1001)
c.add_user("Diksha", 1002)

c.add_driver("Prabhat", 20, "l1001", "MP1001")
c.add_driver("Smruti", 22, "l1002", "MP1002")
c.add_driver("Darpan", 22, "l1003", "MP1003")
c.add_driver("Ishant", 21, "l1004", "MP1004")

c.book_car(1001, 25)
c.return_car(1001)

c.view_drivers()
c.view_users()           