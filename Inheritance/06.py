'''
Parent:

HospitalStaff

Child:

Doctor
Nurse
Receptionist

Implement duties().'''

from abc import ABC, abstractmethod

class HospitalStaff(ABC):

    @abstractmethod
    def duty(self):
        pass

class Doctor(HospitalStaff):

    def duty(Self):
        print("Doctor Duties:")
        print("1. Examine Patients...")
        print("2. Prescribe Medicines...")
        print("3. Perform Surgery...")

class Receptionist(HospitalStaff):

    def duty(Self):
        print("Receptionists Duties:")
        print("1. Track Visitors entry time...")
        print("2. Track Visitors exit time...")
        print("3. Check which patient visitor wants to visit ...")

class Nurse(HospitalStaff):

    def duty(Self):
        print("Nurse Duties:")
        print("1. Give medicines to patients...")
        print("2. Keep the patients in check...")
        print("3. Change bandages and other things...")


n = Nurse()
d = Doctor()
r = Receptionist()

n.duty()
r.duty()
d.duty()