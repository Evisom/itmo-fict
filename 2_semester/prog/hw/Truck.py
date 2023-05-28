from Database import Database
from random import randint

class Truck():
    def __init__(self, name, cap, w, l, h):
        self.name = name 
        self.cap = int(cap)
        self.w = int(w) 
        self.l = int(l)
        self.h = int(h) 
        self.isBooked = 0 

        self.plate = self.w+self.l+self.h+self.cap  # подразумевается, что plate - уникальная строка, будет нашим primary key
        for i in self.name:
            self.plate += ord(i)
            print(self.plate)
        self.plate = hex(self.plate)
    
    def addTruck(self):
        d = Database('db.sqlite3')
        d.connect()
        d.insert('trucks', [
            (self.name, self.cap, self.w, self.l, self.h, self.isBooked, self.plate)
        ])
        d.close()

    def deleteTruck(self):
        d = Database('db.sqlite3')
        d.connect()
        print(self.plate)
        d.delete('trucks', 'WHERE plate ="' + self.plate +'";')
        d.close()

    def bookTruck(self):
        pass 

    def unbookTruck(self):
        pass 

    def isFit(self):
        pass 
    