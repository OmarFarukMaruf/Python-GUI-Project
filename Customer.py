from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


class Customer:
    def __init__(self,root):
        self.window = root
        self.window.title('SmartPhone Buying Shop')
        self.window.geometry("1280x800+0+0")
        self.window.config(bg = "white")

        self.frame1 = Frame(self.window, bg = 'orange')
        self.frame1.place(x=0, y=0, width=450, relheight = 1)
        label_1 = Label(self.frame1, text='Smart', font=('time new roman', 45, 'bold'),bg='orange', fg="red").place(x=50,y=100)
        label_2 = Label(self.frame1, text='Phone', font=('time new roman', 45, 'bold'),bg='orange', fg="blue").place(x=220,y=100)
        label_3 = Label(self.frame1, text='Find your best deal in best Platform', font=('time new roman', 14, 'bold'),bg='orange', fg="gray").place(x=50,y=179)
        self.bg_img = ImageTk.PhotoImage(file="pic.png")
        background = Label(self.frame1, image=self.bg_img, bg='orange').place(x=0,y=200)

        self.frame2 = Frame(self.window, bg = "gray95")
        self.frame2.place(x=450,y=0,relwidth=1, relheight=1)

        self.frame3 = Frame(self.frame2, bg="white")
        self.frame3.place(x=140,y=150,width=600,height=400)

        self.add_product = Button(self.frame3, text='SEARCH PRODUCT', font=('time new roman',12, 'bold'), bd=0, cursor='hand2', bg='sky blue').place(x=220, y=100)
        self.add_product = Button(self.frame3, text='DISPLAY PRODUCT', font=('time new roman',12, 'bold'), bd=0, cursor='hand2', bg='sky blue').place(x=220, y=50)
        self.add_product = Button(self.frame3, text='EXIT', font=('time new roman',12, 'bold'), bd=0, cursor='hand2', bg='red').place(x=280, y=220)



if __name__ == '__main__':
    root = Tk()
    obj = Customer(root)
    root.mainloop()
