from tkinter import *
from Navbar import Navbar 
from Booking import Booking 
from Cars import Cars

class UI (Navbar, Booking, Cars):
    def __init__ (self):
        self.root = Tk()
        self.root.geometry('500x500')
        self.root.title('Sample text')

        self.renderNavbar(self.root, self.showCars, self.showBooking,)

    def showBooking(self):
        self.destroyBooking()
        self.destroyCars()
        self.renderBooking(self.root)
    def showCars(self):
        self.destroyBooking()
        self.destroyCars()
        self.renderCars(self.root)

    def mainloop(self):
        self.root.mainloop()


