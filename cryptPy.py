from tkinter import *
from tkinter import messagebox
import base64
import os

def main_screen():
        screen=Tk()
        screen.geometry("375x398")

        #icon
        image_icon=PhotoImage(file="keys.png")
        screen.iconphoto(False,image_icon)
        screen.title("PctApp")
        
        Label(text="Enter text for encryption", fg="black",font=("calbri,13")).place(x=10,y=10)
        
        screen.mainloop()

main_screen()      