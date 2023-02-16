class Cat:
    def __init__ (self, name, age, hair, className):
        self.__name = name 
        self.__hair = hair 
        self.__className = className
        if age >= 0:
            self.__age = age
        else:
            print('Возраст не может быть отрицательным')
            self.__age = False 

    def getInfo(self):
        print()
        print(self.__name)
        print(self.__age)
        print(self.__hair)
        print(self.__className)

class Sphinx(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, 'bald', 'hunter')


class MaineCoon(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, 'long', 'relax')

class Korat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, 'medium', 'mousehunter')

s = Sphinx('Barsik', 10)
s.getInfo()


m = MaineCoon('Ugolyok', 6)
m.getInfo()

k = Korat('Murzik', 2)
k.getInfo()

