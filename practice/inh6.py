from abc import ABC, abstractmethod

class A(ABC):

    @abstractmethod
    def __new__(cls):
        pass

class B(A):
    pass

b = A()
print(b)
print(type(b))
print(A.mro())