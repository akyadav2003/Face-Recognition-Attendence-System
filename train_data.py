from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root, text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="yellow",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top = Image.open(r"college_images\facial_recognition_action.jpg")
        img_top=img_top.resize((1530,325))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=1530, height=325)

        #Button
        b=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="purple",fg="white")
        b.place(x=13,y=370,width=1500,height=60)

        img_top1 = Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        img_top1=img_top1.resize((1500,325))
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(self.root, image=self.photoimg_top1)
        f_lbl.place(x=13, y=440, width=1500, height=325)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  #Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #=================Train the classifier and save===============
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!!",parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()