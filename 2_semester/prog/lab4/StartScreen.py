from tkinter import * 
from Calculator import Calculator
from Rectangle import Rectangle

class StartScreen(Calculator, Rectangle):
    def renderStartScreen(self, window):
        self.window = window 
        self.StartScreen = Frame(self.window)
        self.StartScreen.pack()
        self.radio = IntVar();
        self.label = Label(self.StartScreen, text= 'Select mode:')
        self.label.pack()
        self.radio1 = Radiobutton(self.StartScreen, text='Calculator', value = 0, variable=self.radio)
        self.radio1.pack()
        self.radio2 = Radiobutton(self.StartScreen, text='Rectangle', value = 1, variable=self.radio)
        self.radio2.pack()
        self.button = Button(self.StartScreen, text='Enter',command = self.__buttonOnClick).pack()

    def __buttonOnClick(self):
        self.clearStartScreen()
        if self.radio.get() == 0:
            self.renderCalculator(self.window)
        else:
            self.renderRectangleScreen(self.window)
            

    def clearStartScreen(self):
        self.StartScreen.destroy()
