class Calculator:

    @staticmethod
    def __get_input(func):
        def wrap(self):
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))
            return func(self, a,b)
        return wrap

    @__get_input
    def add(self, a, b):
        return a + b

class Sec_Calculator(Calculator):
    pass

c = Sec_Calculator()
print(c.add())