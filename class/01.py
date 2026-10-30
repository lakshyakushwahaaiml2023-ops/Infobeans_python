class Time:
    def __init__(self, hr, min, sec):
        self.__hr = hr
        self.__min = min
        self.__sec = sec

    def add_time(self, t1, t2):
        hour = t1.__hr + t2.__hr
        mins = t1.__min + t2.__min
        secs = t1.__sec + t2.__sec

        if secs >= 60:
            mins += 1
            secs -= 60
        if mins >= 60:
            hour += 1
            mins -= 60

        t3.__hr = hour
        t3.__min = mins
        t3.__sec = secs

    def display(self):
        print(f"{self.__hr} : {self.__min} : {self.__sec}")

t1 = Time(2, 45, 30)

t2 = Time(4, 59, 12)

t3 = Time(0,0,0)

t3.add_time(t1, t2)

print("Time 1 : ",end = " ")
t1.display()
print("Time 2 : ",end = " ")
t2.display()
print("Added Time : ",end = " ")
t3.display()