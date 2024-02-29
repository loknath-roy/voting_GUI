import tkinter as t
import adminlogin as a
from PIL import Image,ImageTk
class main:
    def __init__(self):
        
        self.window=t.Tk()
         
        
        positionRight = int(self.window.winfo_screenwidth()/2 - 300/2)
        positionDown = int(self.window.winfo_screenheight()/2 - 300/2)
         
        self.window.geometry("+{}+{}".format(positionRight, positionDown))
        self.window.overrideredirect("True")
    
        img=Image.open("images/indiaflag.jpg")
        new_img=img.resize((600,600))
        new_img.save("images/indiaflag.jpg")
        act_img=ImageTk.PhotoImage(new_img)

        label=t.Label(image=act_img)
        label.place(x=0,y=0)
        
        user=t.Button(text="USER",bg="white",fg="green",font=("Arial Bold", 15))
        admin=t.Button(text="ADMIN",bg="white",fg="green",font=("Arial Bold", 15))

        img1=Image.open("images/BACK2.jpg")
        new_img1=img1.resize((50,50))
        new_img1.save("images/BACK2.jpg")
        act_img1=ImageTk.PhotoImage(new_img1)
        back=t.Label(image=act_img1)
        
        back.grid(row="0",column="0",sticky="W")
        user.grid(row="1",column="0",padx=100,pady=40,ipadx=15,ipady=5)
        admin.grid(row="2",column="0",ipadx=10,ipady=5,pady=50)


        user.bind("<Button-1>",lambda event:self.demo(event))
        admin.bind("<Button-1>",lambda event:self.demo2(event))
        back.bind("<Button-1>",lambda event:self.demo1(event))

        t.mainloop()
   

    def demo(self,event):
        self.window.destroy()
        import login as l
        w=l.login()

    def demo1(self,event):
        import WELCOME
        self.window.destroy()
        w=WELCOME.Welcome()
    def demo2(self,event):
        self.window.destroy()
        aa=a.login()

#tt=main()
