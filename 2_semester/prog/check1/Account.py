from functools import wraps 
import Error 

class Account: 
    def log(func):
        print('Transaction complete')
        return func 
    @log 
    def __add__(self, amount): # Top up method 
        if self._isOpened: # Account must be opened
            if amount > 0: # Amount must be positive
                self._balance += amount 
                self._updateHistory(amount)
            else: print('Amount must be positive')
        else: raise Error.AccountClosed
    @log
    def __sub__(self, amount): # Top up method 
        if self._isOpened: # Account must be opened
            if amount > 0: # Amount must be positive
                self._balance -= amount 
                self._updateHistory((-1)*amount)
            else: print('Amount must be positive')
        else: raise Error.AccountClosed
    
    @property
    
    def balance(self): # Method return currect balance
        return round(self._balance + self._profit, 2)