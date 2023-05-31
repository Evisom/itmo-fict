from tkinter import *
from Navbar import Navbar 
from Booking import Booking 
from Cars import Cars
from BookedTrucks import BookedTrucks

class UI (Navbar, Booking, Cars, BookedTrucks):
    def __init__ (self):
        self.root = Tk()
        self.root.geometry('500x500')
        self.root.title('Sample text')

        self.renderNavbar(self.root, self.showCars, self.showBooking, self.showBookedTrucks)

    def showBooking(self):
        self.destroyBooking()
        self.destroyCars()
        self.destroyBookedTrucks()
        self.renderBooking(self.root)
    def showCars(self):
        self.destroyBooking()
        self.destroyCars()
        self.destroyBookedTrucks()
        self.renderCars(self.root)

    def showBookedTrucks(self):
        self.destroyBooking()
        self.destroyCars()
        self.destroyBookedTrucks()
        self.renderBookedTrucks(self.root)

    def mainloop(self):
        self.root.mainloop()


