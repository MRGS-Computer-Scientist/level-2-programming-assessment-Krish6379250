from tkinter import *
from app_setting import * 
from os import *

class App():


    def __init__(self):
        self.window = Tk()
        self.window.geometry(str(w_width) + "x" + str(w_height))
        self.window.title(app_title)

        

        self.top_frame = Frame(background='#F9F9F9', width=w_width, height=200)
        self.top_frame = Label(text="Navigating App") #work on this later
        self.top_frame.pack()

        self.main_frame = Frame(background=bg_color, width=w_width, height=600)
        self.main_frame.pack()

        self.bottom_frame = Frame(background='#F9F9F9', width=w_width, height=200)
        self.bottom_frame.pack(side="bottom")

        self.home_button = Button(self.main_frame, text="Start", height=10, width=75, bg="#7899D4", command=exit)
        #change command from exit to next page later
        self.home_button.place(x=30, y=400)


        self.dirname = path.dirname(__file__)
        self.filename = path.join(self.dirname, 'image/')

        self.window.mainloop()

    
    def exit(self):
        self.window.destroy()





