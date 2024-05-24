from tkinter import*
from app_setting import *
from os import*


window = Tk()
window.geometry(str(w_width) + "x" + str(w_height))


top_frame = Frame(background='#F9F9F9', width=w_width, height=500)
top_frame.pack()

main_frame = Frame(background=bg_color, width=w_width, height=(w_height-700))
main_frame.pack()

bottom_frame = Frame(background='white', width=w_width, height=200)
bottom_frame.pack(side="bottom")


home_button = Button(main_frame, text="Start", height=20)

dirname = path.dirname(__file__)
filename = path.join(dirname, 'image/')

window.mainloop()

