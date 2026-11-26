'''60. Loan Interest Calculator
Problem Statement

Banks offer different interest rates.

Create:

abstract class Loan

Child:

HomeLoan
CarLoan
EducationLoan
Formula

Interest=
100
P×R×T'''

from abc import ABC, abstractmethod

class Loan(ABC):

    @property
    @abstractmethod
    def intrest_rate(self):
        pass

    @property
    @abstractmethod
    def getName(self):
        pass

class HomeLoan(Loan):
    @property
    def intrest_rate(self):
        return 8.5

    @property
    def getName(self):
        return "Home-Loan"

class CarLoan(Loan):
    @property
    def intrest_rate(self):
        return 9.5

    @property
    def getName(self):
        return "Car-Loan"

class EducationLoan(Loan):
    @property
    def intrest_rate(self):
        return 6.5

    @property
    def getName(self):
        return "Eductaion-Loan"
    
for i in [HomeLoan(), CarLoan(), EducationLoan()]:
    print(i.getName, " --> Interest Rate: ", i.intrest_rate, "%")