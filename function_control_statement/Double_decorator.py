import time 

def check_performance(func):
    def wrap():
        start = time.perf_counter()
        print(f"Start: {start}")
        func()
        end = time.perf_counter()
        print(f"End: {end}")
        return f"Total Execution time: {end - start}"
    return wrap

def take_input(func):
    def wrap():
        a = int(input("a = "))
        b = int(input("b = "))
        return func(a,b)
    return wrap

def check_divisibility(func):
    def wrap(a,b):
        if b==0:
            return f"Cannot divide by 0"
        return func(a,b)
    return wrap

@check_performance
@take_input
def add(a,b):
    return a + b

@take_input
@check_divisibility
def divide(a,b):
    return a/b


print(add())
# print(divide())
