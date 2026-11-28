'''66. Hospital Billing System
Problem Statement

Hospital charges differ by patient type.

Create:

abstract class Patient

Child:

GeneralPatient
ICUPatient
EmergencyPatient'''

from abc import ABC, abstractmethod

class Patient(ABC):

    @property
    @abstractmethod
    def calculate_bill(self):
        pass

class GeneralPatient(Patient):

    def __init__(self, days_admitted):
        self.__days_admitted = days_admitted
        self.__daily_rate = 1000

    @property
    def calculate_bill(self):
        return self.__days_admitted * self.__daily_rate

class ICUPatient(Patient):

    def __init__(self, days_admitted):
        self.__days_admitted = days_admitted
        self.__daily_rate = 5000

    @property
    def calculate_bill(self):
        return self.__days_admitted * self.__daily_rate

class EmergencyPatient(Patient):

    def __init__(self, days_admitted):
        self.__days_admitted = days_admitted
        self.__daily_rate = 2000

    @property
    def calculate_bill(self):
        return self.__days_admitted * self.__daily_rate

patients = [GeneralPatient(5), ICUPatient(3), EmergencyPatient(2)]
for patient in patients:    
    print(f"Patient Type: {patient.__class__.__name__}, Total Bill: {patient.calculate_bill} Rs.")
