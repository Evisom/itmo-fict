import threading
from FastDeposit import FastDeposit
from BonusDeposit import BonusDeposit
from LongDeposit import LongDeposit
from GUI import GUI 

class App(GUI):
    def __init__ (self):
        self.amount = 0
        self.periods = 0
        # self.GUI = GUI()
        self.renderGUI(self.calculateDeposits)

    def calculateDeposits(self):
        self.a1 = FastDeposit(self.amount)
        self.a2 = BonusDeposit(self.amount)
        self.a3 = LongDeposit(self.amount)
        for i in range(self.periods):
            self.a1.period()
            self.a2.period()
            self.a3.period()
        self.renderResults()
