from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Face Recogniton System')

        title_label = Label(self.root, text='HELP DESK', font=('times new roman', 35, 'bold'), bg='white',
                            fg='blue')
        title_label.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open('./images/aheliotech-help-desk.jpg')
        img_top = img_top.resize((1530, 740), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_label = Label(self.root, image=self.photoimg_top)
        f_label.place(x=0, y=45, width=1530, height=740)

        help_label = Label(f_label, text='Email: nguyentuanphung270301@gmail.com', font=('times new roman', 15, 'bold'), bg='white',fg='blue')
        help_label.place(x=550, y=400)






if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()