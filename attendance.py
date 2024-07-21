from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognization System")

      #=============varaibles==================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()



        #  first image
        
        img=Image.open(r"D:\python project\college-images\college_images\smart-attendance.jpg")
        img=img.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)


        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)

        # 2nd image
        img1=Image.open(r"D:\python project\college-images\college_images\clg.jpg")
        img1=img1.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)


        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)

        
          #bg image
        img3=Image.open(r"D:\python project\college-images\college_images\wp2551980.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)


        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)

        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)


        
        img_left=Image.open(r"D:\python project\college-images\college_images\a.jpeg")
        img_left=img_left.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)
         
        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=370)
 
        #labels and entries

        # attendance id  
        attendanceID_label=Label(left_inside_frame,text="AttendanceID:",font=("times new roman",13,"bold"),bg="white")
        attendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)


        attendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

         # roll  
        rollLabel=Label(left_inside_frame,text="Roll:",font=("times new roman",13,"bold"),bg="white")
        rollLabel.grid(row=0,column=2,padx=4,pady=8,sticky=W)


        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",13,"bold"))
        atten_roll.grid(row=0,column=3,padx=10,pady=5,sticky=W)

         # name 
        nameLabel=Label(left_inside_frame,text="Name:",font=("comicsansns 11 bold"),bg="white")
        nameLabel.grid(row=1,column=0)


        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",13,"bold"))
        atten_name.grid(row=1,column=1,pady=8)


        # Department
        depLabel=Label(left_inside_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        depLabel.grid(row=1,column=2)


        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",13,"bold"))
        atten_dep.grid(row=1,column=3,pady=8)

        # time
        timeLabel=Label(left_inside_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
        timeLabel.grid(row=2,column=0)


        atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",13,"bold"))
        atten_time.grid(row=2,column=1,pady=8)


        # Date

        dateLabel=Label(left_inside_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
        dateLabel.grid(row=2,column=2)


        atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",13,"bold"))
        atten_date.grid(row=2,column=3,pady=8)


        # attendance

        attendanceLabel=Label(left_inside_frame,text="Attendance Status:",font=("times new roman",13,"bold"),bg="white")
        attendanceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font=("times new roman",13,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)


        # buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)


        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)


        delete_btn=Button(btn_frame,text="update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)


        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


         #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=690,height=580)


        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=680,height=465)

        #########scroll bar #############
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReporttable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReporttable.xview)
        scroll_y.config(command=self.AttendanceReporttable.yview)

        self.AttendanceReporttable.heading("id",text="Attendance ID")
        self.AttendanceReporttable.heading("roll",text="Roll")
        self.AttendanceReporttable.heading("name",text="Name")
        self.AttendanceReporttable.heading("department",text="Department")
        self.AttendanceReporttable.heading("time",text="Time")
        self.AttendanceReporttable.heading("date",text="Date")
        self.AttendanceReporttable.heading("attendance",text="Attendance")

        self.AttendanceReporttable["show"]="headings"
        self.AttendanceReporttable.column("id",width=100)
        self.AttendanceReporttable.column("roll",width=100)
        self.AttendanceReporttable.column("name",width=100)
        self.AttendanceReporttable.column("department",width=100)
        self.AttendanceReporttable.column("time",width=100)
        self.AttendanceReporttable.column("date",width=100)
        self.AttendanceReporttable.column("attendance",width=100)
        
      
        self.AttendanceReporttable.pack(fill=BOTH,expand=1)

        self.AttendanceReporttable.bind("<ButtonRelease>",self.get_cursor)

# ==================================================fetch data ===========
    def fetchData(self,rows):
        self.AttendanceReporttable.delete(*self.AttendanceReporttable.get_children())
        for i in rows:
           self.AttendanceReporttable.insert("",END,values=i)
    # import csv
    def importCsv(self):     
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV FILE","*.csv"),("Al1 File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)    
            self.fetchData(mydata)

      #export csv
    def exportCsv(self):
       try:
         if len(mydata)<1:
            messagebox.showerror("NO data","No data found to export",parent=self.root)      
            return False   
         fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV FILE","*.csv"),("Al1 File","*.*")),parent=self.root)
         with open(fln,mode="w",newline=" ") as myfile:
            exp_write=csv.writer(myfile,delimiter=",")
         for i in mydata:
               exp_write.writerow(i)
         messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+ "successfully")
       except Exception as  es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root )  

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReporttable.focus()
        content=self.AttendanceReporttable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])        
        self.var_atten_roll.set(rows[1]) 
        self.var_atten_name.set(rows[2]) 
        self.var_atten_dep.set(rows[3]) 
        self.var_atten_time.set(rows[4]) 
        self.var_atten_date.set(rows[5])  
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
         self.var_atten_id.set("")        
         self.var_atten_roll.set("") 
         self.var_atten_name.set("") 
         self.var_atten_dep.set("") 
         self.var_atten_time.set("") 
         self.var_atten_date.set("")  
         self.var_atten_attendance.set("")



    
             



        

        


        
           











         


       




if __name__ =="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()        