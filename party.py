import tkinter as t
from PIL import Image,ImageTk
import mysql.connector as mysql
from tkinter import messagebox 


class party:
    
        
    def __init__(self,aid):
        self.aid=aid
        self.window=t.Tk()
        

        positionRight = int(self.window.winfo_screenwidth()/2 - 900/2)
        positionDown = int(self.window.winfo_screenheight()/2 - 750/2)

        self.window.geometry("+{}+{}".format(positionRight, positionDown))

        self.window.overrideredirect(1)

        img=Image.open("images/flgg.jpg")
        new_img=img.resize((750,820))
        new_img.save("images/flgg.jpg")
        act_img=ImageTk.PhotoImage(new_img)

        label=t.Label(image=act_img)
        label.place(x=0,y=0)


        head=t.Label(text="PARTIES",fg="green",bg="white",font=("Arial Bold", 30))
        head.grid(row="1",column="0",pady=20,padx=200,ipadx=80,ipady=20,columnspan=2)
        


        img1=Image.open("images/bjpp.png")
        new_img1=img1.resize((100,70))
        new_img1.save("images/bjpp.png")
        act_img1=ImageTk.PhotoImage(new_img1)

        bjp=t.Button(text="BJP",image=act_img1,bg="white")
        bjp.grid(row="2",column="0",pady=10,padx=20,ipadx=50,ipady=50)

        img2=Image.open("images/congs.png")
        new_img2=img2.resize((100,70))
        new_img2.save("images/congs.png")
        act_img2=ImageTk.PhotoImage(new_img2)

        cong=t.Button(text="CONGRESS",image=act_img2,bg="white")
        cong.grid(row="2",column="1",pady=10,padx=0,ipadx=50,ipady=50)

        img3=Image.open("images/appp.jpg")
        new_img3=img3.resize((100,70))
        new_img3.save("images/appp.jpg")
        act_img3=ImageTk.PhotoImage(new_img3)

        aap=t.Button(text="AAP",image=act_img3,bg="white")
        aap.grid(row="3",column="0",pady=10,padx=20,ipadx=50,ipady=50)

        img4=Image.open("images/cpm.jpg")
        new_img4=img4.resize((100,70))
        new_img4.save("images/cpm.jpg")
        act_img4=ImageTk.PhotoImage(new_img4)
        
        cpm=t.Button(text="CPIM",image=act_img4,bg="white")
        cpm.grid(row="3",column="1",pady=10,padx=0,ipadx=50,ipady=50,columnspan=1)


        img5=Image.open("images/tmc.png")
        new_img5=img5.resize((100,70))
        new_img5.save("images/tmc.png")
        act_img5=ImageTk.PhotoImage(new_img5)

        tmc=t.Button(text="TMC",image=act_img5,bg="white")
        tmc.grid(row="4",column="0",pady=10,padx=20,ipadx=50,ipady=50)

        img6=Image.open("images/nota.jpg")
        new_img6=img6.resize((100,70))
        new_img6.save("images/nota.jpg")
        act_img6=ImageTk.PhotoImage(new_img6)

        nota=t.Button(text="NOTA",image=act_img6,bg="white")
        nota.grid(row="4",column="1",pady=10,padx=0,ipadx=50,ipady=50)

        cnfrm=t.Button(text="Submit",fg="green",bg="white",font=("Arial Bold", 17))
        cnfrm.grid(row="5",column="0",pady=20,padx=200,ipadx=80,ipady=20,columnspan=2)




        bjp.bind("<Button-1>",lambda event,p="BJP":self.dblogin(event,p))
        cong.bind("<Button-1>",lambda event,p="CONG":self.dblogin(event,p))
        aap.bind("<Button-1>",lambda event,p="AAP":self.dblogin(event,p))
        cpm.bind("<Button-1>",lambda event,p="CPM":self.dblogin(event,p))
        tmc.bind("<Button-1>",lambda event,p="TMC":self.dblogin(event,p))
        nota.bind("<Button-1>",lambda event,p="NOTA":self.dblogin(event,p))

        cnfrm.bind("<Button-1>",lambda event:self.setparty(event))
        t.mainloop()

        
    def dblogin(self,event,p):
        
        con=mysql.connect(host="localhost",user="root",password="root@123",database="voting")
        cor=con.cursor()
        cor.execute("update registration set Status=1 ,party=%s where Aadhaar_no=%s ",(p,self.aid.strip()))
        con.commit()
        con.close()
        messagebox.showinfo("Thanks","Voting Successful")
        self.window.destroy()
        
        

        
        

     

        

