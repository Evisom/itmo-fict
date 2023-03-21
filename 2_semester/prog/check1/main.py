# import deposit classes
from FastDeposit import FastDeposit
from BonusDeposit import BonusDeposit
from LongDeposit import LongDeposit


amount = int(input('How much money do you want to invest?'))
periods = int(input('For how long?'))

a1 = FastDeposit(amount)
a2 = BonusDeposit(amount)
a3 = LongDeposit(amount)


for i in range(periods):
    a1.period()
    a2.period()
    a3.period()

print('Fast deposit: ', a1.balance)
print('Bonus deoisut: ', a2.balance)
print('Long deposit: ', a3.balance)



































# from tkinter import * 

# window = Tk()
# window.title('Deposit calculator')
# window.geometry('300x400')



# title = Label(text='Deposit calculator', font=('Arial', 25)).pack(pady=20)
# label1 = Label(text='How much do you want to invest?').pack()
# input1 = Entry(window)
# input1.pack()
# label2 = Label(text='For how long?').pack()
# input2 = Entry(window)
# input2.pack()

# result1 = StringVar()
# result2 = StringVar()
# result3 = StringVar()



# def onclick():
#     amount = input1.get()
#     periods = input2.get()
#     correct = True 
#     try:
#         amount = int(amount)
#         periods = int(periods)
#     except:
#         errorLabel = Label(window, text='Invalid data!', fg='red')
#         errorLabel.pack()
#         errorLabel.after(2000, errorLabel.destroy)
#         correct = False 
#     if correct: 
#         a1 = FastDeposit(amount)
#         a2 = BonusDeposit(amount)
#         a3 = LongDeposit(amount)
#         for i in range(periods):
#             a1.period()
#             a2.period()
#             a3.period()
#         result1.set('Fast deposit: ' + str(a1.balance))
#         result2.set('Bonus deposit: ' + str(a2.balance))
#         result3.set('Long deposit: ' + str(a3.balance))


# button = Button(window, text='Calculate', command=onclick).pack()


# r1 = Label(textvariable=result1).pack()
# r2 = Label(textvariable=result2).pack()
# r3 = Label(textvariable=result3).pack()

# window.mainloop()
