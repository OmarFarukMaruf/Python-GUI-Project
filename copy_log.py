from tkinter import *
from tkinter import ttk, messagebox
import pymysql
from PIL import Image, ImageTk
from Customer import Customer
from Seller import Seller
from copy_singup import Sign_page



class Log_page:
    def __init__(self, root):

        self.temp_email = StringVar()
        self.temp_password = StringVar()

        self.window = root
        self.window.title('Login Page')
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
        self.frame3.place(x=140,y=150,width=500,height=450)

        self.email_label = Label(self.frame3,text="Email Address", font=("helvetica",20,"bold"),bg="white", fg="gray").place(x=80,y=40)
        self.temp_email = Entry(self.frame3, font=("times new roman",15,"bold"),bg="white",fg="gray")
        self.temp_email.place(x=80, y =80, width=300)

        self.password_label = Label(self.frame3,text="Password", font=("helvetica",20,"bold"),bg="white", fg="gray").place(x=80,y=120)
        self.temp_password= Entry(self.frame3, font=("times new roman",15,"bold"),bg="white",fg="gray", show='*')
        self.temp_password.place(x=80, y =160, width=300)

        self.button1 = Button(self.frame3, text='Log In', font=("times new roman", 15, "bold"), command=self.seller_log,bd=0, cursor="hand2", bg="blue", fg="white").place(x=80, y=200, width=300)
        self.forgotten_pass = Button(self.frame3, text="Forgotten password?", font=("times new roman", 10, "bold"), bd=0, cursor="hand2", bg="white", fg="blue").place(x=125, y=260, width=150)
        self.create_button = Button(self.frame3,text="Create New Account", command= self.new_window,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="green2",fg="white").place(x=100,y=320,width=250)

    def seller_log(self):
        self.email_log = self.temp_email.get()
        self.password_log = self.temp_password.get()
        if self.email_log == "" or self.password_log == "":
            messagebox.showerror("Error!", "Sorry!, All fields are required", parent=self.window)
        else:
            file = open('Account.txt')
            all_lines = file.readlines()
            str_match = [s for s in all_lines if s.__contains__(self.email_log)]
            if str_match == []:
                messagebox.showerror("Error!", "Sorry!, You have no Account", parent=self.window)
            if str_match != []:
                str_match2 = [s for s in all_lines if s.__contains__(self.password_log)]
                if str_match2 == []:
                    messagebox.showerror("Wrong Password!", parent=self.window)
                else:
                   # messagebox.showinfo("showinfo", "You are in", parent = self.window)
                    self.window.destroy()
                    root = Tk()
                    sell_obj = Seller(root)
                    root.mainloop()


    def new_window(self):
        self.window.destroy()
        root = Tk()
        sing_obj = Sign_page(root)
        root.mainloop()


class CusLog_page:
    def __init__(self, root):

        self.temp_email = StringVar()
        self.temp_password = StringVar()

        self.window = root
        self.window.title('Login Page')
        self.window.geometry("1280x800+0+0")
        self.window.config(bg="white")

        self.frame1 = Frame(self.window, bg='orange')
        self.frame1.place(x=0, y=0, width=450, relheight=1)
        label_1 = Label(self.frame1, text='Smart', font=(
            'time new roman', 45, 'bold'), bg='orange', fg="red").place(x=50, y=100)
        label_2 = Label(self.frame1, text='Phone', font=(
            'time new roman', 45, 'bold'), bg='orange', fg="blue").place(x=220, y=100)
        label_3 = Label(self.frame1, text='Find your best deal in best Platform', font=(
            'time new roman', 14, 'bold'), bg='orange', fg="gray").place(x=50, y=179)
        self.bg_img = ImageTk.PhotoImage(file="pic.png")
        background = Label(self.frame1, image=self.bg_img,
                           bg='orange').place(x=0, y=200)

        self.frame2 = Frame(self.window, bg="gray95")
        self.frame2.place(x=450, y=0, relwidth=1, relheight=1)

        self.frame3 = Frame(self.frame2, bg="white")
        self.frame3.place(x=140, y=150, width=500, height=450)

        self.email_label = Label(self.frame3, text="Email Address", font=(
            "helvetica", 20, "bold"), bg="white", fg="gray").place(x=80, y=40)
        self.temp_email = Entry(self.frame3, font=(
            "times new roman", 15, "bold"), bg="white", fg="gray")
        self.temp_email.place(x=80, y=80, width=300)

        self.password_label = Label(self.frame3, text="Password", font=(
            "helvetica", 20, "bold"), bg="white", fg="gray").place(x=80, y=120)
        self.temp_password = Entry(self.frame3, font=(
            "times new roman", 15, "bold"), bg="white", fg="gray", show='*')
        self.temp_password.place(x=80, y=160, width=300)

        self.button1 = Button(self.frame3, text='Log In', font=("times new roman", 15, "bold"),
                              command=self.customer_log, bd=0, cursor="hand2", bg="blue", fg="white").place(x=80, y=200, width=300)
        self.forgotten_pass = Button(self.frame3, text="Forgotten password?", font=(
            "times new roman", 10, "bold"), bd=0, cursor="hand2", bg="white", fg="blue").place(x=125, y=260, width=150)
        self.create_button = Button(self.frame3, text="Create New Account", command=self.new_window, font=(
            "times new roman", 18, "bold"), bd=0, cursor="hand2", bg="green2", fg="white").place(x=100, y=320, width=250)

    def customer_log(self):
        self.email_log = self.temp_email.get()
        self.password_log = self.temp_password.get()
        if self.email_log == "" or self.password_log == "":
            messagebox.showerror(
                "Error!", "Sorry!, All fields are required", parent=self.window)
        else:
            file = open('Account.txt')
            all_lines = file.readlines()
            str_match = [
                s for s in all_lines if s.__contains__(self.email_log)]
            if str_match == []:
                messagebox.showerror(
                    "Error!", "Sorry!, You have no Account", parent=self.window)
            if str_match != []:
                str_match2 = [
                    s for s in all_lines if s.__contains__(self.password_log)]
                if str_match2 == []:
                    messagebox.showerror("Wrong Password!", parent=self.window)
                else:
                   # messagebox.showinfo("showinfo", "You are in", parent = self.window)
                    self.window.destroy()
                    root = Tk()
                    customer_obj = Customer(root)
                    root.mainloop()

    def new_window(self):
        self.window.destroy()
        root = Tk()
        sing_obj = Sign_page(root)
        root.mainloop()

    def log_in(self):
        pass





if __name__ == '__main__':
    root = Tk()
    obj = Log_page(root)
    root.mainloop()
