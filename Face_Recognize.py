from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class face_Recognizer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+250+150")
        self.root.title("Face Detection")

        # TITLE
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=(
            "Sans Serif", 35, "bold"), bg="#151d28", fg="white")
        title_lbl.place(x=0, y=10, width=1366, height=45)

        #IMAGES
        img_top = Image.open(r"Face_Recog_Images/sebastian-svenson-d2w-_1LJioQ-unsplash.jpg")
        img_top = img_top.resize((1366, 768), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=1366, height=768)

        # button
        b1_1 = Button(f_lbl, text="Face Recognition",command=self.face_recog, cursor="hand2",
                      font=("Sans Serif", 15, "bold"), bg="#fbfc74", fg="Black")
        b1_1.place(x=550, y=300, width=250, height=45)

        #ATTENCDANCE
    def mark_attendance(self,i,r,n,g):
        with open("Attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry==line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (g not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{g},{dtString},{d1},Present")




        #FACE RECOGNITION
    def face_recog(self):
        def draw_boundary(img,classifier, scaleFactor, minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", user="root", password="08052002H@ck",database="facerecognizer", auth_plugin="mysql_native_password")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select RollNo from student where Id=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("select Gender from student where Id=" + str(id))
                g = my_cursor.fetchone()
                g = "+".join(g)

                my_cursor.execute("select Id from student where Id=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                if confidence>77:
                    cv2.putText(img, f"Id:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img,f"RollNo:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"Name:{n}", (x, y - 20), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Gender:{g}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i,r,n,g)
                else:
                    cv2.rectangle(img,(x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img,"Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord=[x,y,w,y]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img, faceCascade, 1.1, 10, (255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret, img=video_cap.read()
            img=recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    obj = face_Recognizer(root)
    root.mainloop()