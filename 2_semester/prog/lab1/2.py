class Triangle:
    def __init__(self, a, b, c):
        self.correct = True
        if a <= 0 or b <= 0 or c <= 0:
            print('Incorrect triangle')
            self.correct = False
        if not (a <= b+c and b <= a+c and c <= b+a):
            print('Incorrect triangle')
            self.correct = False

        self.a = a
        self.b = b
        self.c = c
    def getSquare(self):
        if self.correct:
            p = (self.a + self.b + self.c)/2
            s = (p*(p-self.a)*(p - self.b)*(p-self.c))**(1/2)
            print(s)
        else:
            print('Incorrect triangle')

tr1 = Triangle(0,0,0)

tr2 = Triangle(3,3,3)
tr2.getSquare()

tr3 = Triangle(4, 2, 3)
tr3.getSquare()
