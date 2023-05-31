from tkinter import *
from Truck import Truck
from Database import Database

class Cars ():
    def renderCars(self, root):
        self.root = root 
        self.CarsFrame = Frame()
        self.AddTitle = Button(self.CarsFrame, text='Добавить машину:', command=self.addCar).grid(row=5, column=0, columnspan=2)
        Label(self.CarsFrame, text='Марка машины').grid(row=0, column=0)
        self.eName = Entry(self.CarsFrame)
        self.eName.grid(row=0, column=1)
        Label(self.CarsFrame, text='Грузоподъемность').grid(row=1, column=0)
        self.eCap = Entry(self.CarsFrame)
        self.eCap.grid(row=1, column=1)
        Label(self.CarsFrame, text='Ширина').grid(row=2, column=0)
        self.eW = Entry(self.CarsFrame)
        self.eW.grid(row=2, column=1)
        Label(self.CarsFrame, text='Длина').grid(row=3, column=0)
        self.eL = Entry(self.CarsFrame)
        self.eL.grid(row=3, column=1)
        Label(self.CarsFrame, text='Высота').grid(row=4, column=0)
        self.eH = Entry(self.CarsFrame)
        self.eH.grid(row=4, column=1)
        self.CarsFrame.pack()
        self.sortIncrease = None 
        self.SortButton = Button(self.CarsFrame, text='Сортировать', command=self.sortBy)
        self.SortButton.grid(row=6, column=0)
        # кнопочки и инпуты покрасивее сделаешь по своему усмотрению

        self.showTrucks()

    def sortBy(self):
        if self.sortIncrease == None:
            self.sortIncrease = True 
            self.SortButton.config(text='↑')
        elif self.sortIncrease:
            self.SortButton.config(text='↑')
            self.sortIncrease = False
        else:
            self.SortButton.config(text='↓')
            self.sortIncrease = True
        self.showTrucks(self.sortByCap, self.sortIncrease)

    def sortByCap(self, arr, increase):
        swapped = False
        
        for n in range(len(arr)-1, 0, -1):
            for i in range(n):
                if arr[i][1] > arr[i + 1][1]:
                    swapped = True
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]       
            if not swapped:
                if increase:
                    return arr
                else:
                    return arr[::-1]
        if increase: return arr
        else: return arr[::-1]

    def showTrucks(self, sortMethod=False, v=False):
        d = Database('db.sqlite3')
        d.connect()
        trucks = d.select('trucks', ';')

        print(trucks)
        try: self.truckList.destroy()
        except: pass 
        if sortMethod:
            trucks = sortMethod(trucks, v)
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
        self.truckList.grid(row=7, column=0, columnspan=2)

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