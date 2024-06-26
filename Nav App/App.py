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
        self.location_headline = Label(self.location_frame, text="Location", font=("Ubuntu",25), bg="#DDE1E4")

        self.location_button_frame= Frame(background="#F4F4F8", width=240, height=410)

        self.location_office_button= Button(self.location_button_frame, text="Office", width=30, height=1, bg="#7899D4", command=self.multiple_location_office)
        self.location_deans_button= Button(self.location_button_frame, text="Deans", width=30, height=1, bg="#7899D4", command=self.multiple_location_deans)
        self.location_hall_button= Button(self.location_button_frame, text="Hall", width=30, height=1, bg="#7899D4", command=self.multiple_location_hall)
        self.location_gyms_button= Button(self.location_button_frame, text="Gyms", width=30, height=1, bg="#7899D4", command=self.multiple_location_gyms)

        self.location_select_frame = Frame(background="#DDE1E4", width=230, height=40)
        self.location_select_text = Label(self.location_select_frame ,background="#DDE1E4", text="Selected :", font=("Ubuntu",20))

        self.location_select_office = Label(self.location_select_frame ,background="#DDE1E4", text="Office", font=("Ubuntu",20))
        self.location_select_deans = Label(self.location_select_frame ,background="#DDE1E4", text=" Deans", font=("Ubuntu",20))
        self.location_select_gyms = Label(self.location_select_frame ,background="#DDE1E4", text=" Gyms", font=("Ubuntu",20))
        self.location_select_hall = Label(self.location_select_frame ,background="#DDE1E4", text="Hall", font=("Ubuntu",20))

        #####################Desination ##################################

        self.destination_frame = Frame(background="#DDE1E4", width=250, height=470)
        self.destination_headline = Label(self.destination_frame, text="Desination", font=("Ubuntu",25), bg="#DDE1E4")

        self.destination_button_frame= Frame(background="#F4F4F8", width=240, height=410)

        self.destination_office_button= Button(self.destination_button_frame, text="Office", width=30, height=1, bg="#7899D4", command=self.multiple_destination_office)
        self.destination_deans_button= Button(self.destination_button_frame, text="Deans", width=30, height=1, bg="#7899D4", command=self.multiple_destination_deans)
        self.destination_hall_button= Button(self.destination_button_frame, text="Hall", width=30, height=1, bg="#7899D4", command=self.multiple_destination_hall)
        self.destination_gyms_button= Button(self.destination_button_frame, text="Gyms", width=30, height=1, bg="#7899D4", command=self.multiple_destination_gyms)

        self.destination_select_frame = Frame(background="#DDE1E4", width=230, height=40)
        self.destination_select_text = Label(self.destination_select_frame ,background="#DDE1E4", text="Selected :", font=("Ubuntu",20))

        self.destination_select_office = Label(self.destination_select_frame ,background="#DDE1E4", text="Office", font=("Ubuntu",20))
        self.destination_select_deans = Label(self.destination_select_frame ,background="#DDE1E4", text=" Deans", font=("Ubuntu",20))
        self.destination_select_gyms = Label(self.destination_select_frame ,background="#DDE1E4", text=" Gyms", font=("Ubuntu",20))
        self.destination_select_hall = Label(self.destination_select_frame ,background="#DDE1E4", text="Hall", font=("Ubuntu",20))


        ################################# Direction ############################

        self.direction_frame = Frame(background="#DDE1E4", width=250, height=470)
        self.direction_headline = Label(self.direction_frame, text="Direction", font=("Ubuntu",25), bg="#DDE1E4")

        self.direction_text_frame= Frame(background="#F4F4F8", width=240, height=410)

        self.location_variable = StringVar()

        self.destination_variable = StringVar()
        ###################### ALL 12 LABEL DIRECTIONS ######################
        self.direction_office_deans = Label(self.direction_text_frame, text="When entering through the office, once you walk past the receptionist, take a left then your destination would be straight ahead", font=("Ubuntu",25), bg="#DDE1E4") #1

        self.direction_office_gyms = Label(self.direction_text_frame, text="When entering through the office, walk straight ahead to the exit, once you're out continue ahead along with A block, once you made it to the end turn left, there you will see a parking lot, instead of going there turn right where the field is, after that turn left and the gyms should be in that direction  ", font=("Ubuntu",25), bg="#DDE1E4") #2

        self.direction_office_hall = Label(self.direction_text_frame, text="When entering through the office, walk straight ahead to the exit, once you're out continue ahead along with A block, once you made it to the end turn left, there you will see a parking lot at which the hall would be the bigger building infront of the car pack.", font=("Ubuntu",25), bg="#DDE1E4") #3

        self.direction_deans_office = Label(self.direction_text_frame, text="When you're at the entrance to the deans just walk straight ahead into the next building, then you are in the office", font=("Ubuntu",25), bg="#DDE1E4") #4

        self.direction_deans_gyms = Label(self.direction_text_frame, text="When you're at the entrance to the deans, take a left then turn right straight after, next take a left but don't go inside A block, Walk straight along A block until you make it to the end there turn left, there you will see a parking lot, instead of going there turn right where the field is, after that turn left and the gyms should be in that direction", font=("Ubuntu",25), bg="#DDE1E4") #5

        self.direction_deans_hall = Label(self.direction_text_frame, text="When you're at the entrance to the deans, take a left then turn right straight after, next take a left but don't go inside A block, Walk straight along A block until you make it to the end, at the end turn left, there you will see a parking lot at which the hall would be the bigger building infront of the car pack. ", font=("Ubuntu",25), bg="#DDE1E4") #6

        self.direction_gyms_office = Label(self.direction_text_frame, text="Starting from the entrance to Gym 3, walk straight ahead where the field should be, follow the concrete path until there is a right turn, there you will se a parking lot, you should see the hall a big building in front of the parking lot, on the left of the hall there will be little steps leading to the quad, once in the quad walk straight until you reach E block, turn left then take the first right, the deans should be on your left", font=("Ubuntu",25), bg="#DDE1E4") #7

        self.direction_gyms_deans = Label(self.direction_text_frame, text="Starting from the entrance to Gym 3, walk straight ahead where the field should be, follow the concrete path until there is a right turn, there you will se a parking lot, you should see the hall a big building in front of the parking lot, on the left of the hall there will be little steps leading to the quad, once in the quad walk straight until you reach E block, turn left then take the first right, the deans should be on your right", font=("Ubuntu",25), bg="#DDE1E4") #8

        self.direction_gyms_hall = Label(self.direction_text_frame, text="Starting from the entrance to Gym 3, walk straight ahead where the field should be, follow the concrete path until there is a right turn, there you will see a parking lot, there you will see the hall the big building in front the parking lot.", font=("Ubuntu",25), bg="#DDE1E4") #9

        self.direction_hall_office = Label(self.direction_text_frame, text="From the entrance take the first right into the quad, once there walk forwards until you reach it to E block, turn left then take the first right, the office should be on your left", font=("Ubuntu",25), bg="#DDE1E4") #10

        self.direction_hall_deans = Label(self.direction_text_frame, text="From the entrance take the first right into the quad, once there walk forwards until you reach it to E block, turn left then take the first right, the deans should be on your right", font=("Ubuntu",25), bg="#DDE1E4") #11

        self.direction_hall_gyms = Label(self.direction_text_frame, text="From the entrance take the first left at where the field should be, turn left then walk straight ahead until you reach the gyms", font=("Ubuntu",25), bg="#DDE1E4") #12
        ##################### all 12 if statements for directions ############################
        if self.location_variable == "office" and self.destination_variable == "deans": #1
           self.direction_office_deans.place(x=0, y=10)
         
        if self.location_variable == "office" and self.destination_variable == "gyms": #2
           self.direction_office_gyms.place(x=0,y=10)

        if self.location_variable == "office" and self.destination_variable == "hall": #3
           self.direction_office_hall.place(x=0, y=10)
         
        if self.location_variable == "deans" and self.destination_variable == "office": #4
           self.direction_deans_office.place(x=0, y=10)
         
        if self.location_variable == "deans" and self.destination_variable == "gyms": #5
           self.direction_deans_gyms.place(x=0, y=10)

        if self.location_variable == "deans" and self.destination_variable == "hall": #6
           self.direction_deans_hall.place(x=0, y=10)
           
        if self.location_variable == "gyms" and self.destination_variable == "office": #7
           self.direction_gyms_office.place(x=0, y=10)
         
        if self.location_variable == "gyms" and self.destination_variable == "deans": #8
           self.direction_gyms_deans.place(x=0, y=10)

        if self.location_variable == "gyms" and self.destination_variable == "hall": #9
           self.direction_gyms_hall.place(x=0, y=10)

        if self.location_variable == "hall" and self.destination_variable == "office": #10
           self.direction_hall_office.place(x=0, y=10)
         
        if self.location_variable == "hall" and self.destination_variable == "deans": #11
           self.direction_hall_deans.place(x=0, y=10)

        if self.location_variable == "hall" and self.destination_variable == "gyms": #12 
           self.direction_hall_gyms.place(x=0, y=10)

        ############################### Info ####################################

        self.info_frame = Frame(background="#DDE1E4", width=250, height=470)

        self.info_headline = Label(self.info_frame, text="Info", font=("Ubuntu",25), bg="#DDE1E4")

        self.info_button_frame= Frame(background="#F4F4F8", width=240, height=410)

        self.info_office_button= Button(self.info_button_frame, text="Office", width=30, height=1, bg="#7899D4",command=self.office_info )
        self.info_deans_button= Button(self.info_button_frame, text="Deans", width=30, height=1, bg="#7899D4", command=self.deans_info)
        self.info_hall_button= Button(self.info_button_frame, text="Hall", width=30, height=1, bg="#7899D4", command=self.hall_info)
        self.info_gyms_button= Button(self.info_button_frame, text="Gyms", width=30, height=1, bg="#7899D4", command=self.gyms_info)

        self.info_text_frame = Frame(self.info_button_frame ,background="#FDFFFC",width=230, height=275 )

        self.hall_info_text = Label(self.info_text_frame ,background="#FDFFFC" ,text="A large Assembly Hall with stage, sound and lighting equipment.", wraplength=230)

        self.deans_info_text = Label(self.info_text_frame, background="#FDFFFC", wraplength=230 ,text= """
The House system at Mount Roskill Grammar School comprises five houses – Hillary, Rutherford, Cooper, Ngata and Sheppard. Each house operates as a family, providing all students with an identity within the larger school.
Each House has is overseen by a team of three Deans and a member of the senior leadership team. These focus on pastoral and academic monitoring and support, supervise house activities and set expectations of student behaviour and habits of learning, provide support, welfare and guidance. House assemblies are held regularly and inter-house events are arranged during the year in activities such as volleyball, basketball, netball, athletics and swimming. Through their houses students are also encouraged to be of service to the wider community by fundraising for charities.
The Deans is where each house is put
""")
        
        self.office_info_text = Label(self.info_text_frame, background="#FDFFFC", wraplength=230, text="""
At MRGS the use of the office is to manage administrative duties, such as answering calls and correspondence, ordering supplies and handling information, they also are use in for helping students and parents.
""")
        self.gyms_info_text = Label(self.info_text_frame, background="#FDFFFC", wraplength=230, text="""
MRGS is fortunate to have great facilities for our students to enjoy. Three Gymnasium, field, turf and a swimming pool allow students to participate in a variety of activities in a comfortable environment.
The Department is well served with quality teachers. The HPE Staff are passionate about helping and encouraging all students, to reach their potential, acquire the knowledge that is needed for independent, critical thinkers and to  develop skills for lifelong learning.
""")
        









        self.window.mainloop()

    ################################### DEF ###################################
    ################# If the start button is pressed ##################
    def go_to_frame(self, next_frame):
        if self.current_frame == "home":
            self.home_frame.pack_forget()
        if self.current_frame == "home":
            self.home_button.destroy()
        if self.current_frame == "home":
           ############### 4 corners #######################
           self.top_left_frame.place(x=0, y=0)
           self.top_right_frame.place(x=300,y=0)
           self.bottom_left_frame.place(x=0, y=500)
           self.bottom_right_frame.place(x=300, y=500)
           ############### Map Button ################
           self.map_button.place(x=260, y=450)
           ############## 4 components ###################
           self.location_frame.place(x=5, y=5)
           self.destination_frame.place(x=345, y=5)
           self.direction_frame.place(x=5, y=500)
           self.info_frame.place(x=345, y=500)
           ################ 4 headlines ##################
           self.location_headline.place(x=60, y=5)
           self.destination_headline.place(x=60, y=5)
           self.direction_headline.place(x=60, y=5)
           self.info_headline.place(x=100, y=5)
           ############### component inner frames ##################
           self.location_button_frame.place(x=10, y=55)
           self.destination_button_frame.place(x=350, y=55)
           self.direction_text_frame.place(x=10, y=550)
           self.info_button_frame.place(x=350, y=550)
           self.info_text_frame.place(x=5, y=130)
           self.location_select_frame.place(x=15, y=200)
           self.location_select_text.place(x=1, y=0)
           self.destination_select_frame.place(x=355, y=200)
           self.destination_select_text.place(x=1, y=0)
           ####################### info buttons############################
           self.info_office_button.place(x=13, y=10)
           self.info_deans_button.place(x=13, y=40)
           self.info_hall_button.place(x=13, y=70)
           self.info_gyms_button.place(x=13, y=100)
           ##################### location buttons #########################
           self.location_office_button.place(x=13, y=10)
           self.location_deans_button.place(x=13, y=40)
           self.location_hall_button.place(x=13, y=70)
           self.location_gyms_button.place(x=13, y=100)
           ###################### destination buttons #########################
           self.destination_office_button.place(x=13, y=10)
           self.destination_deans_button.place(x=13, y=40)
           self.destination_hall_button.place(x=13, y=70)
           self.destination_gyms_button.place(x=13, y=100)

        if self.current_frame == "home":
         
 

         if next_frame =="map":
           self.current_frame="map"
        






    #............... From Start Page to Main Page ..................
    ################## def information place text #########################
    def hall_info(self):
       self.hall_info_text.place(x=13, y=5)

    def deans_info(self):
       self.deans_info_text.place(x=2, y=0)

    def office_info(self):
       self.office_info_text.place(x=2, y=0)
    
    def gyms_info(self):
       self.gyms_info_text.place(x=2, y=0)
