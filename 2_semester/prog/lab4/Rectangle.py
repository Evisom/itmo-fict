from tkinter import * 

class Rectangle():
    def renderRectangleScreen(self,window):
        self.window = window
        self.RectangleScreen = Frame(self.window)
        self.RectangleScreen.pack()
        self.wt = Label(self.RectangleScreen, text='Width: (< 400)').pack()
        self.w = Entry(self.RectangleScreen)
        self.w.pack()
        self.ht = Label(self.RectangleScreen, text= 'Height: (< 300)').pack()
        self.h = Entry(self.RectangleScreen)
        self.h.pack()
        self.btn = Button(self.RectangleScreen, text='Draw', command=self.draw).pack()
    def draw(self):
        print("!!!")
        
        try: self.canvas.destroy()
        except: pass 
        try:
            self.width = int(self.w.get())
            self.height = int(self.h.get())
        except: self.r = 'ERROR'
        if self.width not in range(0, 401) or self.height not in range(0, 301):
            self.r = 'ERROR'
        else:
            self.canvas = Canvas(self.RectangleScreen, width=400, height=300)
            self.canvas.pack()
            self.canvas.create_rectangle(0, 0, self.width, self.height, fill='red')
            self.s = self.width * self.height 
            self.p = self.width*2 + self.height*2
            self.r = 'S: ' + str(self.s) + '; P:' + str(self.p)
        try: self.r.destroy()
        except: pass 
        self.result = Label(self.RectangleScreen, text=self.r).pack()