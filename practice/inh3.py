class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B):
    pass

class E(C):
    pass

class F(D, E):
    pass

print(f"A MRO: {A.__mro__}")
print(f"B MRO: {B.__mro__}")
print(f"C MRO: {C.__mro__}")
print(f"D MRO: {D.__mro__}")
print(f"E MRO: {E.__mro__}")
print(f"F MRO: {F.__mro__}")

#In multiple inheritance, the method resolution order (MRO) is determined by the 
# C3 linearization algorithm. The MRO defines the order in which classes are searched 
# when looking for a method or attribute.
# Left --> Right --> Node

'''C3 linearization algorithm...'''