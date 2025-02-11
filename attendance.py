from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        self.var_attend_id=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendance=StringVar()
        

#First img
        img = Image.open(r"college_images\smart-attendance.jpg")
        img = img.resize((750,153))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=10, y=0, width=750, height=153)
#Secound img
        img1 = Image.open(r"college_images\iStock-182059956_18390_t12.jpg")
        img1 = img1.resize((750,153))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=765, y=0, width=750, height=153)


#Bg image
        img3 = Image.open(r"college_images\un.jpg")
        img3 = img3.resize((1530,710))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=153, width=1530, height=710)

        title_lbl=Label(self.root,bd=2,relief=RIDGE,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="yellow",fg="red")
        title_lbl.place(x=5,y=157,width=1520,heigh=50)

#Left label fram
        left_frame=LabelFrame(bg_img,bd=2,relief=RIDGE,text="STUDENT INFORMATION",font=("times new roman",12,"bold"))
        left_frame.place(x=3,y=55,width=721,heigh=575)

        img_left = Image.open(r"college_images\hqdefault.jpg")
        img_left = img_left.resize((712,180))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=1, y=3, width=712, height=180)

#Attendence id
        left1_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="STUDENT INFORMATION",font=("times new roman",12,"bold"))
        left1_frame.place(x=3,y=185,width=711,heigh=270)

        
        attendanceId_label=Label(left1_frame, text="STUDENT ID:",font=("times new roman",12,"bold"),bg="yellow",fg="red")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=15,sticky=W)

        attendanceId_entry=ttk.Entry(left1_frame,textvariable=self.var_attend_id,width=19,font=("times new roman",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=15,sticky=W)

#Roll No
        
        rollLabel=Label(left1_frame, text="ROLL NO:",font=("times new roman",12,"bold"),bg="yellow",fg="red")
        rollLabel.grid(row=0,column=2,padx=10,pady=15,sticky=W)

        atten_roll=ttk.Entry(left1_frame,textvariable=self.var_attend_roll,width=19,font=("times new roman",12,"bold"))
        atten_roll.grid(row=0,column=3,padx=10,pady=15,sticky=W)

#Name
        
        NameLabel=Label(left1_frame, text="NAME:",font=("times new roman",12,"bold"),bg="yellow",fg="red")
        NameLabel.grid(row=1,column=0,padx=10,pady=15,sticky=W)

        atten_name=ttk.Entry(left1_frame,textvariable=self.var_attend_name,width=19,font=("times new roman",12,"bold"))
        atten_name.grid(row=1,column=1,padx=10,pady=15,stick=W)
        
        depLabel=Label(left1_frame, text="DEPARTMENT:",font=("times new roman",12,"bold"),bg="yellow",fg="red")
        depLabel.grid(row=1,column=2,padx=10,pady=15,sticky=W)

        atten_dep=ttk.Entry(left1_frame,textvariable=self.var_attend_dep,width=19,font=("times new roman",12,"bold"))
        atten_dep.grid(row=1,column=3,padx=10,pady=15,sticky=W)

#Time
        
        timeLabel=Label(left1_frame, text="TIME:",font=("times new roman",12,"bold"),bg="yellow",fg="red")
        timeLabel.grid(row=2,column=0,padx=10,pady=15,sticky=W)

        atten_time=ttk.Entry(left1_frame,textvariable=self.var_attend_time,width=19,font=("times new roman",12,"bold"))
        atten_time.grid(row=2,column=1,padx=10,pady=15,sticky=W)

#Date
        
        dateLabel=Label(left1_frame, text="DATE:",font=("times new roman",12,"bold"),bg="yellow",fg="red")
        dateLabel.grid(row=2,column=2,padx=10,pady=15,sticky=W)

        atten_date=ttk.Entry(left1_frame,textvariable=self.var_attend_date,width=19,font=("times new roman",12,"bold"))
        atten_date.grid(row=2,column=3,padx=10,pady=15,sticky=W)

#Attendance Status

        attendanceLabel=Label(left1_frame, text="ATTENDENCE STATUS:",font=("times new roman",12,"bold"),bg="yellow",fg="red")
        attendanceLabel.grid(row=3,column=0,padx=10,sticky=W)

        self.atten_status=ttk.Combobox(left1_frame,textvariable=self.var_attend_attendance,font=("times new roman",12,"bold"),width=20,state="readonly")
        self.atten_status["values"]=("Select Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,padx=2,pady=15,sticky=W)

#Button      
        btn_frame=Frame(left_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=3,y=470,width=711,heigh=80) 

        import_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=19,font=("times new roman",12,"bold"),bg="purple",fg="white")
        import_btn.grid(row=0,column=0,padx=0)

        export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=19,font=("times new roman",12,"bold"),bg="purple",fg="white")
        export_btn.grid(row=0,column=1,padx=1)

        update_btn=Button(btn_frame,text="Update",width=19,font=("times new roman",12,"bold"),bg="purple",fg="white")
        update_btn.grid(row=0,column=2,padx=0)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",12,"bold"),bg="purple",fg="white")
        reset_btn.grid(row=0,column=3,padx=1)  



#Right label fram
        Right_frame=LabelFrame(bg_img,bd=2,relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        Right_frame.place(x=730,y=55,width=790,heigh=575) 

#  =================Table====================  
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=5,width=775,heigh=455)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll No.")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendence Status")
        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)              

#================fetch data===================
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)    

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found To Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("csv File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Dta Export","Your Data Exported to"+os.path.basename(fln)+"Successfully")
        except Exception as es:
            messagebox.showinfo("Error",f"Due To :{str(es)}",parent=self.root)            

    def get_cursor(self,event=""):
         cursor_row=self.AttendanceReportTable.focus()
         content=self.AttendanceReportTable.item(cursor_row)
         rows=content['values']

         self.var_attend_id.set(rows[0])
         self.var_attend_roll.set(rows[1])
         self.var_attend_name.set(rows[2])
         self.var_attend_dep.set(rows[3])
         self.var_attend_time.set(rows[4])
         self.var_attend_date.set(rows[5])
         self.var_attend_attendance.set(rows[6])
         
    def reset_data(self):
         self.var_attend_id.set("")
         self.var_attend_roll.set("")
         self.var_attend_name.set("")
         self.var_attend_dep.set("")
         self.var_attend_time.set("")
         self.var_attend_date.set("")
         self.var_attend_attendance.set("")









if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()