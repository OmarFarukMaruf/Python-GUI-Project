from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os


class Seller:
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

        self.search_product = Button(self.frame3, text='SEARCH PRODUCT', font=('time new roman',12, 'bold'),command=self.search, bd=0, cursor='hand2', bg='sky blue').place(x=20, y=50)
        self.update_product = Button(self.frame3, text='UPDATE PRODUCT', font=('time new roman',12, 'bold'), bd=0, cursor='hand2', bg='sky blue').place(x=220, y=50)
        self.add_product = Button(self.frame3, text='ADD PRODUCT', font=('time new roman',12, 'bold'),command=self.add, bd=0, cursor='hand2', bg='sky blue').place(x=410, y=50)
        self.delete_product = Button(self.frame3, text='DELETE PRODUCT', font=('time new roman',12, 'bold'), bd=0, cursor='hand2', bg='sky blue').place(x=20, y=120)
        self.display_product = Button(self.frame3, text='DISPLAY PRODUCT', font=('time new roman',12, 'bold'), bd=0, cursor='hand2', bg='sky blue').place(x=220, y=120)
        self.exit_button = Button(self.frame3, text='EXIT', font=('time new roman',12, 'bold'), bd=0, cursor='hand2', bg='red').place(x=250, y=220)

    def add(self):
        self.window.destroy()
        # Importing the signup window.
        # The page must be in the same directory
        self.root1= Tk()
        self.root1.title("Forget Password?")
        self.root1.geometry("400x440+450+200")
        self.root1.config(bg="white")

        self.brand_entry = StringVar()
        self.model_entry = StringVar()
        self.price_entry = StringVar()

        self.brand_label = Label(self.root1, text='Brand:', font=('time new roman',14, 'bold'),bd=0, cursor='hand2', bg='cyan').place(x=20, y=50)
        self.brand_entry = Entry(self.root1, font=('time new roman',12), bg='light gray').place(x=100,y=50,width=200)
        self.model_label = Label(self.root1, text='Model:', font=('time new roman',14, 'bold'),bd=0, cursor='hand2', bg='cyan').place(x=20, y=100)
        self.model_entry = Entry(self.root1, font=('time new roman',12), bg='light gray').place(x=100,y=100,width=200)
        self.price_label = Label(self.root1, text='Price:', font=('time new roman',14, 'bold'),bd=0, cursor='hand2', bg='cyan').place(x=20, y=150)
        self.price_entry = Entry(self.root1, font=('time new roman',12), bg='light gray').place(x=100,y=150,width=200)
        self.button_search = Button(self.root1, text='ADD', font=('time new roman', 12),command=self.add_function, bg='light gray', bd=0, cursor='hand2').place(x=100, y=200, width=150)
        self.notif = Label(self.root1, font=('calibri', 11)).place(x=200, y=350, width=150)


    def add_function(self):
        self.brand = self.brand_entry.get()
        self.model = self.model_entry.get()
        self.price = self.price_entry.get()
        self.all_accounts = os.listdir()

        if self.brand == "" or self.model == "" or self.price == "":
            messagebox.showerror("Error!", "Sorry!, All fields are required", parent=self.window)
        else:
            with open("Account.txt", 'a') as a:
                x = a.write(self.name + '\t\t' + self.email +
                            '\t\t' + self.password + '\n')
                self.notif.config(fg='Green', text="ADD Successfully!")



    def search(self):
        self.window.destroy()
        # Importing the signup window.
        # The page must be in the same directory
        self.root2= Tk()
        self.root2.title("Forget Password?")
        self.root2.geometry("400x440+450+200")
        self.root2.config(bg="white")
        self.Label = Label(self.root2, text='Search your product.........', font=('time new roman', 12, 'bold'), bg='white', fg='red').place(x=20, y=10)
        self.brand_label1 = Label(self.root2, text='Brand:', font=('time new roman',14, 'bold'),bd=0, cursor='hand2', bg='cyan').place(x=20, y=60)
        self.brand_entry1 = Entry(self.root2, font=('time new roman',12), bg='light gray').place(x=100,y=60,width=200)
        self.model_label1 = Label(self.root2, text='Model:', font=('time new roman',14, 'bold'),bd=0, cursor='hand2', bg='cyan').place(x=20, y=110)
        self.model_entry1 = Entry(self.root2, font=('time new roman',12), bg='light gray').place(x=100,y=110,width=200)
        self.button_search = Button(self.root2, text='SEARCH', font=('time new roman', 12), bg='light gray').place(x=100, y=200, width=150)

if __name__ == '__main__':
    root = Tk()
    obj = Seller(root)
    root.mainloop()
