from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

 

#=====================variables==================

        self.var_dep=StringVar()
        self.var_Course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


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

        title_lbl=Label(bg_img, text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="yellow",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=7,y=48,width=1510,height=600)

#Left label fram
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        left_frame.place(x=25,y=10,width=725,heigh=580)

        img_left = Image.open(r"college_images\u.jpg")
        img_left = img_left.resize((710,130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=715, height=130)
#Current Course
        current_course_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="CURRENT COURSE INFORMATION",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=100,width=712,heigh=140)

#Department
        dep_lbl=Label(current_course_frame, text="DEPARTMENT:",font=("times new roman",12,"bold"),bg="yellow",fg="red")
        dep_lbl.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=20,state="readonly")
        dep_combo["values"]=("Select Department","CSE","IT","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=1,pady=10,sticky=W)

#Course
        course_lbl=Label(current_course_frame, text="COURSE:",font=("times new roman",12,"bold"),bg="yellow",fg="red")
        course_lbl.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Course,font=("times new roman",12,"bold"),width=20,state="readonly")
        course_combo["values"]=("Select Course","B.E","B.Tech.","Diploma")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

#Year
        year_lbl=Label(current_course_frame, text="YEAR:",font=("times new roman",12,"bold"),bg="yellow",fg="red")
        year_lbl.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=20,state="readonly")
        year_combo["values"]=("Select Year","First","Secound","Third","Fourth")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=20,sticky=W)

#Semester
        
        semester_lbl=Label(current_course_frame, text="SEMESTER:",font=("times new roman",12,"bold"),bg="yellow",fg="red")
        semester_lbl.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=20,state="readonly")
        semester_combo["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

#Class Student information
        class_student_info_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="CLASS STUDENT INFERMATION",font=("times new roman",12,"bold"))
        class_student_info_frame.place(x=5,y=245,width=712,heigh=307)

