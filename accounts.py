import datetime
from datetime import date
import math

class User:
    def __init__(self):
        pass

# Account id, dateCreated, Account Level(gold, silver), password, email, phone number, address
# methods: add, subtract, close
class Account: #superclass
    id = 0
    wait = 0
    availableFunds = 0
    def __init__(self, accountLevel, password, email, phoneNumber, address):
        self.id = id
        self.dateCreated = date.today()
        self.accountLevel = accountLevel
        self.password = password
        self.email = email
        self.phoneNumber = phoneNumber
        self.address = address
        self.value = 0
        self.wait = 0

        Account.id += 1

    def __str__(self):
        return str(self.value)

    def deposit(self, amount):
        self.value += amount
        Account.availableFunds = Account.availableFunds + amount
        self.setFunds()
        return(f"${amount} added to {self.__class__.__name__}| new account balance is: ${self.value}")
        

    def withdraw(self, amount):
        if(self.wait > 0):
            return("waiting")
        if(amount > self.value):
            return("Not enough available funding in account")
        else:
            self.value -= amount
            Account.availableFunds = Account.availableFunds - amount
            return(f"${amount} withdrawn from {self.__class__.__name__}| new account balance is: ${self.value}")
            
    
    def getValue(self):
        return(f"${self.value}")
    
    def setValue(self, amount):
        if(self.value > amount):
            Account.availableFunds = Account.availableFunds - amount
        else:
            Account.availableFunds = Account.availableFunds + amount
        self.value = amount
        
        print(f"Value of account set to ${self.value}")
        return(self.value)

    def setFunds(self):
        return Account.availableFunds

    def Data(self):
        return(self.accountLevel + "\n"+ self.password+ "\n"+ self.email+ "\n"+ self.phoneNumber+ "\n"+ self.address)

    @classmethod # this will call the type class instead of every individual instance
    def out(cls): # cls is the class being saved
        return cls.__name__


class Checkings(Account):
    def __init__(self, accountLevel, password, email, phoneNumber, address):
        super().__init__(accountLevel, password, email, phoneNumber, address)
    def withdraw(self, amount):
        self.wait = 0
        super().withdraw(amount)

# cannot spend money in savings must be put into checkings
class Savings(Account):
    wait = 0
    def __init__(self, accountLevel, password, email, phoneNumber, address):
        super().__init__(accountLevel, password, email, phoneNumber, address)
    def withdraw(self, amount):
        super().withdraw(amount)
    
class Card():
    def __init__(self, password):
        self.balance = 0
        self.password = password
    
class creditCard(Card):
    def __init__(self, password):
        self.credit = 0
        super().__init__(password)
        
class debitCard(Card):
    def __init__(self, password):
        super().__init__(password)


