import tkinter as t
import registrationformproject as reg
from tkinter import messagebox 
import party as p
from PIL import Image,ImageTk
import mysql.connector as c

class login:
    def dblogin(self,event):
        con=c.connect(host="localhost",user="root",password="root@123",database="voting")
        cor=con.cursor()
        cor.execute("select * from admin_details where id=%s and pass=%s",(self.a.get(),self.p.get()))
        rec=cor.fetchall()
        con.commit()
        if len(rec):
            for row in rec:
                self.window.destroy()
                import admin_data as ad
                add=ad.admin_details()
                
        else:
            messagebox.showwarning("Wrong Credentials","Admin Not Found")
        con.close()
    def __init__(self):
        
        self.window=t.Tk()
         
        
        positionRight = int(self.window.winfo_screenwidth()/2 - 500/2)
        positionDown = int(self.window.winfo_screenheight()/2 - 500/2)
         
        self.window.geometry("+{}+{}".format(positionRight, positionDown))
        self.window.overrideredirect(1)




        img=Image.open("images/login.jpg")
        new_img=img.resize((600,480))
        new_img.save("images/login.jpg")
        act_img=ImageTk.PhotoImage(new_img)

        label=t.Label(image=act_img)
        label.place(x=0,y=0)


        img1=Image.open("images/BACK2.jpg")
        new_img1=img1.resize((50,50))
        new_img1.save("images/`BACK2.jpg")
        act_img1=ImageTk.PhotoImage(new_img1)
        back=t.Label(image=act_img1)
        
        details=t.Label(text="ENTER YOUR DETAILS",font=("Arial Bold", 15),bg="white",fg="green")


        self.a=t.StringVar()
        
        admin=t.Label(text="ADMIN ID",bg="white",fg="green",font=("Arial Bold", 13))
        adminentry=t.Entry(textvariable=self.a)


        self.p=t.StringVar()
        password=t.Label(text="PASSWORD",bg="white",fg="green",font=("Arial Bold", 13))
        passwordentry=t.Entry(textvariable=self.p,show="*")



        login=t.Button(text="LOGIN",bg="white",fg="green",font=("Arial Bold", 13))

        back.grid(row="0",column="0",sticky="W")
        details.grid(row="1",column="0",pady=60,padx=50,ipadx=20,ipady=5,columnspan=2)


        
        admin.grid(row="2",column="0",pady=10,padx=10,ipadx=10,ipady=5)
        adminentry.grid(row="2",column="1",pady=10,padx=10,ipadx=40,ipady=10)
        password.grid(row="3",column="0",pady=10,padx=10,ipadx=20,ipady=5)
        passwordentry.grid(row="3",column="1",pady=10,padx=10,ipadx=40,ipady=10)
        login.grid(row="5",column="1",pady=40,padx=50,ipadx=20,ipady=10)



        back.bind("<Button-1>",lambda event:self.demo(event))
        login.bind("<Button-1>",lambda event:self.dblogin(event))
        t.mainloop()
    def demo(self,event):
        self.window.destroy()
        import Mainpage as m
        mm=m.main()
    
#St=login()
