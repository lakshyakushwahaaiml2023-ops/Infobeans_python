'''39. Navigation System

Methods:

navigate()

Implement:

GoogleMaps
AppleMaps'''

from abc import ABC, abstractmethod

class Map(ABC):
  @abstractmethod
  def navigate():
    pass

class GoogleMaps(Map):
  def navigate(self):
    print("Navigating using google maps...")

class AppleMaps(Map):
  def navigate(self):
    print("Navigating using apple maps...")

g = GoogleMaps()
g.navigate()
print()
a = AppleMaps()
a.navigate()
