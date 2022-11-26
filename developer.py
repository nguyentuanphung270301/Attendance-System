from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Face Recogniton System')

        title_label = Label(self.root, text='DEVELOPER', font=('times new roman', 35, 'bold'), bg='white',
                            fg='blue')
        title_label.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open('./images/developer.jpg')
        img_top = img_top.resize((1530, 720), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_label = Label(self.root, image=self.photoimg_top)
        f_label.place(x=0, y=55, width=1530, height=720)

        #Frame
        main_frame = Frame(f_label, bd=2)
        main_frame.place(x=1000, y=0, width=500, height=600)

        img_avt = Image.open('./images/ntp.jpg')
        img_avt = img_avt.resize((200, 200), Image.ANTIALIAS)
        self.photoimg_avt = ImageTk.PhotoImage(img_avt)

        f_label = Label(main_frame, image=self.photoimg_avt)
        f_label.place(x=300, y=0, width=200, height=200)

        # Developer info
        dev_label = Label(main_frame, text='Welcome to my app', font=('times new roman', 15, 'bold'), bg='white')
        dev_label.place(x=0,y=5)

        dev_label = Label(main_frame, text='Code by: Nguyen Tuan Phung', font=('times new roman', 15, 'bold'),
                          bg='white')
        dev_label.place(x=0, y=40)

        img2 = Image.open('./images/dev.png')
        img2 = img2.resize((500, 390), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_label = Label(main_frame, image=self.photoimg2)
        f_label.place(x=0, y=210, width=500, height=390)




if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()