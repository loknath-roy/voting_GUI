import tkinter as t
import registrationformproject as reg
from tkinter import messagebox as mb
import party as p
from PIL import Image,ImageTk
import mysql.connector as mysql
from gtts import gTTS 
from playsound import playsound

class login:
    def dblogin(self,event):
        adhrstr=self.a.get()
        passtr=self.p.get()
        if adhrstr=="" and passtr=="":
          mb.showerror("Error","Please fill all field")
        else:
            con=mysql.connect(host="localhost",username="root",password="root@123",database="voting")  
            cur=con.cursor()
            cur.execute("select * from registration where Aadhaar_no=%s and Password=%s",(adhrstr,passtr))
            tabledata=cur.fetchall()
            for val in tabledata:    
                for row in tabledata:
                   # print(row[9])
                    if row[9]==None:
                        mb.showinfo("Success","Login Successful")
                        self.window.destroy()
                        p1=p.party(adhrstr)
                        break
                    else:           
                        mb.showwarning("Already voted","Already voted")
                        break
                else:
                    mb.showerror("Error","Invalid aadhaar no. or password")
            
            con.close()
        

        
    def __init__(self):
        
        self.window=t.Tk()
         
        
        positionRight = int(self.window.winfo_screenwidth()/2 - 500/2)
        positionDown = int(self.window.winfo_screenheight()/2 - 500/2)
         
        self.window.geometry("+{}+{}".format(positionRight, positionDown))
        self.window.overrideredirect(1)




        img=Image.open("images/login.jpg")
        new_img=img.resize((600,500))
        new_img.save("images/login.jpg")
        act_img=ImageTk.PhotoImage(new_img)

        label=t.Label(image=act_img)
        label.place(x=0,y=0)

        details=t.Label(text="ENTER YOUR DETAILS",font=("Arial Bold", 15),bg="white",fg="green")


        self.a=t.StringVar()
        
        aadhar=t.Label(text="AADHAR NUMBER",bg="white",fg="green",font=("Arial Bold", 13))
        aadharentry=t.Entry(textvariable=self.a)


        self.p=t.StringVar()
        password=t.Label(text="PASSWORD",bg="white",fg="green",font=("Arial Bold", 13))
        passwordentry=t.Entry(textvariable=self.p,show="*")

        newuser=t.Label(text="New User?",bg="white",fg="green",font=("Arial Bold", 10))


        login=t.Button(text="LOGIN",bg="white",fg="green",font=("Arial Bold", 13))


        img1=Image.open("images/BACK2.jpg")
        new_img1=img1.resize((50,50))
        new_img1.save("images/BACK2.jpg")
        act_img1=ImageTk.PhotoImage(new_img1)
        back=t.Label(image=act_img1)
        details.grid(row="1",column="1",pady=60,padx=50,ipadx=20,ipady=5,columnspan=2)


        
        aadhar.grid(row="2",column="0",pady=10,padx=10,ipadx=10,ipady=5)
        aadharentry.grid(row="2",column="1",pady=10,padx=10,ipadx=40,ipady=10)
        password.grid(row="3",column="0",pady=10,padx=10,ipadx=20,ipady=5)
        passwordentry.grid(row="3",column="1",pady=10,padx=10,ipadx=40,ipady=10)
        newuser.grid(row="4",column="1",pady=10,padx=50,ipadx=20)
        login.grid(row="5",column="1",pady=40,padx=50,ipadx=20,ipady=10)

        back.grid(row="0",column="0",sticky="W")
        back.bind("<Button-1>",lambda event:self.demo1(event))

        newuser.bind("<Button-1>",lambda event:self.demo(event))
        login.bind("<Button-1>",lambda event:self.dblogin(event))
        t.mainloop()
    def demo(self,event):
        self.window.destroy()
        tt=reg.form()
    def demo1(self,event):
        self.window.destroy()
        import Mainpage as m
        mm=m.main()
    
St=login()
