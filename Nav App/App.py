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

        self.home_frame = Frame(background=bg_color, width=w_width, height=(w_height-200))
        
        self.home_frame.pack()
        
        self.home_button = Button(self.home_frame, text="Start", height=10, width=75, bg="#7899D4",
                                   command=lambda: self.go_to_frame("map") and self.show_frame)
        #change command from exit to next page later
        self.home_button.place(x=30, y=400)
        ######################## MAP/NEW PAGE ##############################

        ####################### TOP HALF ##############################

        self.top_left_frame= Frame( background="Red", width=300, height=500)
        self.top_left_frame.place_forget()

        self.top_right_frame = Frame( background="Blue", width=300, height=500)
        self.top_right_frame.place_forget()


         ######################### BOTTOM HALF ######################################






        ######################## HOME BOTTOM FRAME ##########################

        self.bottom_frame = Frame(background='#F9F9F9', width=w_width, height=300)
        self.bottom_frame.pack(side="bottom")

        ###################### OTHERS #####################################
        self.dirname = path.dirname(__file__)
        self.filename = path.join(self.dirname, 'image/')

        self.window.mainloop()

    ################################### DEF ###################################

    ################# If the start button is pressed ##################
    def go_to_frame(self, next_frame):
        if self.current_frame == "home":
            self.home_frame.pack_forget()
        if self.current_frame == "home":
            self.top_frame.pack_forget()
        if self.current_frame == "home":
            self.bottom_frame.pack_forget()
        if self.current_frame == "home":
            self.home_button.destroy()
        
        if next_frame =="map":
            self.current_frame="map"



    #............... From Start Page to Main Page ..................

    def show_frame(self):
        self.top_left_frame.place(x=0, y=0)
        self.top_right_frame.place(x=450, y=0)

        
    #............................. DEF ...............................











