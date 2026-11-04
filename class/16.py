
import time 

class Test:
    def __new__(cls, name, age):
        print("Creating instance of Test class")
        instance = super().__new__(cls)
        instance.name = name
        instance.age = age
        return instance

    def __init__(self, name, age):
        print("__init__ called...")
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name=}, {self.age = }"

start = time.perf_counter()
t1 =Test("Lakshya", 12)
end = time.perf_counter()
print(t1, "Time Taken: ", end - start)
