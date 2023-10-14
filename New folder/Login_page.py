from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #to add background
class Login_window:
    def __init__(self,root):# root is window name
        
        self.root=root
        self.root.title("Login")#To set title of page
        self.root.geometry("1550x800+0+0")#To set dimension and starting and ending point
        
        #To add background image
        self.bg=ImageTk.PhotoImage(file="Image123.jpg")
        lbl_bg=Label(self.root,image=self.bg)#To place the image we create a label
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)#It place the label if we increase the relwidth and relheight it will increase the postion in x and y direction
 
        #To add Black frame on Background 
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)#width and height of frame. x and y are starting point


        #How to add admin logo in center at black screen
        img1=Image.open("5087579.png")
        img1=img1.resize((100,100))
        self.photoimage1=ImageTk.PhotoImage(img1)# here img1 comnes in photoimage1 by ImageTk
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)#To place the image we create a label
        lblimg1.place(x=730,y=175,width=100,height=100)

        #How to add text below the admin logo
        get_str=Label(frame,text="Admin Login",font=("Times new roman",20,"bold"),fg="aqua",bg="black")#fg is label color and bg is label background colour
        get_str.place(x=95,y=100)

        #How to display Username text on frame
        get_username=Label(frame,text="Username",font=("Times new roman",15,"bold"),fg="white",bg="black")
        get_username.place(x=70,y=155)

        #place a text box to enter a user name in it
        self.txtuser=ttk.Entry(frame,font=("Times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        #How to add icon before username
        img2=Image.open("747959.png")
        img2=img2.resize((25,25))
        self.photoimage2=ImageTk.PhotoImage(img2)# here img1 comnes in photoimage1 by ImageTk
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)#To place the image we create a label
        lblimg1.place(x=650,y=323,width=25,height=25)

        #How to display Password text on frame
        get_password=Label(frame,text="Password",font=("Times new roman",15,"bold"),fg="white",bg="black")
        get_password.place(x=70,y=225)

        #How to add icon before password
        img3=Image.open("1232.png")
        img3=img3.resize((25,25))
        self.photoimage3=ImageTk.PhotoImage(img3)# here img1 comnes in photoimage1 by ImageTk
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)#To place the image we create a label
        lblimg1.place(x=650,y=396,width=25,height=25)

        #place a text box to enter a user name in it
        self.txtpass=ttk.Entry(frame,font=("Times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #place  login button
        butt=Button(frame,text="Login",font=("Times new roman",15,"bold"),fg="black",bg="aqua",activeforeground="black",activebackground="aqua")
        #fg is font color,activeforeground and activebakground not set then color changes on click
        butt.place(x=110,y=300,width=120,height=35)

        #place  Register  button
        butt=Button(frame,text="New user Register",borderwidth=0,font=("Times new roman",12,"bold"),fg="aqua",bg="black",activeforeground="black",activebackground="black")
        #fg is font color,activeforeground and activebakground not set then color changes on click
        butt.place(x=20,y=340,width=160,height=35)

        #place  Forgot password button
        butt=Button(frame,text="Forgot Password",borderwidth=0,font=("Times new roman",12,"bold"),fg="aqua",bg="black",activeforeground="black",activebackground="black")
        #fg is font color,activeforeground and activebakground not set then color changes on click
        butt.place(x=12,y=370,width=160,height=35)

        


if __name__=="__main__":
    root=Tk()
    app=Login_window(root)#object creation
    root.mainloop()