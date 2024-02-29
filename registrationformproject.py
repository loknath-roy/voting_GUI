import tkinter as t
from tkinter import messagebox as mb
import mysql.connector as c
from PIL import Image,ImageTk

from tkcalendar import *



class form:
    def setDetails(self,event):
        if len(self.f.get())==0 or len(self.l.get())==0 or len(self.e.get())==0 or len(self.d.get())==0 or len(self.p.get())==0 or len(self.cp.get())==0  or len(self.e.get())==0 or len(self.a.get())==0 :
            mb.showerror("INCORRECT","Please fill all entries!!!")
            
        else:
            if self.p.get()==self.cp.get():
                
                
                con=c.connect(host="localhost",user="root",password="root@123",database="voting")
                cur=con.cursor()
                cur.execute("insert into registration(First_name,Last_name,Email_Id,Password,Confirm_pass,Aadhaar_no,DOB,Gender) values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.f.get(),self.l.get(),self.e.get(),self.p.get(),self.cp.get(),self.a.get(),self.d.get(),self.g.get()))
                
                    
                con.commit()
                con.close()
                
                mb.showinfo("CORRECT","Registration successful!!!")
                self.window.destroy()
        
                
            else:
                mb.showerror("INCORRECT","Enter same password in confirm password")
           
    
    def __init__(self):
        self.window=t.Tk()

        posRight=int(self.window.winfo_screenwidth()/2-600/2)
        posDown=int(self.window.winfo_screenheight()/2-600/2)
        self.window.geometry("+{}+{}".format(posRight,-100))

        self.window.overrideredirect(1)

        img=Image.open("images/bod2.jpg")
        new_img=img.resize((520,840))
        new_img.save("images/bod2.jpg")
        act_img=ImageTk.PhotoImage(new_img)

        label=t.Label(image=act_img)
        label.place(x=0,y=0)


        self.f=t.StringVar()
        self.l=t.StringVar()
        self.e=t.StringVar()
        self.d=t.StringVar()
        self.p=t.StringVar()
        self.cp=t.StringVar()
        self.a=t.StringVar()
        self.g=t.StringVar()
        self.c=t.StringVar()
      
        img1=Image.open("images/BACK2.jpg")
        new_img1=img1.resize((50,50))
        new_img1.save("images/BACK2.jpg")
        act_img1=ImageTk.PhotoImage(new_img1)
        back=t.Label(image=act_img1)
        back.grid(row="0",column="0",sticky="W")

        

        details=t.Label(text="ENTER YOUR DETAILS",font=("Arial Bold", 17),bg="white")

        first=t.Label(text="Enter First Name",font=("Arial Bold", 13),bg="white")
        firsttext=t.Entry(textvariable=self.f)

        last=t.Label(text="Enter Last Name",font=("Arial Bold", 13),bg="white")
        lasttext=t.Entry(textvariable=self.l)

        email=t.Label(text="Enter Email",font=("Arial Bold", 13),bg="white")
        emailtext=t.Entry(textvariable=self.e)

        dob=t.Label(text="Enter DOB",font=("Arial Bold", 13),bg="white")
        dobtext=t.Entry(textvariable=self.d)

        password=t.Label(text="Enter Password",font=("Arial Bold", 13),bg="white")
        passwordtext=t.Entry(textvariable=self.p,show="*")

        Cpassword=t.Label(text="Enter C-Password",font=("Arial Bold", 13),bg="white")
        Cpasswordtext=t.Entry(textvariable=self.cp,show="*")

        aadhar=t.Label(text="Aaadhaar Number",font=("Arial Bold", 13),bg="white")
        aadhartext=t.Entry(textvariable=self.a)


        gender=t.Label(text="Select Gender",font=("Arial Bold", 13),bg="white")

        Male=t.Radiobutton(text="Male" ,variable=self.g,value="male",font=("Arial Bold", 13),bg="white")
        Female=t.Radiobutton(text="Female",variable=self.g,value="female",font=("Arial Bold", 13),bg="white")


        city=t.Label(text="Enter City",font=("Arial Bold", 13),bg="white")
        OptionList = ["Bankura","Kolkata","Durgapur","Howrah","Darjeeling"]
        self.var = t.StringVar()
        self.var.set(OptionList[0])
        citydrop=t.OptionMenu(self.window,self.var,*OptionList)

      
        signupnbutton=t.Button(text="Sign Up",font=("Arial Bold", 15),bg="white")
        details.grid(row="1",column="0",padx=60,pady=40,columnspan=2)

        first.grid(row="2",column="0",padx=60,pady=20,sticky="W")
        firsttext.grid(row="2",column="1",padx=60,pady=20)

        last.grid(row="3",column="0",padx=60,pady=20,sticky="W")
        lasttext.grid(row="3",column="1",padx=60,pady=20)


        email.grid(row="4",column="0",padx=60,pady=20,sticky="W")
        emailtext.grid(row="4",column="1",padx=60,pady=20)

        dob.grid(row="5",column="0",padx=60,pady=20,sticky="W")
        dobtext.grid(row="5",column="1",padx=60,pady=20)

        password.grid(row="6",column="0",padx=60,pady=20,sticky="W")
        passwordtext.grid(row="6",column="1",padx=60,pady=20)
        
        Cpassword.grid(row="7",column="0",padx=60,pady=20,sticky="W")
        Cpasswordtext.grid(row="7",column="1",padx=60,pady=20)

        aadhar.grid(row="8",column="0",padx=60,pady=20,sticky="W")
        aadhartext.grid(row="8",column="1",padx=60,pady=20)


        gender.grid(row="9",column="0",padx=60,pady=20,sticky="W")
        Male.grid(row="9",column="1",padx=60,pady=20,sticky="W")
        Female.grid(row="10",column="1",padx=60,pady=0,sticky="W")


        city.grid(row="11",column="0",padx=60,pady=0,sticky="W")
        citydrop.grid(row="11",column="1",padx=70,pady=20,ipadx=30)

        signupnbutton.grid(row="12",column="0",padx=60,pady=0,columnspan=2)

        back.bind("<Button-1>",lambda event:self.demo(event))
        signupnbutton.bind("<Button-1>",lambda event:self.setDetails(event))


        t.mainloop()
        
    def demo(self,event):
        self.window.destroy()
        import login as l
        lo=l.login()
#f=form() 
