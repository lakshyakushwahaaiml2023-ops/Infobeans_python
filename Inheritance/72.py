'''72. Notification Service
Problem Statement

Application sends notifications differently.

Create:

abstract class Notification

Child:

EmailNotification
SMSNotification
PushNotification
'''
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send_noti(self):
        pass

class EmailNotification(Notification):
    def send_noti(self, msg):
        return f"Notification pop-up from email...{msg}"

class SMSNotification(Notification):
    def send_noti(self, msg):
        return f"Notification pop-up from SMS...{msg}"

class PushNotification(Notification):
    def send_noti(self, msg):
        return f"Notification pop-up from Push...{msg}"

notis = [EmailNotification(), SMSNotification(), PushNotification()]

for i in notis:
    print(i.send_noti("Hello ~ Lakshya..."))