############################ def information disappear text #################################
    def info_disappear_office(self):
       self.deans_info_text.place_forget()
       self.gyms_info_text.place_forget()
       self.hall_info_text.place_forget()
       
    def info_disappear_deans(self):
       self.office_info_text.place_forget()
       self.gyms_info_text.place_forget()
       self.hall_info_text.place_forget()
       
    def info_disappear_gyms(self):
       self.office_info_text.place_forget()
       self.deans_info_text.place_forget()
       self.hall_info_text.place_forget()
       
    def info_disappear_hall(self):
       self.office_info_text.place_forget()
       self.deans_info_text.place_forget()
       self.gyms_info_text.place_forget()

    ####################### def location selected text   #######################

    def selected_location_office(self):
       self.location_select_office.place(x=125, y=0)

    def selected_location_dean(self):
       self.location_select_deans.place(x=125, y=0)

    def selected_location_gyms(self):
       self.location_select_gyms.place(x=125, y=0)

    def selected_location_hall(self):
       self.location_select_hall.place(x=125, y=0)
       
   ######################### def destination selected text ###########################
    def selected_destination_office(self):
        self.destination_select_office.place(x=125, y=0)
      
    def selected_destination_dean(self):
       self.destination_select_deans.place(x=125, y=0)

    def selected_destination_gyms(self):
       self.destination_select_gyms.place(x=125, y=0)

    def selected_destination_hall(self):
       self.destination_select_hall.place(x=125, y=0)

   ###################### disappear labels location selected #######################

    def gone_location_office(self):
       self.location_select_deans.place_forget()
       self.location_select_gyms.place_forget()
       self.location_select_hall.place_forget()

    def gone_location_deans(self):
       self.location_select_office.place_forget()
       self.location_select_gyms.place_forget()
       self.location_select_hall.place_forget()

    def gone_location_gyms(self):
       self.location_select_office.place_forget()
       self.location_select_deans.place_forget()
       self.location_select_hall.place_forget()

    def gone_location_hall(self):
       self.location_select_deans.place_forget()
       self.location_select_gyms.place_forget()
       self.location_select_office.place_forget()

