from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Train Face Data")


        # Title
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=(
            "Sans Serif", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=10, width=1920, height=45)

        #Top Image
        img_top = Image.open(r"Face_Recog_Images/Train data1.jpg")
        img_top = img_top.resize((1920, 440), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=1920, height=480)

        #button
        b1_1 = Button(self.root, text="TRAIN DATA",command=self.train_classifier, cursor="hand2", font=("Sans Serif", 35, "bold"), bg="#F45D01",fg="Black")
        b1_1.place(x=0, y=520, width=1920, height=60)

        #Bottom Image
        img_bottom = Image.open(r"Face_Recog_Images/Train data2.jpg")
        img_bottom = img_bottom.resize((1920, 440), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=580, width=1920, height=480)

    def train_classifier(self):
        data_dir= ("Data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # Gray Scale Image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1) == 13
        ids=np.array(ids)


        # TRAIN THE CLASSIFIER AND SAVE
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Data set Completed")











if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()