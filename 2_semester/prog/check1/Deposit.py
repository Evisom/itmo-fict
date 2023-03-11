from datetime import date

class Deposit:
    # Basic deposit class
    def __init__(self, balance=0): # Deposit constructor
        self._balance = balance
        self._periods = 0
        self._isOpened = True
        self._transactions = []

    def __str__ (self): # Overloading default str method
        info = ('Open: ' + str(self._isOpened) + '\nBalance: ' +  str(self._balance) + '\nPeriods:' + str(self._periods))
        return info 

    def getHistory(self): # Method returns account history
        print('Date     | Amount | Balance')
        for i in self._transactions:
            print(i['date'], i['amount'], '   ', i['balance'])

    def getBalance(self): # Method return currect balance
        return round(self._balance,2)

    def __updateHistory(self, amount): # Method updates history 
        self._transactions.append({
            "amount": amount,
            "balance" : self._balance,
            "date": date.today()   
        })

    def __add__(self, amount): # Top up method 
        if self._isOpened: # Account must be opened
            if amount > 0: # Amount must be positive
                self._balance += amount 
                self.__updateHistory(amount)
            else: print('Amount must be greater than zero')
        else: print('Account closed')


    def __sub__(self, amount): # Top up method 
        if self._isOpened: # Account must be opened
            if amount > 0: # Amount must be positive
                self._balance -= amount 
                self._updateHistory((-1)*amount)
            else: print('Amount must be greater than zero')
        else: print('Account closed')
