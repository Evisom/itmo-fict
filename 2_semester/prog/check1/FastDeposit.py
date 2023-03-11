from Deposit import Deposit

class FastDeposit(Deposit):
    def __init__(self, balance=0, roi = 0.05) -> None:
        super().__init__(balance)
        self._roi = roi
        self._profit = 0

    # Withdraw and top-up are not availible for fast deposit
    def __add__ (self, amount):
        print('Not available for this deposit')

    def __sub__ (self, amount):
        print('Not available for this deposit')  

    def __str__ (self): # Overloading default str method
        info = ('Open: ' + str(self._isOpened) + '\nBalance: ' +  str(self._balance) + '\nPeriods:' + str(self._periods) + '\nProfit: ' + str(self._profit))
        return info       

    def getBalance(self): # Method returns balance + profit for all time 
        return round(self._balance + self._profit, 2)

    def period(self): # add profit to a separate account
        self._periods +=1
        self._profit += self._balance * self._roi 
        self._Deposit__updateHistory(self._balance * self._roi )
