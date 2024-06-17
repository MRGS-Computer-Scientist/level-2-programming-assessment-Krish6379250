from tkinter import *
from app_setting import * 
from os import *


class App():

    current_frame= "home"




    def __init__(self):
        self.window = Tk()
        self.window.geometry("600x1000")
        self.window.title(app_title)
        #################### HOME FRAME ############################

        self.home_frame = Frame(background=bg_color, width=600, height=1000)
        self.home_frame.pack()

        self.headline = Label( self.home_frame ,text="Navigating App", font=("Arial",30), bg="#F9F9F9")
        self.headline.place(x=175, y=0)
        
        self.home_button = Button(self.home_frame, text="Start", height=10, width=75, bg="#7899D4",
                                   command=lambda: self.go_to_frame("map"))
        self.home_button.place(x=35, y=400)
        ######################## New Page ################################
        ########################## 4 Corners #######################################
        self.top_left_frame = Frame(background="white", width=300, height=500)
        self.top_right_frame = Frame(background="white", width=300, height=500)
        self.bottom_left_frame = Frame(background="white", width=300, height=500)
        self.bottom_right_frame = Frame(background="white", width=300, height=500)

        ####################### Center Button #################################
        self.map_button = Button(text= "Map", height=5, width=10,  bg="#7899D4")

        ######################## Location #################################

        self.location_frame = Frame(background="#DDE1E4", width=250, height=470)

        #####################Desination ##################################

        self.destination_frame = Frame(background="#DDE1E4", width=250, height=470)

        ################################# Direction ############################

        self.direction_frame = Frame(background="#DDE1E4", width=250, height=470)

        ############################### Info ####################################

        self.info_frame = Frame(background="#DDE1E4", width=250, height=470)








        self.window.mainloop()

    ################################### DEF ###################################
    ################# If the start button is pressed ##################
    def go_to_frame(self, next_frame):
        if self.current_frame == "home":
            self.home_frame.pack_forget()
        if self.current_frame == "home":
            self.home_button.destroy()
        if self.current_frame == "home":
           self.top_left_frame.place(x=0, y=0)
           self.top_right_frame.place(x=300,y=0)
           self.bottom_left_frame.place(x=0, y=500)
           self.bottom_right_frame.place(x=300, y=500)
           self.map_button.place(x=260, y=450)
           self.location_frame.place(x=5, y=5)
           self.destination_frame.place(x=345, y=5)
           self.direction_frame.place(x=5, y=500)
           self.info_frame.place(x=345, y=500)
        if self.current_frame == "home":
         
 

         if next_frame =="map":
           self.current_frame="map"
        






    #............... From Start Page to Main Page ..................



        
    #............................. DEF ...............................











