'''8. Salary Tax Calculator
Problem Statement

Tax calculation differs by employee category.

Create:

abstract class TaxPayer

Child:

GovernmentEmployee
PrivateEmployee
Freelancer'''

from abc import ABC, abstractmethod

class TaxPayer(ABC):
    @abstractmethod
    def tax():
        pass

class GovernmentEmployee(TaxPayer):
    def tax(self, income):
        return income * 0.10

    def getName(self):
        return "Government Employee"


class PrivateEmployee(TaxPayer):
    def tax(self, income):
        return income * 0.15

    def getName(self):
        return "Private Employee"

class Freelancer(TaxPayer):
    def tax(self, income):
        return income * 0.20

    def getName(self):
        return "Freelancer"

emps = [GovernmentEmployee(),
        PrivateEmployee(),
        Freelancer()]

income = 50000

for employee in emps:
    print(f"{employee.getName()} : Tax -> {employee.tax(income)}")
