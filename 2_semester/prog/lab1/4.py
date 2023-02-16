class Tree:
    def __init__ (self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        self.plant = False
        self.cutOff = False 
    def plant(self):
        if not(self.plant):
            self.plant = True
            print('Дерево пересадили')
        else:
            print('Дерево уже пересажено')
    def cutOff(self):
        if not(self.cutOff):
            self.cutOff = True
            print('Дерево срублено')
        else:
            print('Дерево уже срубили')
        
    def setName(self, name):
        self.name = name 
    
    def setHeight(self, height):
        self.height = height

    def getInfo(self):
        
        print('Имя дерева:' , self.name)
        print('Возраст дерева:' , self.age)
        print('Высота дерева:' , self.height)
        print("Дерево посажено:" , self.plant)
        print("Дерево срублено:" , self.cutOff)
        

tree1 = Tree('дерево1', '2', '4')
tree1.setName('dsfdsf')
tree1.getInfo()
