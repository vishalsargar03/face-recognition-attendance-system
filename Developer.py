from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
         self.root=root
         self.root.geometry("1530x790+0+0")
         self.root.title("Face Regonition System")
        
         title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
         title_lbl.place(x=0,y=0,width=1350,height=45)
        
         img_top=Image.open(r"D:\python project\college-images\college_images\dev.jpg")
         img_top=img_top.resize((1530,720),Image.ANTIALIAS)
         self.photoimg_top=ImageTk.PhotoImage(img_top)
        
         f_lbl=Label(self.root,image=self.photoimg_top)
         f_lbl.place(x=0,y=55,width=1530,height=720)
      
         # Frame  
         main_frame=Frame(f_lbl,bd=2,bg="White")
         main_frame.place(x=1000,y=0,width=500,height=600)
        
         img_top1=Image.open(r"D:\python project\college-images\college_images\dev.jpg")
         img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
         self.photoimg_top1=ImageTk.PhotoImage(img_top1)
        
         f_lbl=Label(main_frame,image=self.photoimg_top1)
         f_lbl.place(x=300,y=0,width=200,height=200)

         # Developer info
         dev_label=Label(main_frame,text="Vishal(5021154)",font=("times new roman",18,"bold"),bg="white",fg="grey")
         dev_label.place(x=0,y=5)
        
         dev_label=Label(main_frame,text="Atharva(5021141)",font=("times new roman",18,"bold"),bg="white",fg="grey")
         dev_label.place(x=0,y=40)

         dev_label=Label(main_frame,text="piyush(5021134)",font=("times new roman",18,"bold"),bg="white",fg="grey")
         dev_label.place(x=0,y=80)

         dev_label=Label(main_frame,text="Ruturaj(5021147)",font=("times new roman",18,"bold"),bg="white",fg="grey")
         dev_label.place(x=0,y=120)
        
         img2=Image.open(r"D:\python project\college-images\college_images\A.jpg.")
         img2=img2.resize((500,390),Image.Resampling.LANCZOS)
         self.photoimg2=ImageTk.PhotoImage(img2)


         f_lbl=Label(main_frame,image=self.photoimg2)
         f_lbl.place(x=0,y=210,width=500,height=390)


        
        
        
   
if __name__ =="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()