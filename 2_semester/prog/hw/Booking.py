from tkinter import *

class Booking ():
    def renderBooking(self, root):
        self.root = root 
        self.BookingFrame = Frame()
        self.Label = Label(self.BookingFrame, text='Введите параметры груза').pack()
        self.eW = Entry(self.BookingFrame)
        self.eH = Entry(self.BookingFrame)
        self.eL = Entry(self.BookingFrame)
        self.eCap = Entry(self.BookingFrame)
        self.eW.pack()
        self.eH.pack()
        self.eL.pack()
        self.eCap.pack()
        self.Button = Button('Подобрать грузовик')
        self.BookingFrame.pack()
    def destroyBooking(self):
        try: self.BookingFrame.destroy()
        except: pass
