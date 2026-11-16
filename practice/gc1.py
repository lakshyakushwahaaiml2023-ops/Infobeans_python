import gc
import time

class A:
    def __init__(self):
        print("A - init called...")
        time.sleep(2)

    def __del__(self):
        print("A Destructor called...")
        time.sleep(2)

# gc.disable()
a = A()
b = A()
a.x = b
b.x = a
del a
del b
# gc.collect()
print("Hello")