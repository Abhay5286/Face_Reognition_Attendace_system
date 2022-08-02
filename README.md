# Face_Reognition_Attendace_system

#Main.py

from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student


class Face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        #First Image
        img=Image.open("C:/Users/Abhay/PycharmProjects/Advance_Face_Recognition_Project/Face_Recog_Images/Nkt.jpg")
        img=img.resize((900,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=50,y=0, width=900,height=130)


        #Second Image
        img1 = Image.open("C:/Users/Abhay/PycharmProjects/Advance_Face_Recognition_Project/Face_Recog_Images/Face_recog.jpg")
        img1 = img1.resize((900, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=550, y=0, width=700, height=130)

        #Third Image
        img2 = Image.open("C:/Users/Abhay/PycharmProjects/Advance_Face_Recognition_Project/Face_Recog_Images/Nkt.jpg")
        img2 = img2.resize((900, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1250, y=0, width=500, height=130)

        # Background Image
        img3 = Image.open("C:/Users/Abhay/PycharmProjects/Advance_Face_Recognition_Project/Face_Recog_Images/bg_img.jpg")
        img3 = img3.resize((1920, 1080), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1920, height=1080)


        #Title
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("Sans Serif",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1920,height=45)


        #Student Button
        img4 = Image.open("C:/Users/Abhay/PycharmProjects/Advance_Face_Recognition_Project/Face_Recog_Images/Student.jpg")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1 = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2", font=("Sans Serif",15,"bold"),bg="Light Blue",fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)


        # Detect Face Button
        img5 = Image.open("C:/Users/Abhay/PycharmProjects/Advance_Face_Recognition_Project/Face_Recog_Images/Face_detector.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2", font=("Sans Serif", 15, "bold"), bg="Light Blue", fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)


        # Attendance Button
        img6 = Image.open(
            "C:/Users/Abhay/PycharmProjects/Advance_Face_Recognition_Project/Face_Recog_Images/Attendance.png")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b1.place(x=780, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2", font=("Sans Serif", 15, "bold"), bg="Light Blue",fg="white")
        b1_1.place(x=780, y=300, width=220, height=40)


        # Help Desk Button
        img7 = Image.open( "C:/Users/Abhay/PycharmProjects/Advance_Face_Recognition_Project/Face_Recog_Images/He.jpg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b1.place(x=1060, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2", font=("Sans Serif", 15, "bold"), bg="Light Blue",
                      fg="white")
        b1_1.place(x=1060, y=300, width=220, height=40)


        # Train Face Button
        img8 = Image.open(
            "C:/Users/Abhay/PycharmProjects/Advance_Face_Recognition_Project/Face_Recog_Images/Data Training.jpg")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2")
        b1.place(x=200, y=400, width=220, height=220)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2", font=("Sans Serif", 15, "bold"), bg="Light Blue",
                      fg="white")
        b1_1.place(x=200, y=600, width=220, height=40)


        # Photos Button
        img9 = Image.open("C:/Users/Abhay/PycharmProjects/Advance_Face_Recognition_Project/Face_Recog_Images/Phostos.jpg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2")
        b1.place(x=500, y=400, width=220, height=220)

        b1_1 = Button(bg_img, text="Photos", cursor="hand2", font=("Sans Serif", 15, "bold"), bg="Light Blue",
                      fg="white")
        b1_1.place(x=500, y=600, width=220, height=40)


        # Developer Button
        img10 = Image.open(
            "C:/Users/Abhay/PycharmProjects/Advance_Face_Recognition_Project/Face_Recog_Images/Developer.jpg")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        b1.place(x=800, y=400, width=220, height=220)

        b1_1 = Button(bg_img, text="Developer", cursor="hand2", font=("Sans Serif", 15, "bold"), bg="Light Blue",
                      fg="white")
        b1_1.place(x=800, y=600, width=220, height=40)


        # Exit Button
        img11 = Image.open("C:/Users/Abhay/PycharmProjects/Advance_Face_Recognition_Project/Face_Recog_Images/Exit.png")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        b1.place(x=1100, y=400, width=220, height=220)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", font=("Sans Serif", 15, "bold"), bg="Light Blue",
                      fg="white")
        b1_1.place(x=1100, y=600, width=220, height=40)


    def student_details(self):
       self.new_window = Toplevel(self.root)
       self.app = Student(self.new_window)



if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition_system(root)
    root.mainloop()
