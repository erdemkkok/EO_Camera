# import everything from tkinter module
from tkinter import *   
import os
import csv 
import time
from tracemalloc import start
from xml.dom.pulldom import START_DOCUMENT
from tkinter import filedialog, ttk
import pandas as pd
from PIL import ImageTk, Image


root = Tk()   
root.geometry('1080x720')          
labelframe1 = LabelFrame(root, text="Control Panel")  
labelframe1.pack(fill="both", expand="yes")  
xa=10101010
button1 = Button(root, text="Browse A File", command=lambda: koordinat())
button1.place(rely=0.85, relx=0.50)
frame = Frame(root, width=400, height=200)
img = ImageTk.PhotoImage(Image.open("resultt.png"))

def click_button():
    os.system('python3 detect.py --source EO.mp4')
    return True
def koordinat():
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    # Create an object of tkinter ImageTk


    label = Label(frame, image = img)
    label.pack()
    with open("koordinat.csv", "r") as f:


        # Create a Label Widget to display the text or Image

        reader = csv.reader(f, delimiter="\t")  
        for i, line in enumerate(reader):
            print (line)

        
    return True


while True:
    root.update()
    #click_button()