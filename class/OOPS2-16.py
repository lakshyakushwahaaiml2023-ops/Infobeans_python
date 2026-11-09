'''16. Train Reservation System
Problem

Design ticket reservation system.

Requirements

Train should contain:

train number
total seats
booked seats
Functionalities
Reserve seat
Cancel seat
Display available seats'''

class Seat:
  def __init__(self, sno):
    self.__seat_number = sno
    self.__status = "Available"
        
  def __str__(self):
    return f"Seat: {self.__seat_number} --> {self.__status}"

  def reserve_seat(self):
    self.__status = "Reserved"
    print("Seat reserved succesfully!!")

  def cancel_seat(self):
    self.__status = "Available"
    print("Reservation cancelled!!")

  def get_status(self):
    return self.__status == "Reserved"

class Train:
  __seat_no = 1
    
  def __init__(self, tno, ts):
    self.__tno = tno
    self.__total_seats = ts
    self.__reserved_seats = 0
    self.__seats = {}
    for i in range(1, ts + 1):
      self.__seats[i] = Seat(i)
    self.__cancelled_seats = []

  def booking(self, count):
    if count <=  (self.__total_seats - self.__reserved_seats):
        for i in self.__cancelled_seats:
            self.__seats[i].reserve_seat()
            self.__reserved_seats += 1
            count -= 1
            self.__cancelled_seats.remove(i)
        for i in range(count):
            self.__seats[Train.__seat_no].reserve_seat()
            Train.__seat_no += 1
        self.__reserved_seats += count
    else:
        print("There are not enough seats available!!!")
    
  def cancelling(self, sno):
    if self.__seats[sno].get_status():
        self.__seats[sno].cancel_seat()
        self.__cancelled_seats.append(sno)
        self.__reserved_seats -= 1
    else:
        print("This seat is not reserved!!")
            
  def view_seats(self):
    for seat in self.__seats.values():
        print(seat)

  def view_status(self):
    print(f"Available seats: {self.__total_seats - self.__reserved_seats}")

t1 = Train(101, 20)
t1.booking(5)
t1.cancelling(3)
t1.cancelling(4)
t1.booking(2)
t1.view_seats()
t1.view_status()
