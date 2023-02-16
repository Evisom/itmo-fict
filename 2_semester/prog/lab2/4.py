class Doctor:
    def __init__ (self, className):
        self.__name = 'Aybolit'
        self.__age = 25
        self.__className = className 
    
    def getName(self):
        print(self.__name)

    def setName(self, name):
        self.__name = name

    def getInfo(self):
        print(self.__dict__)

class Pediatrist(Doctor):
    def __init__(self):
        super().__init__('Pediatrist')
    def getName(self):
        print(self._Doctor__name + " - имя доктора")

class Dentist(Doctor):
    def __init__(self):
        super().__init__('Dentist')
    def getName(self):
        print(self._Doctor__name + " - имя доктора")


d1 = Pediatrist()
d1.getInfo()

d2 = Dentist()
d2.getInfo()