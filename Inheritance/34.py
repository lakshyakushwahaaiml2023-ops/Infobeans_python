'''34. Cloud Storage Interface

Methods:

upload()
download()

Implement:

GoogleDrive
Dropbox'''

from abc import ABC, abstractmethod

class Cloud(ABC):
  @abstractmethod
  def upload():
    pass

  @abstractmethod
  def download():
    pass

class GoogleDrive(Cloud):
  def upload(Self):
    print("File uploading to google drive storage...")

  def download(self):
    print("File downloading from google drive storage...")

class DropBox(Cloud):
  def upload(Self):
    print("File uploading to Dropbox storage...")

  def download(self):
    print("File downloading from Dropbox storage...")

gd = GoogleDrive()
gd.upload()
gd.download()
