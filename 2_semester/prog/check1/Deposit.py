from datetime import date
from Account import Account

class Deposit(Account):
    # Basic deposit class
    def __init__(self, balance=0): # Deposit constructor
        self._balance = balance
        self._periods = 0
        self._isOpened = True
        self._transactions = []
        self._profit = 0

    def __str__ (self): # Overloading default str method
        info = ('Open: ' + str(self._isOpened) + '\nBalance: ' +  str(self._balance) + '\nPeriods:' + str(self._periods))
        return info 

    def getHistory(self): # Method returns account history
        print('Date     | Amount | Balance')
        for i in self._transactions:
            print(i['date'], i['amount'], '   ', i['balance'])

    def __updateHistory(self, amount): # Method updates history 
        self._transactions.append({
            "amount": amount,
            "balance" : self._balance,
            "date": date.today()   
        })

