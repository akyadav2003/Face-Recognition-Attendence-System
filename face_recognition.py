from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,relief=RIDGE, text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="yellow",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=50)

        img_top = Image.open(r"college_images\face_detector1.jpg")
        img_top=img_top.resize((850,740))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=850, height=740)

        img_top1 = Image.open(r"college_images\face_reco.jpg")
        img_top1=img_top1.resize((680,740))
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(self.root, image=self.photoimg_top1)
        f_lbl.place(x=853,y=50,width=680,height=740)


        b=Button(self.root,text="Face Detector",command=self.face_recog,cursor="hand2",font=("times new roman",17,"bold"),bg="white",fg="black")
        b.place(x=1015,y=710,width=370,height=40)

#==================Attendence================
    def mark_attendence(self,s,r,n,d):
        with open("ankit.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split(",")
                name_list.append(entry[0])
            if((s not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{s},{r},{n},{d},{dtString},{d1},present")



#==============Recognition function=================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+h])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="MySQL@2003",database="face_reco_sys")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id ="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id ="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_id ="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_id from student where Student_id ="+str(id))
                s=my_cursor.fetchone()
                s="+".join(s)

                if confidence>77:
                    cv2.putText(img,f"ID: {s}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),2)
                    cv2.putText(img,f"Roll: {r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),2)
                    cv2.putText(img,f"Name: {n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),2)
                    cv2.putText(img,f"Department: {d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),2)
                    self.mark_attendence(s,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),2)
                
                coord=[x,y,w,h]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
    
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret, img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()