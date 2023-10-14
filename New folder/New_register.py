from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

class Register:
    def __init__ (self,root):
        self.root=root
        self.root.title("Register Page")
        self.root.geometry("1500x700+0+0")


       #to add background image
        self.bg=ImageTk.PhotoImage(file="Image123.jpg")
        bg_lbl=Label(root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #To add company logo in side
        self.logo=ImageTk.PhotoImage(file="123.png")
        logo_lbl=Label(root,image=self.logo)
        logo_lbl.place(x=100,y=150,width=400,height=400)

        #frame for regsitartion form
        frame=Frame(self.root,bg="white")
        frame.place(x=550,y=70,width=750,height=550)

        #Heading Register here
        reg_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="green",bg="white")
        reg_lbl.place(x=20,y=20)

        #setting Labels
        fir_name=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        fir_name.place(x=50,y=100)

        #taking input text box for entering name
        fir_name_entry=ttk.Entry(frame,font=("times new roman",13))
        fir_name_entry.place(x=50,y=130,width=250)







if __name__=="__main__":
    root=Tk()#object call
    obj=Register(root)
    root.mainloop()