'''38. File Compression Tool

Methods:

compress()

Implement:

ZIPCompression
RARCompression'''

from abc import ABC, abstractmethod

class Compresser(ABC):
  @abstractmethod
  def compress():
    pass

class ZIP(Compresser):
  def compress(self, name):
    print(f"{name} compressed using -> ZIP")

class RAR(Compresser):
  def compress(self, name):
    print(f"{name} compressed using -> RAR")

z = ZIP()
z.compress("Game1")

r = RAR()
r.compress("Movies")
