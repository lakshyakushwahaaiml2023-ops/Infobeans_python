'''75. Employee Work Report System
Problem Statement

Different employees submit reports differently.

Create:

abstract class WorkReport

Child:

DeveloperReport
TesterReport
ManagerReport'''

from abc import ABC, abstractmethod

class WorkReport(ABC):
    @abstractmethod
    def report(self):
        pass

class DeveloperReport(WorkReport):
    def __init__(self, name, id, report_t):
        self.__name = name
        self.__id = id
        self.__report = report_t
        self.__role = "Developer"

    def report(self):
        return f"{self.__name} | {self.__id} | {self.__role}nReport: {self.__report}"

class TesterReport(WorkReport):
    def __init__(self, name, id, report_t):
        self.__name = name
        self.__id = id
        self.__report = report_t
        self.__role = "Tester"

    def report(self):
        return f"{self.__name} | {self.__id} | {self.__role}nReport: {self.__report}"

class ManagerReport(WorkReport):
    def __init__(self, name, id, report_t):
        self.__name = name
        self.__id = id
        self.__report = report_t
        self.__role = "Manager"

    def report(self):
        return f"{self.__name} | {self.__id} | {self.__role}Report: {self.__report}"


dev = DeveloperReport(
    "Lakshya", "D101", "Completed API development"
)

tester = TesterReport(
    "Diksha", "T102", "Completed login module testing"
)

manager = ManagerReport(
    "Riya", "M103", "Reviewed project progress"
)

employees = [dev, tester, manager]

for employee in employees:
    print(employee.report())
    print("-" * 40)