'''77. Game Character Attack System
Problem Statement

Game characters attack differently.

Create:

abstract class Character

Child:

Archer
Warrior
Mage'''


from abc import ABC, abstractmethod

class Character:
    @abstractmethod
    def attack(self):
        pass

class Archer(Character):
    def attack(self):
        print("Archer Attack = Arrow")

class Warrior(Character):
    def attack(self):
        print("Warrior Attack = Sword")

class Mage(Character):
    def attack(self):
        print("Mage Attack = Magic")

chars = [Archer(), Warrior(), Mage()]
for c in chars:
    c.attack()  