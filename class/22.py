"""19. Write a Java program to create a class with methods to search for flights and hotels, and to book and cancel reservations."""


class Hotel:
    def __init__(self, name, stars, place, total_rooms, aval_rooms, price):
        self.__name = name
        self.__stars = stars
        self.__place = place
        self.__total_rooms = total_rooms
        self.__aval_rooms = aval_rooms
        self.__price = price

    def view_hotel(self):
        print("=" * 40)
        print(f"Hotel Name: {self.__name}")
        print(f"Hotel Rating: {self.__stars} Stars")
        print(f"Hotel Location: {self.__place}")
        print(f"Total Rooms: {self.__total_rooms}")
        print(f"Available Rooms: {self.__aval_rooms}")
        print(f"Price Per Night: {self.__price} Rs")
        print("=" * 40)

    def get_details(self):
        return self.__name, self.__place, self.__price, self.__aval_rooms

    def book_room(self, rooms):
        if rooms > 0 and self.__aval_rooms >= rooms:
            self.__aval_rooms -= rooms
            return True
        return False

    def cancel_room(self, rooms):
        self.__aval_rooms = min(
            self.__total_rooms,
            self.__aval_rooms + rooms
        )


class Flight:
    def __init__(self, plane_no, airline_name, src, dest,
                 dep_time, arrival_time, ticket_price, seats=100):

        self.__plane_no = plane_no
        self.__airline_name = airline_name
        self.__src = src
        self.__dest = dest
        self.__dep_time = dep_time
        self.__arrival_time = arrival_time
        self.__ticket_price = ticket_price
        self.__total_seats = seats
        self.__seats = seats

    def view_flight(self):
        print("====== Flight Details ======")
        print("Plane Number:", self.__plane_no)
        print("Airline Name:", self.__airline_name)
        print("Source:", self.__src)
        print("Destination:", self.__dest)
        print("Departure Time:", self.__dep_time)
        print("Arrival Time:", self.__arrival_time)
        print("Ticket Price: Rs", self.__ticket_price)
        print("Available Seats:", self.__seats)
        print("=" * 40)

    def get_details(self):
        return (self.__plane_no, self.__src, self.__dest,
                self.__ticket_price, self.__seats)

    def get_route(self, src, dest):
        return (self.__src.lower() == src.lower()
                and self.__dest.lower() == dest.lower())

    def book_seat(self, seats):
        if seats > 0 and self.__seats >= seats:
            self.__seats -= seats
            return True
        return False

    def cancel_seat(self, seats):
        self.__seats = min(
            self.__total_seats,
            self.__seats + seats
        )


class User:
    def __init__(self, user_id, name, email, phone, password):
        self.__user_id = user_id
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__password = password

    def verify_password(self, password):
        return self.__password == password

    def view_details(self):
        print("=" * 40)
        print(f"User ID: {self.__user_id}")
        print(f"User Name: {self.__name}")
        print(f"E-mail: {self.__email}")
        print(f"Phone Number: {self.__phone}")
        print("=" * 40)


