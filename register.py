from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title('Register')
        self.root.geometry('1600x900+0+0')
        #====== varibles =============
        self.var_fname=StringVar()
        self.var_lname = StringVar()
        self.var_username = StringVar()
        self.var_email = StringVar()
        self.var_sercurityQ = StringVar()
        self.var_sercurityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        #=============bg image ===========================
        self.bg=ImageTk.PhotoImage(file=r'./images/bgimg.jpg')
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        # =============left image ===========================
        self.left = ImageTk.PhotoImage(file=r'./images/reg_left.jpg')
        left_lbl = Label(self.root, image=self.left)
        left_lbl.place(x=50, y=100, width=470,height=550)

        # =============main frame===========================
        frame = Frame(self.root,bg='white')
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl = Label(frame,text='REGISTER HERE',font=('times new roman',25,'bold'),fg='darkgreen',bg='white')
        register_lbl.place(x=20,y=20)

        #=============label and entry ==========================
        #====row 1================
        fname=Label(frame,text='First Name',font=('times new roman',15,'bold'),bg='white')
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame, textvariable=self.var_fname,font=('times new roman',15,'bold'))
        fname_entry.place(x=50,y=130,width=250)

        lname = Label(frame, text='Last Name', font=('times new roman', 15, 'bold'), bg='white')
        lname.place(x=370, y=100)

        lname_entry = ttk.Entry(frame,textvariable=self.var_lname, font=('times new roman', 15, 'bold'))
        lname_entry.place(x=370, y=130, width=250)

        #========row 2=========
        username = Label(frame, text='Username', font=('times new roman', 15, 'bold'), bg='white',fg='black')
        username.place(x=50, y=170)

        username_entry = ttk.Entry(frame,textvariable=self.var_username, font=('times new roman', 15, 'bold'))
        username_entry.place(x=50, y=200, width=250)

        email = Label(frame, text='Email', font=('times new roman', 15, 'bold'), bg='white', fg='black')
        email.place(x=370, y=170)

        email_entry = ttk.Entry(frame,textvariable=self.var_email, font=('times new roman', 15, 'bold'))
        email_entry.place(x=370, y=200, width=250)

        # ========row 3=========
        sercurity_Q = Label(frame, text='Select Sercurity Quetions', font=('times new roman', 15, 'bold'), bg='white', fg='black')
        sercurity_Q.place(x=50, y=240)

        self.combo_sercurity_Q=ttk.Combobox(frame,textvariable=self.var_sercurityQ,font=('times new roman', 15, 'bold'), state='readonly')
        self.combo_sercurity_Q['values']=('Select','Your Birth Place','Your Girlfriend name','Your pet name')
        self.combo_sercurity_Q.place(x=50,y=270,width=250)
        self.combo_sercurity_Q.current(0)


        sercurity_A = Label(frame, text='Sercurity Answer', font=('times new roman', 15, 'bold'), bg='white', fg='black')
        sercurity_A.place(x=370, y=240 )

        sercurity_entry = ttk.Entry(frame,textvariable=self.var_sercurityA, font=('times new roman', 15, 'bold'))
        sercurity_entry.place(x=370, y=270, width=250)

        # ========row 4=========
        password = Label(frame, text='Password', font=('times new roman', 15, 'bold'), bg='white', fg='black')
        password.place(x=50, y=310)

        password_entry = ttk.Entry(frame,textvariable=self.var_pass, font=('times new roman', 15, 'bold'))
        password_entry.place(x=50, y=340, width=250)

        confirm_password = Label(frame, text='Confirm Password', font=('times new roman', 15, 'bold'), bg='white', fg='black')
        confirm_password.place(x=370, y=310)

        confirmPasswrod_entry = ttk.Entry(frame,textvariable=self.var_confpass, font=('times new roman', 15, 'bold'))
        confirmPasswrod_entry.place(x=370, y=340, width=250)

        #========= check button===========
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text='I Agree The Terms & Conditions',font=('times new roman',12,'bold'),bg='white',onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #======== register button===========
        img=Image.open('./images/register_btn.png')
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoImage=ImageTk.PhotoImage(img)
        b1=Button(frame,command=self.register_data,image=self.photoImage,borderwidth=0,cursor='hand2')
        b1.place(x=50,y=420,width=200)

        # ======== login button===========
        img1 = Image.open('./images/login_btn.png')
        img1 = img1.resize((200, 50), Image.ANTIALIAS)
        self.photoImage1 = ImageTk.PhotoImage(img1)
        b2 = Button(frame,command=self.login_window, image=self.photoImage1, borderwidth=0, cursor='hand2')
        b2.place(x=370, y=420, width=200)

    #============ function declaration ==============
    def register_data(self):
        if self.var_fname.get()=='' or self.var_username.get()=='' or self.var_sercurityQ.get()=='Select':
            messagebox.showerror('Error','All fields are required',parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror('Error','Password & confirm password must be same',parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror('Error','Please argee our terms are condition',parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='27032001',database='face_recognizer')
            my_cursor=conn.cursor()
            query=('select * from register where username=%s')
            value=(self.var_username.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row !=None:
                messagebox.showerror('Error','User already exist,please try another username',parent=self.root)
            else:
                my_cursor.execute('insert into register values(%s,%s,%s,%s,%s,%s,%s)',(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_username.get(),
                    self.var_email.get(),
                    self.var_sercurityQ.get(),
                    self.var_sercurityA.get(),
                    self.var_pass.get()
                ))
                messagebox.showinfo('Success', 'Register successfully')
            conn.commit()
            conn.close()
            self.root.destroy()
    def login_window(self):
        self.root.destroy()








if __name__ == '__main__':
    root=Tk()
    app = Register(root)
    root.mainloop()