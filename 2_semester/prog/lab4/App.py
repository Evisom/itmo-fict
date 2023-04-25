from tkinter import * 
from StartScreen import StartScreen


class App(StartScreen):
    def __init__ (self, resolution='500x500'):
        self.window = Tk()
        self.window.geometry(resolution)
        self.menu = Menu(self.window, tearoff=0)
        
        self.menu_file = Menu(self.menu)
        self.menu_file.add_command(label='Exit', command=exit)
        self.window.config(menu=self.menu)
        self.renderStartScreen(self.window)
        self.window.config(menu=self.menu)

        self.window.mainloop()

    def exit(self):
        self.window.destroy()

