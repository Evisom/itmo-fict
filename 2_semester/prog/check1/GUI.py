from tkinter import *
# from App import App 
from tkinter import *

class GUI():
    def renderGUI(self, callback):
        self.root = Tk()

        self.root.title('Deposit calculator')
        self.root.geometry('400x250')
        self.Title = Label(text='Калькулятор вкладов').grid(row=0, column=0)
        self.Label1 = Label(text='Сколько вы хотите вложить?').grid(row=1, column=0)
        self.Inp1 = Entry()
        self.Inp1.grid(row=1, column=1)
        self.Label2 = Label(text='На какой срок?').grid(row=2, column=0)
        self.Inp2 = Entry()
        self.Inp2.grid(row=2, column=1)
        self.Button = Button(text='Посчитать!', command=lambda callback = callback: self.getValues(callback))
        self.Button.grid(row=3)
        self.root.mainloop()

    def getValues(self, callback):
        try:
            self.amount = int(self.Inp1.get())
            self.periods = int(self.Inp2.get())
        except: 
            self.amount = False 
            self.periods = False 
        callback()
        self.renderResults()

    def renderResults(self):
        try: self.resultFrame.destroy()
        except: pass 
        self.resultFrame = Frame()
        if self.amount == False:
            self.err = Label(self.resultFrame, text='ERROR').pack()
        else:
            
            self.dl1 = Label(self.resultFrame, text='Fast deposit:' + str(self.a1.balance)).pack()
            self.dl2 = Label(self.resultFrame, text='Bonus deposit:' + str(self.a2.balance)).pack()
            self.dl3 = Label(self.resultFrame, text='Long deposit:' + str(self.a3.balance)).pack()
        self.resultFrame.grid(row=4)
        
    