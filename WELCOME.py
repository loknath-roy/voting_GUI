import tkinter as t
from PIL import Image,ImageTk
import Mainpage as ma
import time
class Welcome:
    def __init__(self):
        self.window=t.Tk()
        
        positionRight = int(self.window.winfo_screenwidth()/2 - 600/2)
        positionDown = int(self.window.winfo_screenheight()/2 - 400/2)

        self.window.geometry("+{}+{}".format(positionRight, positionDown))

        self.window.overrideredirect("True")

        img=Image.open("images/welcome.jpg")
        new_img=img.resize((600,400))
        new_img.save("images/welcome.jpg")
        act_img=ImageTk.PhotoImage(new_img)

        label=t.Label(image=act_img)
        label.pack()
        self.window.after(3000,self.demo)

        t.mainloop()
    def demo(self):
        self.window.destroy()
        tt=ma.main()
    


if __name__=="__main__":
    w=Welcome()

     

