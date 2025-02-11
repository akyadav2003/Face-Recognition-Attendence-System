from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        title_lbl=Label(self.root,bd=2,relief=RIDGE,text="DEVELOPER",font=("times new roman",35,"bold"),bg="yellow",fg="red")
        title_lbl.place(x=0,y=0,width=1530,heigh=50)

        bg_img = Image.open(r"college_images\dev.jpg")
        bg_img = bg_img.resize((1530,750))
        self.photobg_img = ImageTk.PhotoImage(bg_img)

        f_lbl = Label(self.root, image=self.photobg_img)
        f_lbl.place(x=0, y=50, width=1530, height=750)

        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1020,y=5,width=500,height=600)


        bg_img1 = Image.open(r"college_images\tony.jpg")
        bg_img1 = bg_img1.resize((200,200))
        self.photobg_img1 = ImageTk.PhotoImage(bg_img1)

        f_lbl = Label(main_frame,image=self.photobg_img1)
        f_lbl.place(x=293, y=3, width=200, height=200)

        dev_lbl=Label(main_frame,text="Hello my name is Tony",font=("times new roman",13,"bold"),bg="white",fg="black")
        dev_lbl.place(x=0,y=3)

        dev_lbl=Label(main_frame,text="I am full stack developer",font=("times new roman",13,"bold"),bg="white",fg="black")
        dev_lbl.place(x=0,y=30)

        bg_img2 = Image.open(r"college_images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        bg_img2 = bg_img2.resize((1530,750))
        self.photobg_img2 = ImageTk.PhotoImage(bg_img2)

        f_lbl = Label(main_frame, image=self.photobg_img2)
        f_lbl.place(x=0, y=205, width=496, height=391)




if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()