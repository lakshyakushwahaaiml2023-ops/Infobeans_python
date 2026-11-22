'''37. Social Login System

Methods:

login()

Implement:

GoogleLogin
GitHubLogin
LinkedInLogin'''

from abc import ABC, abstractmethod

class Login(ABC):
  @abstractmethod
  def login():
    pass

class Google(Login):
  def login(self, email):
    print("Log-ined using google -> ", email)    

class GitHub(Login):
  def login(self, gitid):
    print("Log-ined using github -> ", gitid)    

class LinkedIn(Login):
  def login(self, l_id):
    print("Log-ined using google -> ", l_id)    

g = Google()
g.login("kushwahalakshya@gmail.com")
print()
gh = GitHub()
gh.login("lakshyakushwaha-2023")
print()
l = LinkedIn()
l.login("lakshya-kushwaha-ai")
