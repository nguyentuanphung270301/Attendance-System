from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from register import Register
import mysql.connector
from main import Face_Recognition_System

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title('Login')
        self.root.geometry('1550x800+0+0')

        self.var_username = StringVar()
        self.var_pass = StringVar()

        self.bg=ImageTk.PhotoImage(file=r'./images/bgimg.jpg')

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg='black')
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open('./images/user.png')
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg='black',borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text='Get Started',font=('times new roman',20,'bold'),fg='white',bg='black')
        get_str.place(x=95,y=100)

        # label
        username=lbl=Label(frame,text='Username',font=('times new roman',15,'bold'),fg='white',bg='black')
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,textvariable=self.var_username,font=('times new roman',15,'bold'))
        self.txtuser.place(x=40,y=180,width=270)

        password = lbl = Label(frame, text='Password', font=('times new roman', 15, 'bold'), fg='white', bg='black')
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame,textvariable=self.var_pass, font=('times new roman', 15, 'bold'))
        self.txtpass.place(x=40, y=250, width=270)

        # ================== Icon Image ==========================
        img2 = Image.open('./images/user.png')
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg='black', borderwidth=0)
        lblimg2.place(x=650, y=323, width=25, height=25)

        img3 = Image.open('./images/pass.png')
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg='black', borderwidth=0)
        lblimg3.place(x=650, y=394, width=25, height=25)

        # login button
        loginbtn=Button(frame,command=self.login, text='Login',font=('times new roman', 15, 'bold'),bd=3,relief=RIDGE,fg='white',bg='red',activeforeground='white',activebackground='red')
        loginbtn.place(x=110,y=300,width=120,height=35)

        # resisgter button
        registerbtn = Button(frame,command=self.rigister_window, text='New User Register', font=('times new roman', 10, 'bold'), borderwidth=0, fg='white',
                          bg='black', activeforeground='white', activebackground='black')
        registerbtn.place(x=15, y=350, width=160)

        # forgetpass button
        forgetbtn = Button(frame,command=self.forgot_password, text='Forget Password', font=('times new roman', 10, 'bold'),borderwidth=0,
                             fg='white',
                             bg='black', activeforeground='white', activebackground='black')
        forgetbtn.place(x=10, y=370, width=160)

    def rigister_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    def login_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition_System(self.new_window)

    def login(self):
        if self.txtuser.get()=='' or self.txtpass.get()=='':
            messagebox.showerror('Error','All fields required')
        elif self.txtuser.get()=='ntp' and self.txtpass.get()=='27032001':
            messagebox.showinfo('Success', 'Welcome to Face Attendance System ')
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='27032001',
                                           database='face_recognizer')
            my_cursor = conn.cursor()
            my_cursor.execute('select * from register where username=%s and password=%s',(
                self.var_username.get(),
                self.var_pass.get()
            ))
            row=my_cursor.fetchone()
            if row ==None:
                messagebox.showerror('Error','Invalid Username & password')
            else:
                self.login_window()
            conn.commit()
            conn.close()

#==============reset pass ===============================

    def reset_password(self):
        if self.combo_sercurity_Q.get()=='Select':
            messagebox.showerror('Error','Select the sercurity question',parent= self.root2)
        elif self.sercurity_A.get()=='':
            messagebox.showerror('Error','please enter the sercurity answer',parent= self.root2)
        elif self.newpassword_entry.get()=='':
            messagebox.showerror('Error','please enter the new password',parent= self.root2)
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='27032001',
                                           database='face_recognizer')
            my_cursor = conn.cursor()
            query=('select * from register where username=%s and sercurityQ=%s and sercurityA=%s')
            value=(self.txtuser.get(),self.combo_sercurity_Q.get(),self.sercurity_A.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror('Error', 'Please enter correct answer',parent= self.root2)
            else:
                query=('update register set password=%s where uaername=%s ')
                value=(self.newpassword_entry.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo('Info','Your password has been reset, please login new password',parent= self.root2)
                self.root2.destroy()

    #==================== forget pass========================
    def forgot_password(self):
        if self.txtuser.get()=='':
            messagebox.showerror('Error','Please enter the username to reset password')
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='27032001',
                                           database='face_recognizer')
            my_cursor = conn.cursor()
            query=('select * from register where username=%s')
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            print(row)

            if row==None:
                messagebox.showerror('Error','Please enter the valid username')
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title('Forget password')
                self.root2.geometry('340x450+610+170')

                l=Label(self.root2,text='Forget Password',font=('times new roman',12,'bold'),fg='red',bg='white')
                l.place(x=0,y=10,relwidth=1)

                sercurity_Q = Label(self.root2, text='Select Sercurity Quetions', font=('times new roman', 15, 'bold'),
                                    bg='white', fg='black')
                sercurity_Q.place(x=50, y=80)

                self.combo_sercurity_Q = ttk.Combobox(self.root2,
                                                      font=('times new roman', 15, 'bold'), state='readonly')
                self.combo_sercurity_Q['values'] = (
                'Select', 'Your Birth Place', 'Your Girlfriend name', 'Your pet name')
                self.combo_sercurity_Q.place(x=50, y=110, width=250)
                self.combo_sercurity_Q.current(0)

                self.sercurity_A = Label(self.root2, text='Sercurity Answer', font=('times new roman', 15, 'bold'), bg='white',
                                    fg='black')
                self.sercurity_A.place(x=50, y=150)

                self.sercurity_entry = ttk.Entry(self.root2,
                                            font=('times new roman', 15, 'bold'))
                self.sercurity_entry.place(x=50, y=180, width=250)

                self.newpassword = Label(self.root2, text='New password', font=('times new roman', 15, 'bold'),
                                    bg='white',
                                    fg='black')
                self.newpassword.place(x=50, y=220)

                self.newpassword_entry = ttk.Entry(self.root2,
                                            font=('times new roman', 15, 'bold'))
                self.newpassword_entry.place(x=50, y=250, width=250)

                btn=Button(self.root2,text='Reset',font=('times new roman',15,'bold'),fg='white',bg='green')
                btn.place(x=100,y=290)


if __name__== '__main__':
    main()
