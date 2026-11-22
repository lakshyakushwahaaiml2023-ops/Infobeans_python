'''32. Database Interface

Methods:

connect()
disconnect()

Implement:

MySQL
MongoDB
PostgreSQL'''

from abc import ABC, abstractmethod

class Database(ABC):
  @abstractmethod
  def connect(self):
    pass

  @abstractmethod
  def disconnect(self):
    pass

class MySQL(Database):
  def connect(self):
    print("Database connection established -> MySQL")

  def disconnect(self):
    print("Datbase connection terminated -> MySQL")
    
    
class MongoDB(Database):
  def connect(self):
    print("Database connection established -> MongoDB")

  def disconnect(self):
    print("Datbase connection terminated -> MongoDB")
    

class PostgreSQL(Database):
  def connect(self):
    print("Database connection established -> PostgreSQL")

  def disconnect(self):
    print("Datbase connection terminated -> PostgreSQL")

mysql = MySQL()
mysql.connect()
mysql.disconnect()
print()
mongo = MongoDB()
mongo.connect()
mongo.disconnect()
print()
psql = PostgreSQL()
psql.connect()
psql.disconnect()
