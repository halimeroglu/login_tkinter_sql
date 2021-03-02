from db import DB
from tkinter import *
from tkinter import messagebox

db = DB('new.db')


root = Tk()
root.geometry('370x450')
root.title('Login')
root.config(bg="#55efc4")


login_username = StringVar()
login_password = StringVar()
signup_email = StringVar()
signup_username = StringVar()
signup_password = StringVar()



#login function
def login():
    for row in db.fetch():
         if login_username.get() in row:
             if login_password.get() in row:
                  messagebox.showinfo(message="Your page")
                  post_page = Toplevel(root)
                  post_page.geometry('370x450')
                  post_page.title("My Page")
                  post_page.config(bg="#a29bfe")
                  post_title = Label(post_page, text="My Account", font=('Arial', 28), fg='#2d3436',
                                     bg="#a29bfe").place(x=100, y=30)
                  break
             else:
                  messagebox.showinfo(message="Username or password is wrong")
                  break
         else:
             messagebox.showinfo(message="Username or password is wrong")
             break

#sign up page
def signup():
    signup_page = Toplevel(root)
    signup_page.geometry('370x450')
    signup_page.title('Sign Up')
    signup_page.config(bg="#fab1a0")
    def create_account():
        if signup_username.get() == "" or signup_password.get() == "" or signup_email.get() == "":
            messagebox.showinfo(title="Info",message="This sections can not be empty !")
        else:
            db.insert(signup_username.get(),signup_password.get(),signup_email.get())
            messagebox.showinfo(title="Info", message="Account created successfully !")


    #make widgets
    signup_title = Label(signup_page, text="Sign Up", font=('Arial', 28), fg='#2d3436', bg="#fab1a0").place(x=125, y=30)
    email_label = Label(signup_page, text="Email", font=('Arial', 11), fg='#2d3436', bg="#fab1a0").place(x=30, y=150)
    email_entry = Entry(signup_page, textvariable=signup_email, font=('Arial', 11))
    email_entry.place(x=105,y=150)
    signup_username_label = Label(signup_page, text="Username", font=('Arial', 11), fg='#2d3436', bg="#fab1a0").place(x=30, y=190)
    signup_username_entry = Entry(signup_page, textvariable=signup_username, font=('Arial', 11))
    signup_username_entry.place(x=105, y=190)
    signup_password_label = Label(signup_page, text="Password", font=('Arial', 11), fg='#2d3436', bg="#fab1a0").place(x=30, y=230)
    signup_password_entry = Entry(signup_page, textvariable=signup_password, font=('Arial', 11), show="*")
    signup_password_entry.place(x=105, y=230)
    signup_page_button = Button(signup_page, text="Sign Up", width=15,command=create_account).place(x=125, y=270)




#widgets
title = Label(root,text="Login",font=('Arial',28),fg='#0a3d62',bg="#55efc4").place(x=125,y=30)
username_label = Label(root,text="Username",font=('Arial',11),fg='#0a3d62',bg="#55efc4").place(x=30,y=150)
username_entry = Entry(root,textvariable=login_username,font=('Arial',11))
username_entry.place(x=105,y=150)
password_label = Label(root,text="Password",font=('Arial',11),fg='#0a3d62',bg="#55efc4").place(x=30,y=190)
password_entry = Entry(root,textvariable=login_password,font=('Arial',11),show="*")
password_entry.place(x=105,y=190)
login_button = Button(root,text="Login",width=15,command=login).place(x=125,y=230)
signup_button = Button(root,text="Sign Up",width=15,command = signup).place(x=125,y=270)



root.mainloop()