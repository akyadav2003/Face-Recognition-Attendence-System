from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        title_lbl=Label(self.root,bd=2,relief=RIDGE,text="HELP DESK",font=("times new roman",35,"bold"),bg="yellow",fg="red")
        title_lbl.place(x=0,y=0,width=1530,heigh=50)

        bg_img = Image.open(r"college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpEG")
        bg_img = bg_img.resize((1530,750))
        self.photobg_img = ImageTk.PhotoImage(bg_img)

        f_lbl = Label(self.root, image=self.photobg_img)
        f_lbl.place(x=0, y=50, width=1530, height=750)

        dev_lbl=Label(f_lbl,text="Email:codewithkiran@gmail.com",font=("times new roman",20,"bold"),bg="white",fg="black")
        dev_lbl.place(x=550,y=200)




if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()