from tkinter import *
from Database import Database
from Truck import Truck

class Booking ():
    def renderBooking(self, root):
        self.root = root 
        self.BookingFrame = Frame()
        self.Label = Label(self.BookingFrame, text='Введите параметры груза').grid(row=0, column=0, columnspan=2)
        self.eW = Entry(self.BookingFrame)
        self.eH = Entry(self.BookingFrame)
        self.eL = Entry(self.BookingFrame)
        self.eCap = Entry(self.BookingFrame)
        Label(self.BookingFrame, text='Ширина:').grid(row=1, column=0)
        self.eW.grid(row=1, column=1)
        Label(self.BookingFrame, text='Высота:').grid(row=2, column=0)
        self.eH.grid(row=2, column=1)
        Label(self.BookingFrame, text='Длинна:').grid(row=3, column=0)
        self.eL.grid(row=3, column=1)
        Label(self.BookingFrame, text='Грузоподъемность:').grid(row=4, column=0)
        self.eCap.grid(row=4, column=1)
        self.Button = Button(self.BookingFrame, text='Подобрать грузовик', command=self.getTruck)
        self.Button.grid(row=5, column=0, columnspan=2)
        self.BookingFrame.pack()
        self.BookingResults = Frame(self.BookingFrame)
        self.BookingResults.grid(row=6, column=0, columnspan=2)

    def destroyBooking(self):
        try: self.BookingFrame.destroy()
        except: pass

    def getTruck(self):
        d = Database('db.sqlite3')
        d.connect()
        trucks = d.select('trucks', ';')
        c = int(self.eCap.get())
        w = int(self.eW.get())
        h = int(self.eH.get())
        l = int(self.eL.get())
        r = 0
        for i in trucks:
            truck = Truck(i[0], i[1], i[2], i[3], i[4])
            if truck.isFit(c, w, h, l) and i[5] == 0:
                Label(self.BookingResults, text=truck.name).grid(row=r, column=0)
                Button(self.BookingResults, text='Забронировать', command=truck.bookTruck).grid(row=r, column=1)
                r+=1