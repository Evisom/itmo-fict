from Deposit import Deposit

class LongDeposit(Deposit):
    def __init__(self, balance=0, roi = 0.04) -> None:
        super().__init__(balance)
        self._roi = roi

    # Withdraw are not availible for long deposit 
    def __sub__ (self, amount):
        print('Not available for this deposit')  
        

    # Compound interest
    def period(self):
        self._periods +=1
        self._updateHistory(self._balance * self._roi)
        self._balance += self._balance * self._roi
    
    
        
