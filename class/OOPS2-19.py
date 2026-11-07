'''19. Flight Reservation System
Problem

Create airline reservation software.

Requirements

Flight should contain:

flight number
total seats
booked seats
Functionalities
Book ticket
Cancel ticket
Prevent overbooking'''

class Seat:
    def __init__(self, sno):
        self.__seat_number = sno
        self.__status = "Available"
        
    def __str__(self):
        return f"Seat: {self.__seat_number} --> {self.__status}"

    def book_seat(self):
        self.__status = "Booked"
        print("Seat booked succesfully!!")

    def cancel_seat(self):
        self.__status = "Available"
        print("Booking cancelled!!")

    def get_status(self):
        return self.__status == "Booked"

class Flight:
    __seat_no = 1
    
    def __init__(self, fno, ts):
        self.__fno = fno
        self.__total_seats = ts
        self.__booked_seats = 0
        self.__seats = {}
        for i in range(1, ts + 1):
          self.__seats[i] = Seat(i)
        self.__cancelled_seats = []

    def booking(self, count):
        if count <=  (self.__total_seats - self.__booked_seats):
            for i in self.__cancelled_seats:
                self.__seats[i].book_seat()
                self.__booked_seats += 1
                count -= 1
                self.__cancelled_seats.remove(i)
            for i in range(count):
                self.__seats[Flight.__seat_no].book_seat()
                Flight.__seat_no += 1
            self.__booked_seats += count
        else:
            print("There are not enough seats available!!!")
    
    def cancelling(self, sno):
        if self.__seats[sno].get_status():
            self.__seats[sno].cancel_seat()
            self.__cancelled_seats.append(sno)
            self.__booked_seats -= 1
        else:
            print("This seat is not booked!!")
            
    def view_seats(self):
        for seat in self.__seats.values():
            print(seat)

    def view_status(self):
        print(f"Available seats: {self.__total_seats - self.__booked_seats}")

f1 = Flight(101, 20)
f1.booking(5)
f1.cancelling(3)
f1.cancelling(4)
f1.booking(2)
f1.view_seats()
f1.view_status()
