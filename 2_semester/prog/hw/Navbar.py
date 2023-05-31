from tkinter import *

class Navbar():
    def renderNavbar (self, root, action1, action2, action3):
        self.root = root
        self.NavbarFrame = Frame()
        self.NavbarLabel = Label(self.NavbarFrame, text='ООО "Бешенные гонщики"').grid(row=0, column=0)
        self.NavbarButton1 = Button(self.NavbarFrame, text='Машины', command=action1).grid(row=0, column=1)
        self.NavbarButton2 = Button(self.NavbarFrame, text='Бронирование', command=action2).grid(row=0, column=2)
        self.NavbarButton3 = Button(self.NavbarFrame, text='Забронированные машины', command=action3).grid(row=0, column=3)
        self.NavbarFrame.pack()

    