#Student ID
        
        student_id_lbl=Label(class_student_info_frame, text="STUDENT ID:",font=("times new roman",12,"bold"),bg="yellow",fg="red")
        student_id_lbl.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        student_id_entry=ttk.Entry(class_student_info_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        student_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

#Student name
        
        studentname_lbl=Label(class_student_info_frame, text="STUDENT NAME:",font=("times new roman",12,"bold"),bg="yellow",fg="red")
        studentname_lbl.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_student_info_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


#Class Divition
        
        classdiv_lbl=Label(class_student_info_frame, text="CLASS DIVISION:",font=("times new roman",12,"bold"),bg="yellow",fg="red")
        classdiv_lbl.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        classdiv_entry=ttk.Entry(class_student_info_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        classdiv_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)


#Roll no
        
        rollno_lbl=Label(class_student_info_frame, text="ROLL NO.:",font=("times new roman",12,"bold"),bg="yellow",fg="red")
        rollno_lbl.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        rollno_entry=ttk.Entry(class_student_info_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


#Gender
        
        gender_lbl=Label(class_student_info_frame, text="GENDER:",font=("times new roman",12,"bold"),bg="yellow",fg="red")
        gender_lbl.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        gender_combo=ttk.Combobox(class_student_info_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=18,state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

#DOB
        
        dob_lbl=Label(class_student_info_frame, text="DOB:",font=("times new roman",12,"bold"),bg="yellow",fg="red")
        dob_lbl.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_info_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


#Email
        
        email_lbl=Label(class_student_info_frame, text="E-MAIL:",font=("times new roman",12,"bold"),bg="yellow",fg="red")
        email_lbl.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_info_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


#Phone no
        
        phone_lbl=Label(class_student_info_frame, text="PHONE NO.:",font=("times new roman",12,"bold"),bg="yellow",fg="red")
        phone_lbl.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_info_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


#Adderess
        
        add_lbl=Label(class_student_info_frame, text="ADDERESS:",font=("times new roman",12,"bold"),bg="yellow",fg="red")
        add_lbl.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        add_entry=ttk.Entry(class_student_info_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        add_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


#Teacher Name
        
        teacher_name_lbl=Label(class_student_info_frame, text="TEACHER NAME:",font=("times new roman",12,"bold"),bg="yellow",fg="red")
        teacher_name_lbl.grid(row=4,column=2,padx=5,pady=10,sticky=W)

        teacher_name_entry=ttk.Entry(class_student_info_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_name_entry.grid(row=4,column=3,padx=10,pady=10,sticky=W)

#radio Button

        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_info_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0,pady=3)

        radiobtn2=ttk.Radiobutton(class_student_info_frame,variable=self.var_radio1,text="No Photo Sample",value="No ")
        radiobtn2.grid(row=6,column=1,pady=3)

#button frame 1

        btn_frame=Frame(class_student_info_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=4,y=213,width=700,heigh=33)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=18,font=("times new roman",12,"bold"),bg="purple",fg="white")
        save_btn.grid(row=0,column=0,padx=1)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=18,font=("times new roman",12,"bold"),bg="purple",fg="white")
        update_btn.grid(row=0,column=1,padx=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=18,font=("times new roman",12,"bold"),bg="purple",fg="white")
        delete_btn.grid(row=0,column=2,padx=1)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=18,font=("times new roman",12,"bold"),bg="purple",fg="white")
        reset_btn.grid(row=0,column=3,padx=1)

#button frame 2

        btn_frame2=Frame(class_student_info_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame2.place(x=4,y=248,width=700,heigh=32)

        take_photo_btn=Button(btn_frame2,command=self.generate_dataset,text="Take Photo Sample",width=38,font=("times new roman",12,"bold"),bg="purple",fg="white")
        take_photo_btn.grid(row=1,column=0)

        update_photo_btn=Button(btn_frame2,text="Update Photo Sample",width=38,font=("times new roman",12,"bold"),bg="purple",fg="white")
        update_photo_btn.grid(row=1,column=1,padx=1) 
        

#Right label fram
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        right_frame.place(x=755,y=10,width=725,heigh=580) 

        img_right = Image.open(r"C:\Users\ankit\OneDrive\Desktop\face_recogn_system\college_images\u.jpg")
        img_right = img_right.resize((710,130))
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=715, height=130)


#  =================Search System====================  

        search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="SEARCH SYSTEM",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=100,width=712,heigh=70)

        search_lbl=Label(search_frame, text="SEARCH BY:",font=("times new roman",12,"bold"),bg="yellow",fg="red")
        search_lbl.grid(row=0,column=0,padx=7,pady=10,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=20,state="readonly")
        search_combo["values"]=("Select meadium","Roll No.","Phone No.","Name")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=3,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=9,font=("times new roman",12,"bold"),bg="purple",fg="white")
        search_btn.grid(row=0,column=3,padx=5)

        ShowAll_btn=Button(search_frame,text="Show All",width=9,font=("times new roman",12,"bold"),bg="purple",fg="white")
        ShowAll_btn.grid(row=0,column=4,padx=5)

#  =================Table Frame====================  

        table_frame=Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=180,width=712,heigh=370)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("Dep","Course","Year","Sem.","ID","Name","Div.","roll","gender","DOB","Email","Phone","Address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem.",text="Semester")
        self.student_table.heading("ID",text="Student Id")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Div.",text="Division")
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Address",text="Adderess")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("Dep",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem.",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Div.",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


#===============function decration=======================

    def add_data(self):
                        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                         messagebox.showerror("Error","All fields are required",parent=self.root)
                        else:
                           try:
                                conn=mysql.connector.connect(host="localhost",username="root",password="MySQL@2003",database="face_reco_sys")
                                my_cursor=conn.cursor()
                                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                                        self.var_dep.get(),
                                                                                                                                        self.var_Course.get(),
                                                                                                                                        self.var_year.get(),
                                                                                                                                        self.var_semester.get(),
                                                                                                                                        self.var_std_id.get(),
                                                                                                                                        self.var_std_name.get(),
                                                                                                                                        self.var_div.get(),
                                                                                                                                        self.var_roll.get(),
                                                                                                                                        self.var_gender.get(),
                                                                                                                                        self.var_dob.get(),
                                                                                                                                        self.var_email.get(),
                                                                                                                                        self.var_phone.get(),
                                                                                                                                        self.var_address.get(),
                                                                                                                                        self.var_teacher.get(),
                                                                                                                                        self.var_radio1.get()
                                                                                                                                                                ))

                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("Success","Student details has been added Successfully!",parent=self.root)
                           except Exception as es:
                             messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                        
