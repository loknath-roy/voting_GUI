import tkinter as t
from tkinter import ttk
import mysql.connector as c
from tkinter import *
import mysql.connector as c


class admin_details:
    def Search(self,event):
        con=c.connect(host="localhost",user="root",password="root@123",database="voting")
        cor=con.cursor()
        cor.execute("select First_name, Last_name,Email_Id, Aadhaar_no from registration where Aadhaar_no=%s",(self.adhrstr.get(),))
        rec=cor.fetchall()
        if len(rec):
            p=1
            for row in rec:
                for j in range(len(row)):
                    print(row[j])
                    e = t.Label(self.tab2,width=10, text=row[j], borderwidth=2,relief='ridge')
                    e.grid(row=p, column=j)
        else:
            print("no record found!!")
    
        con.commit()
        con.close()
        
    def __init__(self):
        
       
        self.window =t.Tk()
        self.window.geometry("380x300")

        positionRight = int(self.window.winfo_screenwidth()/2 - 380/2)
        positionDown = int(self.window.winfo_screenheight()/2 - 300/2)

        self.window.geometry("+{}+{}".format(positionRight, positionDown))
        tab_parent=ttk.Notebook(self.window)

        tab1=ttk.Frame(tab_parent)
        self.tab2=ttk.Frame(tab_parent)
        
        tab_parent.add(tab1,text="Record of Users")
        tab_parent.add(self.tab2,text="Search By Adahar ID")
       

        tab_parent.pack(expand=1,fill="both")

        con=c.connect(host="localhost",user="root",password="root@123",database="voting")
        cor=con.cursor()
        cor.execute("select First_name, Last_name, Aadhaar_no ,DOB , Gender , party from registration")  
        rec=cor.fetchall()
        con.commit()

        p=0
        num_fields = len(cor.description)
        field_names = [i[0] for i in cor.description]
        for voters in rec:
            for j in range(len(voters)):
                 e =t.Label(tab1,width=10, text=field_names[j],
                            borderwidth=2,relief='ridge') 
                 e.grid(row=p, column=j) 
          
        i=1

        for voters in rec: 
            for j in range(len(voters)):
                
                e =t.Label(tab1,width=10, text=voters[j],
                borderwidth=2,relief='ridge', anchor="w") 
                e.grid(row=i, column=j) 
              
            i=i+1
        

       # self.adhaar=t.StringVar()

        tab2aid=t.Entry(self.tab2)
        tab2search=t.Button(self.tab2,text="Search")

        tab2aid.grid(row=0,column=0,pady=20,columnspan=3,padx=20)
        tab2search.grid(row=0,column=3,sticky="E")

        tab2search.bind("<Button-1>",lambda event:self.Search(event))



        tab3=ttk.Frame(tab_parent)
        tab_parent.add(tab3,text="Total Votes")
        cor3=con.cursor()
        cor3.execute("select party, count(*) as votes from registration group by party order by votes desc")  
        rec3=cor3.fetchall()
        
        
        con.commit()
        i3=1

        for result in rec3:
            for j in range(len(result)):
                if(result[j]!=None):
                    e =t.Label(tab3,width=10, text=result[j],
                    borderwidth=2,relief='ridge', anchor="w") 
                    e.grid(row=i3, column=j)
                else:
                    break
              
            i3=i3+1
        con.close()



        
        

        self.window.mainloop()


        

if __name__=="__main__":
    v1=admin_details()
