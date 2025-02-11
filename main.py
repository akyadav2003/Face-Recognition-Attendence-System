from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from student import Student
import os
from train_data import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help 
from time import strftime
from datetime import datetime

class face_recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
   
#First img
        img = Image.open(r"college_images\Stanford.jpg")
        img = img.resize((500,130))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=10, y=0, width=500, height=130)
#Secound img
        img1 = Image.open(r"college_images\facialrecognition.png")
        img1 = img1.resize((500,130))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=515, y=0, width=500, height=130)
#Third img
        img2 = Image.open(r"college_images\u.jpg")
        img2 = img2.resize((500,130))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1020, y=0, width=500, height=130)

#Bg image
        img3 = Image.open(r"college_images\wp2551980.jpg")
        img3 = img3.resize((1530,710))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl=Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",34,"bold"),bg="yellow",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

#==================time===================
        def time():
                string = strftime('%H:%M:%S %p')
                lbl.config(text= string)
                lbl.after(1000,time)
        lbl= Label(title_lbl,font =('time new roman',14,'bold'),background='yellow',foreground='black')
        lbl.place(x=3,y=0,width=120,heigh=45)
        time()   


# Student Button
        img4 = Image.open(r"college_images\AdobeStock_303989091.jpeg")
        img4 = img4.resize((220,220))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=70,width=220,height=220)

        b1_1=Button(bg_img,text="STUDENT DETAILS",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=200,y=270,width=220,height=40)


# Detect face Button
        img5 = Image.open(r"college_images\face_detector1.jpg")
        img5 = img5.resize((220,220))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.face_data,cursor="hand2")
        b1.place(x=500,y=70,width=220,height=220)

        b1_1=Button(bg_img,text="FACE DETECTOR",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=500,y=270,width=220,height=40)


# Attendence Button
        img6 = Image.open(r"college_images\report.jpg")
        img6 = img6.resize((220,220))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,command=self.attendance_data, cursor="hand2")
        b1.place(x=800,y=70,width=220,height=220)

        b1_1=Button(bg_img,text="ATTENDENCE",command=self.attendance_data, cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=800,y=270,width=220,height=40)

# Help Button
        img7 = Image.open(r"college_images\chat.jpg")
        img7 = img7.resize((220,220))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,command=self.help_data, cursor="hand2")
        b1.place(x=1100,y=70,width=220,height=220)

        b1_1=Button(bg_img,text="HELP DESK",command=self.help_data ,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=1100,y=270,width=220,height=40)


# Train data Button
        img8 = Image.open(r"college_images\facialrecognition (1).png")
        img8 = img8.resize((220,220))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,command=self.train_data, cursor="hand2")
        b1.place(x=200,y=350,width=220,height=220)

        b1_1=Button(bg_img,text="TRAIN DATA",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=200,y=570,width=220,height=40)


# Photo Button
        img9 = Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        img9 = img4.resize((220,220))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,command=self.open_img,cursor="hand2")
        b1.place(x=500,y=350,width=220,height=220)

        b1_1=Button(bg_img,text="PHOTO",command=self.open_img, cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=500,y=570,width=220,height=40)

 # Developer Button
        img10 = Image.open(r"college_images\gettyimages-1022573162.jpg")
        img10 = img10.resize((220,220))
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,command=self.developer_data, cursor="hand2")
        b1.place(x=800,y=350,width=220,height=220)

        b1_1=Button(bg_img,text="DEVELOPER", cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=800,y=570,width=220,height=40)

 # Exit Button
        img11 = Image.open(r"college_images\exit.jpg")
        img11 = img11.resize((220,220))
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,command=self.Exit, cursor="hand2")
        b1.place(x=1100,y=350,width=220,height=220)

        b1_1=Button(bg_img,text="EXIT", cursor="hand2",command=self.Exit,font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=1100,y=570,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    def Exit(self):
         self.Exit = messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
         if self.Exit >0:
            self.root.destroy()
         else:
              return
            

# ==================Function Buttons=================

    def student_details(self):
         self.new_window=Toplevel(self.root)
         self.app=Student(self.new_window)

    def train_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Train(self.new_window)

    def face_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Attendance(self.new_window)

    def developer_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Developer(self.new_window)

    def help_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Help(self.new_window)         
         






if __name__ == "__main__":
    root = Tk()
    obj = face_recognition_system(root)
    root.mainloop()