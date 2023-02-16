class Pupil:
    def __init__ (self, name='Radomit', age=8, classNumber='1-A'):
        self.__name = name 
        self.__age = age 
        self.__classNumber = classNumber
    
    def getName(self):
        return self.__name 
    
    def setName(self, name):
        self.__name = name 
        return True 
    
    def getAge(self):
        return self.__age 

    def setAge(self, age):
        self.__age = age
        return True 

    def getClassNumber(self):
        return self.__classNumber 

    def setClassNumber(self, classNumber):
        self.__classNumber = classNumber 

    def getInfo(self):
        print('Имя:' , self.__name)
        print('Возраст: ', self.__age)
        print('Класс: ', self.__classNumber)


st1 = Pupil('Vasya', 11, 3)
st1.getInfo()


st2 = Pupil('Artem', 12, 3)
st2.getInfo()

st3 = Pupil('Nikita', 31, 5)
st3.getInfo()

st4 = Pupil('Jenya', 14, 4)
st4.getInfo()

st5 = Pupil('Alisa', 16, 2)
st5.getInfo()

st6 = Pupil()
st6.getInfo()