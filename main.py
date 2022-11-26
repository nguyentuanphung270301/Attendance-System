import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from atttendance import Attendance
from developer import Developer
from help import Help
from time import strftime
from datetime import datetime


class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Face Recogniton System')


        # first img
        img = Image.open('./images/facebanner.png')
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_label = Label(self.root, image=self.photoimg)
        f_label.place(x=0,y=0,width=500,height=130)

        # second img
        img1 = Image.open('./images/banner2.jpg')
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_label = Label(self.root, image=self.photoimg1)
        f_label.place(x=517, y=0, width=500, height=130)

        # third img
        img2 = Image.open('./images/banner3.jpg')
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_label = Label(self.root, image=self.photoimg2)
        f_label.place(x=1000, y=0, width=550, height=130)

        #background img
        bg_img = Image.open('./images/bgimg.jpg')
        bg_img = bg_img.resize((1530,710), Image.ANTIALIAS)
        self.bg_photoimg = ImageTk.PhotoImage(bg_img)

        bg_label = Label(self.root, image=self.bg_photoimg)
        bg_label.place(x=0, y=130, width=1530, height=710)

        title_label = Label(bg_label,text='FACE RECOGNITON ATTENDANCE SYSTEM SOFTWARE',font=('times new roman',35,'bold'),bg='white',fg='red')
        title_label.place(x=0,y=0,width=1530,height=45)

        #time
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(100,time)

        lbl=Label(title_label,font=('times new roman',14,'bold'),background='white',fg='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()


        #student button
        student_btn_img = Image.open('./images/student.png')
        student_btn_img = student_btn_img.resize((220, 220), Image.ANTIALIAS)
        self.student_img = ImageTk.PhotoImage(student_btn_img)

        btn_1 = Button(bg_label,image=self.student_img,command=self.student_details,cursor='hand2')
        btn_1.place(x=200, y=100, width=220, height=220 )

        btn_1_1 = Button(bg_label, text='Student Details',command=self.student_details, cursor='hand2',font=('times new roman',15,'bold'),bg='darkblue',fg='white')
        btn_1_1.place(x=200, y=300, width=220, height=40)

        # Detect face button
        detectFace_btn_img = Image.open('./images/facedetector.jpg')
        detectFace_btn_img = detectFace_btn_img.resize((220, 220), Image.ANTIALIAS)
        self.detectFace_img = ImageTk.PhotoImage(detectFace_btn_img)

        btn_1 = Button(bg_label,command=self.face_data, image=self.detectFace_img, cursor='hand2')
        btn_1.place(x=500, y=100, width=220, height=220)

        btn_1_1 = Button(bg_label,command=self.face_data, text='Face Detector', cursor='hand2', font=('times new roman', 15, 'bold'),
                         bg='darkblue', fg='white')
        btn_1_1.place(x=500, y=300, width=220, height=40)

        # Attendance button
        attendance_btn_img = Image.open('./images/attendance.jpg')
        attendance_btn_img= attendance_btn_img.resize((220, 220), Image.ANTIALIAS)
        self.attendance_img = ImageTk.PhotoImage(attendance_btn_img)

        btn_1 = Button(bg_label,command=self.attendance_data,  image=self.attendance_img, cursor='hand2')
        btn_1.place(x=800, y=100, width=220, height=220)

        btn_1_1 = Button(bg_label,command=self.attendance_data,  text='Attendance', cursor='hand2', font=('times new roman', 15, 'bold'),
                         bg='darkblue', fg='white')
        btn_1_1.place(x=800, y=300, width=220, height=40)

        # Help button
        help_btn_img = Image.open('./images/help.png')
        help_btn_img = help_btn_img.resize((220, 220), Image.ANTIALIAS)
        self.help_img = ImageTk.PhotoImage(help_btn_img)

        btn_1 = Button(bg_label,command=self.help_data, image=self.help_img, cursor='hand2')
        btn_1.place(x=1100, y=100, width=220, height=220)

        btn_1_1 = Button(bg_label,command=self.help_data, text='Help Desk', cursor='hand2', font=('times new roman', 15, 'bold'),
                         bg='darkblue', fg='white')
        btn_1_1.place(x=1100, y=300, width=220, height=40)

        # Train data button
        trainData_btn_img = Image.open('./images/traindata.png')
        trainData_btn_img = trainData_btn_img.resize((220, 220), Image.ANTIALIAS)
        self.trainData_img = ImageTk.PhotoImage(trainData_btn_img)

        btn_1 = Button(bg_label,command=self.train_data, image=self.trainData_img, cursor='hand2')
        btn_1.place(x=200, y=380, width=220, height=220)

        btn_1_1 = Button(bg_label, text='Train Data',command=self.train_data, cursor='hand2', font=('times new roman', 15, 'bold'),
                         bg='darkblue', fg='white')
        btn_1_1.place(x=200, y=580, width=220, height=40)

        # Photos button
        photo_btn_img = Image.open('./images/Photo-icon.png')
        photo_btn_img = photo_btn_img.resize((220, 220), Image.ANTIALIAS)
        self.photo_img = ImageTk.PhotoImage(photo_btn_img)

        btn_1 = Button(bg_label, image=self.photo_img, cursor='hand2',command=self.open_img)
        btn_1.place(x=500, y=380, width=220, height=220)

        btn_1_1 = Button(bg_label,command=self.open_img, text='Photos', cursor='hand2', font=('times new roman', 15, 'bold'),
                         bg='darkblue', fg='white')
        btn_1_1.place(x=500, y=580, width=220, height=40)

        # Developer button
        developer_btn_img = Image.open('./images/developer.png')
        developer_btn_img = developer_btn_img.resize((220, 220), Image.ANTIALIAS)
        self.developer_img = ImageTk.PhotoImage(developer_btn_img)

        btn_1 = Button(bg_label,command=self.developer_data, image=self.developer_img, cursor='hand2')
        btn_1.place(x=800, y=380, width=220, height=220)

        btn_1_1 = Button(bg_label,command=self.developer_data, text='Developer', cursor='hand2', font=('times new roman', 15, 'bold'),
                         bg='darkblue', fg='white')
        btn_1_1.place(x=800, y=580, width=220, height=40)

        # Exit button
        exit_btn_img = Image.open('./images/exit.png')
        exit_btn_img = exit_btn_img.resize((220, 220), Image.ANTIALIAS)
        self.exit_img = ImageTk.PhotoImage(exit_btn_img)

        btn_1 = Button(bg_label, image=self.exit_img, cursor='hand2',command=self.isExit)
        btn_1.place(x=1100, y=380, width=220, height=220)

        btn_1_1 = Button(bg_label,command=self.isExit, text='Exit', cursor='hand2', font=('times new roman', 15, 'bold'),
                         bg='darkblue', fg='white')
        btn_1_1.place(x=1100, y=580, width=220, height=40)

    def open_img(self):
        os.startfile('data')

    def isExit(self):
        self.isExit=tkinter.messagebox.askyesno('Face Recognition','Are you sure exit project',parent=self.root)
        if self.isExit > 0:
            self.root.destroy()
        else:
            return

        #===========Fuctions buttons=====================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Help(self.root)
        self.app=Developer(self.new_window)



if __name__ == "__main__":
    root=Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()