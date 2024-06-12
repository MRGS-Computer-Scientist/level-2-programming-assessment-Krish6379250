from tkinter import *
from app_setting import * 
from os import *


class App():

    current_frame= "home"




    def __init__(self):
        self.window = Tk()
        self.window.geometry("600x1000")
        self.window.title(app_title)

        ###################### HOME TOP FRAME ##########################

        
        self.headline = Label( text="Navigating App", font=("Arial",30), bg="#F9F9F9")
        self.headline.place(x=300, y=0)

        #################### HOME FRAME ############################

        self.home_frame = Frame(background=bg_color, width=600, height=1000)
        self.home_frame.pack()
        
        self.home_button = Button(self.home_frame, text="Start", height=10, width=75, bg="#7899D4",
                                   command=lambda: self.go_to_frame("map"))
        #change command from exit to next page later
        self.home_button.place(x=0, y=400)


        self.window.mainloop()

    ################################### DEF ###################################
    ################# If the start button is pressed ##################
    def go_to_frame(self, next_frame):
        if self.current_frame == "home":
            self.home_frame.pack_forget()
        if self.current_frame == "home":
            self.home_button.destroy()
        if self.current_frame == "home":


         if next_frame =="map":
           self.current_frame="map"
        






    #............... From Start Page to Main Page ..................



        
    #............................. DEF ...............................











