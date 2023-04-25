from tkinter import * 

class Calculator():
    def renderCalculator(self, window):
        self.window = window 
        self.CalculatorScreen = Frame(self.window)
        self.CalculatorScreen.pack()
        self.buttons = []
        self.b_value = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '+', '-', '/', '*', 'C', '=']
        self.input = '0'
        self.value = ['0','0']
        self.stage = 0
        self.action = None
        self.renderCalculatorInput()

        for i in range(len(self.b_value)):
            self.buttons.append(Button(self.CalculatorScreen, text=self.b_value[i], command=lambda a = self.b_value[i]: self.numOnClick(a)))
            self.buttons[-1].grid(row=i//4+1, column=i%4)
            # self.buttons[-1].pack()

            
    def numOnClick(self, value):
        print(self.stage)
        if str(value) in '0123456789':
            if self.value[self.stage] == '0':
                self.value[self.stage] = str(value)
            else:
                self.value[self.stage] += str(value)
        elif str(value) == '.' and  '.' not in self.value[self.stage]:
            self.value[self.stage] += str(value)

        elif str(value) == 'C':
            self.value = ['0','0']
            self.stage = 0

        elif str(value) in '-+/*':
            print('!')
            if self.stage == 0:
                self.stage+=1
                self.action = str(value)

        elif str(value) == '=':
            if self.stage == 1:
                if self.value[1] != '0':
                    self.value[1] = eval(self.value[0] + self.action + self.value[1])
                else:
                    self.value[1] = 'ERROR'
            
        self.renderCalculatorInput()
    
    def renderCalculatorInput(self):
        try: self.title.destroy() 
        except: pass
        self.title = Label(self.CalculatorScreen, text=self.value[self.stage])
        self.title.grid(row = 0, columnspan=4)


    def exitCalculator(self):
        # self.CalculatorScreen.destroy()
        self.window.destroy()

        