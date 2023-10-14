from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

class Register:
    def __init__ (self,root):
        self.root=root
        self.root.title("Register Page")
        self.root.geometry("1500x700+0+0")



if __name__=="__main__":
    root=Tk()#object call
    obj=Register(root)
    root.mainloop()