from ast import Global
from http.client import NOT_MODIFIED
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import os

class Sign_page():
    def __init__(self,root):

        global email_entry
        global name_entry
        global password_txt
        global notif

        self.email_entry = StringVar()
        self.name_entry = StringVar()
        self.password_txt = StringVar()
        self.window = root
        self.window.title('SignUp Page')
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

        self.name_label = Label(self.frame3,text="Name: ", font=("helvetica",14,"bold"),bg="white", fg="gray").place(x=40,y=40)
        self.name_entry = Entry(self.frame3, font=("times new roman",15,"bold"),bg="white",fg="gray")
        self.name_entry.place(x=150, y =40, width=200)

        self.email_label = Label(self.frame3,text="Email: ", font=("helvetica",14,"bold"),bg="white", fg="gray").place(x=40,y=80)
        self.email_entry = Entry(self.frame3, font=("times new roman",15,"bold"),bg="white",fg="gray")
        self.email_entry.place(x=150, y =80, width=200)

        sec_question = Label(self.frame3, text="District:", font=("helvetica",14,"bold"),bg="white", fg='gray').place(x=40, y=120)
        self.questions = ttk.Combobox(self.frame3,font=("helvetica",13),state='readonly',justify=CENTER)
        self.questions['values'] = ("Select","Dhaka","Chittagong","Rajshahi", "Barishal")
        self.questions.place(x=150,y=120,width=200)
        self.questions.current(0)

        password =  Label(self.frame3, text="New password", font=("helvetica",12,"bold"),bg="white").place(x=40, y=160)

        self.password_txt = Entry(self.frame3,font=("arial"),bg="white",fg="gray", show='*')
        self.password_txt.place(x=180, y=160, width=200)
        self.terms = IntVar()
        terms_and_con = Checkbutton(self.frame3,text="I Agree The Terms & Conditions",variable=self.terms,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=40,y=220)
        self.signup = Button(self.frame3,text="Sign Up",font=("times new roman",14, "bold"),command=self.finish, bd=0,cursor="hand2",bg="green",fg="white").place(x=120,y=280,width=250)
        self.notif = Label(self.frame3, font=('Calibri', 12))
        self.notif.place(x=120,y=320, width=250)


    def finish(self):
        self.name = self.name_entry.get()
        self.email = self.email_entry.get()
        self.password = self.password_txt.get()
        self.all_accounts = os.listdir()

        if self.name == "" or self.email == "" or self.password == "":
            self.notif.config(fg='red', text = "All files are required!")
        for self.name_check in self.all_accounts:
            if self.email == self.name_check:
                self.notif.config(fg='red', text="Account already exists")
                return
        else:
            with open("Account.txt", 'a') as a:
                x = a.write(self.name + '\t\t' + self.email + '\t\t' + self.password + '\n')
                self.notif.config(fg='Green', text="Registration Successfull!")




if __name__ == '__main__':
    root =Tk()
    obj = Sign_page(root)
    root.mainloop()