#==============fetch data=====================
    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="MySQL@2003",database="face_reco_sys")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from student")
         data=my_cursor.fetchall()

         if len(data)!=0:
              self.student_table.delete(*self.student_table.get_children())
              for i in data:
                   self.student_table.insert("",END,values=i)
              conn.commit()
              conn.close()

#=======================Get cursor===================
    def get_cursor(self,event=""):
         cursor_focus=self.student_table.focus()
         content=self.student_table.item(cursor_focus)
         data=content["values"]

         self.var_dep.set(data[0]),
         self.var_Course.set(data[1])
         self.var_year.set(data[2])
         self.var_semester.set(data[3])
         self.var_std_id.set(data[4])
         self.var_std_name.set(data[5])
         self.var_div.set(data[6])
         self.var_roll.set(data[7])
         self.var_gender.set(data[8])
         self.var_dob.set(data[9])
         self.var_email.set(data[10])
         self.var_phone.set(data[11])
         self.var_address.set(data[12])
         self.var_teacher.set(data[13])
         self.var_radio1.set(data[14])

  # Update function
    def update_data(self):
         if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                 messagebox.showerror("Error","All fields are required",parent=self.root)
         else:
                try:
                   Update=messagebox.askyesno("Update","Do you want to update student details",parent=self.root)
                   if Update>0:
                        conn=mysql.connector.connect(host="localhost",username="root",password="MySQL@2003",database="face_reco_sys")
                        my_cursor=conn.cursor()
                        my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                                        self.var_Course.get(),
                                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                                        self.var_std_id.get()
                                                                                                                                                                                                                
                                                                                                                                                                                                                                                 ))
                   else:
                        if not Update:
                             return
                   messagebox.showinfo("Success","Student details successfully updated!",parent=self.root)
                   conn.commit()
                   self.fetch_data()
                   conn.close()
                except Exception as es:
                       messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

 #==============Detete function===============
    def delete_data(self):
         if self.var_std_id.get()=="":
               messagebox.showerror("Error","Student must be required",parent=self.root)
         else:
              try:
                   delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student details",parent=self.root)
                   if delete>0:
                        conn=mysql.connector.connect(host="localhost",username="root",password="MySQL@2003",database="face_reco_sys")
                        my_cursor=conn.cursor()
                        sql="delete from student where Student_id=%s"
                        Val=(self.var_std_id.get(),)
                        my_cursor.execute(sql,Val)
                   else:
                        if not delete:
                             return
                   conn.commit()
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo("Delete","Successfully deleted student details!",parent=self.root)
              except Exception as es:
                  messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

 #==================Reset function===============
    def reset_data(self):
         self.var_dep.set("Select Department")
         self.var_Course.set("Select Course")
         self.var_year.set("Select Year")
         self.var_semester.set("Select Semester")
         self.var_std_id.set("")
         self.var_std_name.set("")
         self.var_div.set("Select Division")
         self.var_roll.set("")
         self.var_gender.set("Male")
         self.var_dob.set("")
         self.var_email.set("")
         self.var_phone.set("")
         self.var_address.set("")
         self.var_teacher.set("")
         self.var_radio1.set("")
         
#=================Generate data set or take photo sample==============

    def generate_dataset(self):
         if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                 messagebox.showerror("Error","All fields are required",parent=self.root)
         else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="MySQL@2003",database="face_reco_sys")
                    my_cursor=conn.cursor()
                    my_cursor.execute("select * from student")
                    myresult=my_cursor.fetchall()
                    id=0
                    for x in myresult:
                        id+=1
                    
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                                        self.var_Course.get(),
                                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                                        self.var_std_id.get()==id+1
                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                ))
                    
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()

                    #===========Load predifiend data on face frontals from OpenCV===============

                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                         gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                         faces=face_classifier.detectMultiScale(gray,1.3,5)
                         #scaling factor=1.3
                         #Minimum Neighbor=5

                         for (x,y,w,h) in faces:
                              face_cropped=img[y:y+h,x:x+w]
                              return face_cropped

                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                         ret,my_frame=cap.read()
                         if face_cropped(my_frame) is not None:
                              img_id+=1
                              face=cv2.resize(face_cropped(my_frame),(450,450))
                              face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                              file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                              cv2.imwrite(file_name_path,face)
                              cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                              cv2.imshow("Cropped Face",face)

                         if cv2.waitKey(1)==13 or int(img_id)==100:
                              break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating data sets compled!!!!",parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()