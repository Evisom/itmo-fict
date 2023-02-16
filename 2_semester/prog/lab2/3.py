class Country:
    def __init__(self, capital, population=0):
        self.__capital = capital
        if population >= 0:
            self.__population = population 

    def setPopulation(self, population):
        self.__population = population

    def getInfo(self):
        print(self._Country__capital)
        print(self._Country__population)
    
class Russia(Country):
    def __init__ (self):
        super().__init__('Moscow')


class Germany(Country):
    def __init__ (self):
        super().__init__('Berlin')

class Canada(Country):
    def __init__ (self):
        super().__init__('Ottawa')

r = Russia()
r.setPopulation(1324324)
r.getInfo()

c = Canada()
c.setPopulation(324535)
c.getInfo()

g = Germany()
g.setPopulation(4567643)
g.getInfo()