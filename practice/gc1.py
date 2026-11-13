import gc

class A:
    def __init__(self):
        print("A - init called...")

    def __del__(self):
        print("A Destructor called...")


a = A()
b = A()
b.link = a
a.link = b
del a
del b
# gc.collect()
print("Hello...")