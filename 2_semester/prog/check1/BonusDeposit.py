from Deposit import Deposit

class BonusDeposit(Deposit):
    def __init__(self, balance=0, bonusroi = 0.1, basicroi = 0.01, bonusmin = 100000) -> None:
        super().__init__(balance)
        self._basicRoi = basicroi # ROI for accounts with balance under bonusMin
        self._bonusRoi = bonusroi # ROI for accounts with balance over bonusMibn
        self._bonusMin = bonusmin 
        self._profit = 0

    def __str__ (self): # Overloading default str method
        info = ('Open: ' + str(self._isOpened) + '\nBalance: ' +  str(self._balance) + '\nPeriods:' + str(self._periods) + '\nProfit: ' + str(self._profit))
        return info       

    def getBalance(self): # Method returns balance + profit for all time 
        return round(self._balance + self._profit, 2)
    
    def period(self):
        self._periods +=1
        if self._balance > self._bonusMin: # Check account balance
            self._Deposit__updateHistory(self._balance * self._basicRoi )
            self._profit += self._balance * self._bonusRoi 
        else:
            self._Deposit__updateHistory(self._balance * self._basicRoi )
            self._profit += self._balance * self._basicRoi 

