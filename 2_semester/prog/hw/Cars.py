from tkinter import *
from Truck import Truck
from Database import Database

class Cars ():
    def renderCars(self, root):
        self.root = root 
        self.CarsFrame = Frame()
        self.AddTitle = Button(self.CarsFrame, text='Добавить машину:', command=self.addCar).pack()
        self.eName = Entry(self.CarsFrame)
        self.eName.pack()
        self.eCap = Entry(self.CarsFrame)
        self.eCap.pack()
        self.eW = Entry(self.CarsFrame)
        self.eW.pack()
        self.eL = Entry(self.CarsFrame)
        self.eL.pack()
        self.eH = Entry(self.CarsFrame)
        self.eH.pack()
        self.CarsFrame.pack()
        # кнопочки и инпуты покрасивее сделаешь по своему усмотрению

        self.showTrucks()


    def showTrucks(self):
        d = Database('db.sqlite3')
        d.connect()
        trucks = d.select('trucks', ';')

        print(trucks)
        try: self.truckList.destroy()
        except: pass 
        self.truckList = Frame(self.CarsFrame)
        for i in trucks:
            print(i)
            Label(self.truckList, text=i[0]).grid(row=trucks.index(i), column=1)
            Label(self.truckList, text=i[1]).grid(row=trucks.index(i), column=2)
            Label(self.truckList, text=i[2]).grid(row=trucks.index(i), column=3)
            Label(self.truckList, text=i[3]).grid(row=trucks.index(i), column=4)
            Label(self.truckList, text=i[4]).grid(row=trucks.index(i), column=5)
            Label(self.truckList, text=i[5]).grid(row=trucks.index(i), column=6)
            Label(self.truckList, text=i[6]).grid(row=trucks.index(i), column=7)
            Button(self.truckList, text='delete', command=lambda arg=i:self.deleteCar(arg)).grid(row=trucks.index(i), column=8)
        self.truckList.pack()

    def deleteCar(self, data):
        print('del', data)
        truck = Truck(data[0], data[1], data[2], data[3], data[4])
        truck.deleteTruck()
        self.showTrucks()

    def addCar(self):
            # тут сделаешь проверку параметров на все возможные ошибки
            truck = Truck(self.eName.get(), self.eCap.get(), self.eW.get(), self.eL.get(), self.eH.get())
            truck.addTruck()
            self.showTrucks()

    def destroyCars(self):
        try: self.CarsFrame.destroy()
        except: pass