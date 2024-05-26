from tkinter import *
from app_setting import * 
from os import *

class App():


    def __init__(self):
        self.window = Tk()
        self.window.geometry(str(w_width) + "x" + str(w_height))
        self.window.title(app_title)

        self.top_frame = Frame(background='#F9F9F9', width=w_width, height=500)
        self.top_frame.pack()

        self.main_frame = Frame(background=bg_color, width=w_width, height=(w_height-700))
        self.main_frame.pack()

        self.bottom_frame = Frame(background='white', width=w_width, height=200)
        self.bottom_frame.pack(side="bottom")

        self.home_button = Button(self.main_frame, test="Start", height=100, width=200, bg="#7899D4", command=exit)
        #change command from exit to next page
        self.home_button.place(x=50, y=100)


        self.dirname = path.dirname(__file__)
        self.filename = path.join(self.dirname, 'image/')

        self.window.mainloop()

    
    def exit(self):
        self.window.destroy()





