from tkinter import *
from Database import Database
from Truck import Truck

class BookedTrucks():
    def renderBookedTrucks(self, root):
        try: self.destroyBookedTrucks()
        except: pass
        self.root = root 
        self.BookedFrame = Frame(self.root)
        # Label(self.BookedFrame, text='1').pack()
        self.renderBooked()
        self.BookedFrame.pack()

    def destroyBookedTrucks(self):
        try: self.BookedFrame.destroy()
        except: pass

    def renderBooked(self):
        d = Database('db.sqlite3')
        d.connect()
        trucks = d.select('trucks', ';')
        render_arr = []
        for i in trucks: 
            if i[5] == 1:
                render_arr.append(i)

        for i in range(len(render_arr)):
            Label(self.BookedFrame, text=render_arr[i][0]).grid(row=i, column=0)
            t = render_arr[i]
            Button(self.BookedFrame, text='убрать бронирование', command=lambda truck = t: self.unbook(truck)).grid(row=i, column=1)

    def unbook(self, i):
        truck = Truck(i[0], i[1], i[2], i[3], i[4])
        truck.unbookTruck()
        self.renderBookedTrucks(self.root)