class App:
    user_count = 1000
    booking_count = 5000

    def __init__(self):
        print("========= Welcome to the Booking App =========")

        self.__users = {}
        self.__flights = {}
        self.__hotels = {}

        self.__flight_bookings = {}
        self.__hotel_bookings = {}


    def add_user(self, name, email, phone, password):
        if email in self.__users:
            print("User already exists!")
            return

        user_id = App.user_count
        App.user_count += 1

        user = User(user_id, name, email, phone, password)
        self.__users[email] = user

        print("User added successfully!")

    def verify_user(self, email, password):
        return (
            email in self.__users
            and self.__users[email].verify_password(password)
        )

    def view_user(self, email, password):
        if self.verify_user(email, password):
            self.__users[email].view_details()
        else:
            print("Wrong Details!")


    def add_flight(self, no, airlines, src, dest,
                   dep_time, arr_time, price, seats=100):

        if no in self.__flights:
            print("Flight already exists!")
            return

        f = Flight(no, airlines, src, dest,
                   dep_time, arr_time, price, seats)

        self.__flights[no] = f
        print("Flight Added Successfully!")

    def view_flight(self, no):
        if no in self.__flights:
            self.__flights[no].view_flight()
        else:
            print("Flight Not Found!")

    def search_flight(self, src, dest):
        found = False

        print("\n====== Available Flights ======")

        for flight in self.__flights.values():
            if flight.get_route(src, dest):
                flight.view_flight()
                found = True

        if not found:
            print("No flights available for this route!")


    def add_hotel(self, name, stars, place,
                  total_rooms, aval_rooms, price):

        if name in self.__hotels:
            print("Hotel already exists!")
            return

        if not (0 <= aval_rooms <= total_rooms):
            print("Invalid room availability!")
            return

        h = Hotel(name, stars, place,
                  total_rooms, aval_rooms, price)

        self.__hotels[name] = h
        print("Hotel Added Successfully!")

    def view_hotel(self, name):
        if name in self.__hotels:
            self.__hotels[name].view_hotel()
        else:
            print("Hotel Not Found!")

    def search_hotel(self, place):
        found = False

        print("\n====== Available Hotels ======")

        for hotel in self.__hotels.values():
            details = hotel.get_details()

            if details[1].lower() == place.lower():
                hotel.view_hotel()
                found = True

        if not found:
            print("No hotels available at this location!")


    def book_flight(self, email, password, flight_no, seats=1):

        if not self.verify_user(email, password):
            print("Invalid User Credentials!")
            return

        if flight_no not in self.__flights:
            print("Flight Not Found!")
            return

        if seats <= 0:
            print("Invalid number of seats!")
            return

        flight = self.__flights[flight_no]

        details = flight.get_details()

        if not flight.book_seat(seats):
            print("Not Enough Seats Available!")
            return

        booking_id = App.booking_count
        App.booking_count += 1

        total_price = details[3] * seats

        self.__flight_bookings[booking_id] = {
            "email": email,
            "flight_no": flight_no,
            "seats": seats,
            "price": total_price,
            "status": "Booked"
        }

        print("\n====== Flight Booking Successful ======")
        print("Booking ID:", booking_id)
        print("User:", email)
        print("Flight Number:", flight_no)
        print("Seats Booked:", seats)
        print("Total Price: Rs", total_price)
        print("Status: Booked")
        print("=" * 40)


    def cancel_flight(self, email, password, booking_id):

        if not self.verify_user(email, password):
            print("Invalid User Credentials!")
            return

        if booking_id not in self.__flight_bookings:
            print("Invalid Booking ID!")
            return

        booking = self.__flight_bookings[booking_id]

        if booking["email"] != email:
            print("This booking does not belong to you!")
            return

        if booking["status"] == "Cancelled":
            print("Booking Already Cancelled!")
            return

        flight_no = booking["flight_no"]
        seats = booking["seats"]

        self.__flights[flight_no].cancel_seat(seats)

        booking["status"] = "Cancelled"

        print("\n====== Flight Cancellation Successful ======")
        print("Booking ID:", booking_id)
        print("Refund Amount: Rs", booking["price"])
        print("Status: Cancelled")
        print("=" * 40)


    def book_hotel(self, email, password, hotel_name,
                   rooms=1, nights=1):

        if not self.verify_user(email, password):
            print("Invalid User Credentials!")
            return

        if hotel_name not in self.__hotels:
            print("Hotel Not Found!")
            return

        if rooms <= 0 or nights <= 0:
            print("Invalid number of rooms or nights!")
            return

        hotel = self.__hotels[hotel_name]
        details = hotel.get_details()

        if not hotel.book_room(rooms):
            print("Not Enough Rooms Available!")
            return

        booking_id = App.booking_count
        App.booking_count += 1

        total_price = details[2] * rooms * nights

        self.__hotel_bookings[booking_id] = {
            "email": email,
            "hotel_name": hotel_name,
            "rooms": rooms,
            "nights": nights,
            "price": total_price,
            "status": "Booked"
        }

        print("\n====== Hotel Booking Successful ======")
        print("Booking ID:", booking_id)
        print("Hotel Name:", hotel_name)
        print("Rooms Booked:", rooms)
        print("Nights:", nights)
        print("Total Price: Rs", total_price)
        print("Status: Booked")
        print("=" * 40)


    def cancel_hotel(self, email, password, booking_id):

        if not self.verify_user(email, password):
            print("Invalid User Credentials!")
            return

        if booking_id not in self.__hotel_bookings:
            print("Invalid Booking ID!")
            return

        booking = self.__hotel_bookings[booking_id]

        if booking["email"] != email:
            print("This booking does not belong to you!")
            return

        if booking["status"] == "Cancelled":
            print("Booking Already Cancelled!")
            return

        hotel_name = booking["hotel_name"]
        rooms = booking["rooms"]

        self.__hotels[hotel_name].cancel_room(rooms)

        booking["status"] = "Cancelled"

        print("\n====== Hotel Cancellation Successful ======")
        print("Booking ID:", booking_id)
        print("Refund Amount: Rs", booking["price"])
        print("Status: Cancelled")
        print("=" * 40)


    def view_bookings(self, email, password):

        if not self.verify_user(email, password):
            print("Invalid User Credentials!")
            return

        found = False

        print("\n====== YOUR BOOKING HISTORY ======")

        for booking_id, booking in self.__flight_bookings.items():
            if booking["email"] == email:
                print(
                    f"Flight Booking ID: {booking_id} | "
                    f"Flight: {booking['flight_no']} | "
                    f"Seats: {booking['seats']} | "
                    f"Price: Rs {booking['price']} | "
                    f"Status: {booking['status']}"
                )
                found = True

        for booking_id, booking in self.__hotel_bookings.items():
            if booking["email"] == email:
                print(
                    f"Hotel Booking ID: {booking_id} | "
                    f"Hotel: {booking['hotel_name']} | "
                    f"Rooms: {booking['rooms']} | "
                    f"Price: Rs {booking['price']} | "
                    f"Status: {booking['status']}"
                )
                found = True

        if not found:
            print("No bookings found!")

        print("=" * 40)



