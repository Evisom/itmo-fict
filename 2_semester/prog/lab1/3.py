class Mathem:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def addition(self):
        result = self.a + self.b
        print(result)
    def substraction(self):
        result = self.a - self.b
        print(result)
    def multiplication(self):
        result = self.a * self.b
        print(result)
    def division(self):
        if self.b != 0:
            result = self.a / self.b
            print(result)
        else:
            print('Нельзя делить на ноль')

m = Mathem(int(input()), int(input()))
m.addition()
m.substraction()
m.multiplication()
m.division()