from tkinter import *
from app_setting import * 
from os import *


class App():

    current_frame= "home"


    def __init__(self):
        self.window = Tk()
        self.window.geometry(str(w_width) + "x" + str(w_height))
        self.window.title(app_title)

        ###################### HOME TOP FRAME ##########################

        self.top_frame = Frame(background='#F9F9F9', width=w_width, height=200)
        self.top_frame.pack()

        self.headline = Label(self.top_frame, text="Navigating App", font=("Arial",30), bg="#F9F9F9")
        self.headline.pack()

        #################### HOME FRAME ############################

        self.home_frame = Frame(background=bg_color, width=w_width, height=600)
        self.home_frame.pack()
        
        self.home_button = Button(self.home_frame, text="Start", height=10, width=75, bg="#7899D4", command=lambda: self.go_to_frame("map"))
        #change command from exit to next page later
        self.home_button.place(x=30, y=400)

        self.map_frame = Frame(background=bg_color, width=w_width, height=600)




        ######################## HOME BOTTOM FRAME ##########################

        self.bottom_frame = Frame(background='#F9F9F9', width=w_width, height=300)
        self.bottom_frame.pack(side="bottom")

        ###################### OTHERS #####################################
        self.dirname = path.dirname(__file__)
        self.filename = path.join(self.dirname, 'image/')

        self.window.mainloop()

    
    def exit(self):
        self.window.destroy()

    def go_to_frame(self, next_frame):
        if self.current_frame == "home":
            self.home_frame.pack_forget and self.top_frame.pack_forget()
        if next_frame =="map":
            self.current_frame="map"