a1 = App()

a1.add_user("Lakshya", "kushwahalakshya@gmail.com",
            "6268347442", "1234")

a1.add_user("Diksha", "diksha123@gmail.com",
            "8109927290", "1234")

a1.add_user("Ishant", "ishant@gmail.com",
            "9666966845", "1234")


a1.add_flight(101, "IndiGo", "Delhi", "Mumbai",
              "06:00 AM", "08:15 AM", 4500, 100)

a1.add_flight(102, "Air India", "Mumbai", "Bangalore",
              "09:30 AM", "11:15 AM", 5200, 80)

a1.add_flight(103, "Vistara", "Delhi", "Kolkata",
              "12:00 PM", "02:10 PM", 6000, 90)

a1.add_flight(104, "SpiceJet", "Bangalore", "Hyderabad",
              "03:00 PM", "04:20 PM", 3200, 70)

a1.add_flight(105, "IndiGo", "Raipur", "Delhi",
              "07:00 PM", "09:00 PM", 4800, 60)

a1.add_flight(106, "Air India", "Kolkata", "Mumbai",
              "10:30 PM", "01:15 AM", 6500, 50)


a1.add_hotel("Tiruvantham", 5, "Kerala", 500, 250, 1200)
a1.add_hotel("Taj Palace", 5, "Delhi", 300, 100, 5000)
a1.add_hotel("Hotel Blue", 4, "Mumbai", 200, 80, 2500)
a1.add_hotel("Royal Stay", 3, "Raipur", 100, 50, 1500)



email = "kushwahalakshya@gmail.com"
password = "1234"

a1.view_user(email, password)

a1.search_flight("Delhi", "Mumbai")

a1.search_hotel("Delhi")

a1.book_flight(email, password, 101, 2)

a1.book_hotel(email, password, "Taj Palace", 2, 3)

a1.view_bookings(email, password)

a1.cancel_flight(email, password, 5000)

a1.cancel_hotel(email, password, 5001)

a1.view_bookings(email, password)

a1.view_flight(101)
a1.view_hotel("Taj Palace")