##########################   disappear labels destination selected    #################################
    def gone_destination_office(self):
       self.destination_select_deans.place_forget()
       self.destination_select_gyms.place_forget()
       self.destination_select_hall.place_forget()

    def gone_destination_deans(self):
       self.destination_select_office.place_forget()
       self.destination_select_gyms.place_forget()
       self.destination_select_hall.place_forget()

    def gone_destination_gyms(self):
       self.destination_select_office.place_forget()
       self.destination_select_deans.place_forget()
       self.destination_select_hall.place_forget()

    def gone_destination_hall(self):
       self.destination_select_deans.place_forget()
       self.destination_select_gyms.place_forget()
       self.destination_select_office.place_forget()

######################## disappear labels selected + def location selected text #########################
    def multiple_location_office(self):
       self.selected_location_office()
       self.gone_location_office()
       self.update_location_variable_office()

    def multiple_location_deans(self):
       self.selected_location_dean()
       self.gone_location_deans()
       self.update_location_variable_deans()

    def multiple_location_gyms(self):
       self.selected_location_gyms()
       self.gone_location_gyms()
       self.update_location_variable_gyms()

    def multiple_location_hall(self):
       self.selected_location_hall()
       self.gone_location_hall()
       self.update_location_variable_hall()

#################### disappear labels selected + def destination selected text ##########################

    def multiple_destination_office(self):
       self.selected_destination_office()
       self.gone_destination_office()
       self.update_destination_variable_office()

    def multiple_destination_deans(self):
       self.selected_destination_dean()
       self.gone_destination_deans()
       self.update_destination_variable_deans()

    def multiple_destination_gyms(self):
       self.selected_destination_gyms()
       self.gone_destination_gyms()
       self.update_destination_variable_gyms()

    def multiple_destination_hall(self):
       self.selected_destination_hall()
       self.gone_destination_hall()
       self.update_destination_variable_hall()
   ##################### direction def location ############################   

    def update_location_variable_office(self):
       self.location_variable = "office"
      
    def update_location_variable_deans(self):
       self.location_variable = "deans"

    def update_location_variable_gyms(self):
       self.location_variable = "gyms"

    def update_location_variable_hall(self):
       self.location_variable = "hall"
##################### direction def destination ########################
    def update_destination_variable_office(self):
       self.destination_variable = "office"
      
    def update_destination_variable_deans(self):
       self.destination_variable = "deans"

    def update_destination_variable_gyms(self):
       self.destination_variable = "gyms"

    def update_destination_variable_hall(self):
       self.destination_variable = "hall"


    #............................. DEF ...............................











