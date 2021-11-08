# Object Oriented Programming Challenge

# For this challenge, create a bank account class that has two attributes:

# * owner
# * balance

# and two methods:

# * deposit
# * withdraw

# As an added requirement, withdrawals may not exceed the available balance.

# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:

   def __init__(self, owner, balance):
      self.owner = owner
      self.balance = balance

   def __str__(self):
      return f"Account owner: {self.owner}\nAccount balance: {self.balance}"

   def deposit(self, dep):
      print(f"{dep} has been deposited.")
      self.balance = self.balance + dep


   def withdraw(self,wdrw):
      if wdrw > self.balance:
         print("Funds Unavailable!")
      else:
         self.balance = self.balance - wdrw
         print(f"{wdrw} has been withdrawn.")