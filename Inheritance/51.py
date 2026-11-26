'''Real-World Logical Python OOP Problems
(Inheritance + Abstract Class + Polymorphism)

These are better for interviews because they focus on:

logical thinking
reusable design
business rules
object-oriented reasoning

instead of large system design.

1. Employee Bonus Calculator
Problem Statement

A company gives bonuses differently based on employee type.

Create:

abstract class Employee
child classes:
Developer
Manager
Intern

Rules:

Developer → 20% bonus
Manager → 35% bonus
Intern → fixed ₹5000 bonus
Requirements

Methods:

calculate_bonus()
display_details()
Concepts
Abstract class
Method overriding
Business logic




	​


11. Shape Drawing Application
Problem Statement

A drawing app supports multiple shapes.

Create abstract class Shape.

Child:

Circle
Rectangle
Triangle

Each implements:

draw()
area()
12. Authentication System
Problem Statement

Users can login using multiple methods.

Create:

abstract class Authentication

Child:

OTPAuth
GoogleAuth
FingerprintAuth
13. File Export System
Problem Statement

Application exports files in multiple formats.

Create:

abstract class Exporter

Child:

PDFExporter
ExcelExporter
CSVExporter
14. Employee Attendance Tracker
Problem Statement

Attendance calculation differs.

Create:

abstract class Employee

Child:

FullTimeEmployee
PartTimeEmployee
ContractEmployee
15. Payment Processing System
Problem Statement

Payment methods process payments differently.

Create:

abstract class Payment

Child:

CreditCard
DebitCard
UPI
16. Hospital Billing System
Problem Statement

Hospital charges differ by patient type.

Create:

abstract class Patient

Child:

GeneralPatient
ICUPatient
EmergencyPatient
17. Smart Appliance Controller
Problem Statement

Different appliances behave differently.

Create:

abstract class Appliance

Child:

Fan
AC
WashingMachine
18. Report Card Generator
Problem Statement

Different grading systems exist.

Create:

abstract class Student

Child:

SchoolStudent
CollegeStudent

Each generates grades differently.

19. Courier Service Pricing
Problem Statement

Pricing depends on package type.

Create:

abstract class Courier

Child:

NormalCourier
ExpressCourier
SameDayCourier
20. Ticket Booking System
Problem Statement

Ticket prices differ by seat category.

Create:

abstract class Ticket

Child:

SilverTicket
GoldTicket
PlatinumTicket
21. Online Subscription Plans
Problem Statement

Streaming app has multiple subscription plans.

Create:

abstract class Subscription

Child:

BasicPlan
StandardPlan
PremiumPlan

Each has different:

price
screen limits
22. Notification Service
Problem Statement

Application sends notifications differently.

Create:

abstract class Notification

Child:

EmailNotification
SMSNotification
PushNotification
23. Banking Withdrawal System
Problem Statement

Withdrawal rules vary by account type.

Create:

abstract class Account

Child:

SavingsAccount
CurrentAccount
24. Ride Sharing App Surge Pricing
Problem Statement

Surge pricing differs.

Create:

abstract class RidePricing

Child:

NormalTime
PeakTime
RainTime
25. Employee Work Report System
Problem Statement

Different employees submit reports differently.

Create:

abstract class WorkReport

Child:

DeveloperReport
TesterReport
ManagerReport

'''