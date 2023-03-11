# import deposit classes
from FastDeposit import FastDeposit
from BonusDeposit import BonusDeposit
from LongDeposit import LongDeposit


amount = int(input('How much do you want to invest? '))
periods = int(input('How long? '))


account1 = FastDeposit(amount)
account2 = BonusDeposit(amount)
account3 = LongDeposit(amount)

# Calculate profit for every period
print()
for i in range(periods):
    account1.period()
    account2.period()
    account3.period()

print('Fast deposit', account1.getBalance())
print('Bonus deposit', account2.getBalance())
print('Long deposit', account3.getBalance())