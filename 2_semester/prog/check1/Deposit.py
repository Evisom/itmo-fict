from datetime import date
from Account import Account
import sqlite3 
from Database import Database
import hashlib
import asyncio
import random

class Deposit(Account):
    # Basic deposit class
    def __init__(self, balance=0): # Deposit constructor
        self._balance = balance
        self._periods = 0
        self._isOpened = True
        self._transactions = []
        self._profit = 0
        self._lastTransaction = 0



    def __str__ (self): # Overloading default str method
        info = ('Open: ' + str(self._isOpened) + '\nBalance: ' +  str(self._balance) + '\nPeriods:' + str(self._periods))
        return info 

    def getHistory(self): # Method returns account history
        print('Date     | Amount | Balance')
        for i in self._transactions:
            print(i['date'], i['amount'], '   ', i['balance'])

    async def recordTransaction(self, amount):
        db = Database('transactions.db')
        db.connect()
        db.insert('tr', [
            (str(abs(hash(str(amount)+str(self._balance) + str(date.today()) + str(random.randint(1,1000)))) % (10 ** 8)), str(amount), str(self._balance), str(date.today())),
        ])    
        # print(db.select('tr', '*  '))
        db.close()
        

    def _updateHistory(self, amount): # Method updates history 
        r = self.recordTransaction(amount)
        asyncio.run(r)
        
        # await r
        self._transactions.append({
            "amount": amount,
            "balance" : self._balance,
            "date": date.today()   
        })



# CREATE TABLE tr (
# 	id INT(20),
# 	amount INT(20),
# 	balance INT(20),
# 	date INT(20),
# 	PRIMARY KEY (`id`)
# );
