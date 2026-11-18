'''13. Smart Device System
Device
SmartDevice(Device)
SmartTV(SmartDevice)

Add WiFi support.

'''

class Device:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"{self.__name}"

class SmartDevice(Device):
    def __init__(self, name, wifi):
        super().__init__(name)
        self.__wifi = wifi

    def get_wifi(self):
        return self.__wifi

    def __str__(self):
        return f"{self.get_name()} | WiFi: {self.__wifi}"

class SmartTV(SmartDevice):
    def __init__(self, name, wifi, screen_size):
        super().__init__(name, wifi)
        self.__screen_size = screen_size

    def get_screen_size(self):
        return self.__screen_size

    def __str__(self):
        return f"{self.get_name()} | WiFi: {self.get_wifi()} | Screen Size: {self.__screen_size}"

d = Device("Device")
print(d)

sd = SmartDevice("Smart Device", True)
print(sd)

stv = SmartTV("Smart TV", True, "55 inches")
print(stv)

