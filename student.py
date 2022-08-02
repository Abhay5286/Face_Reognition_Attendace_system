from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        # Variables
        self.var_Course = StringVar()
        self.var_Year = StringVar()
        self.var_Sem = StringVar()
        self.var_Id = StringVar()
        self.var_Name = StringVar()
        self.var_RollNo = StringVar()
        self.var_Gender = StringVar()
        self.var_Email = StringVar()
        self.var_PhoneNo = StringVar()
        self.var_Address = StringVar()
        self.var_Teacher = StringVar()
        self.var_DOB = StringVar()

        # First Image
        img = Image.open(
            "C:/Users/Abhay/PycharmProjects/Advance_Face_Recognition_Project/Face_Recog_Images/Student Details.jpg")
        img = img.resize((900, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=50, y=0, width=900, height=130)

        # Second Image
        img1 = Image.open(
            "C:/Users/Abhay/PycharmProjects/Advance_Face_Recognition_Project/Face_Recog_Images/Student Details1.jpg")
        img1 = img1.resize((900, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=550, y=0, width=700, height=130)

        # Third Image
        img2 = Image.open(
            "C:/Users/Abhay/PycharmProjects/Advance_Face_Recognition_Project/Face_Recog_Images/Student Details2.jpg")
        img2 = img2.resize((900, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1250, y=0, width=500, height=130)

        # Background Image
        img3 = Image.open(
            "C:/Users/Abhay/PycharmProjects/Advance_Face_Recognition_Project/Face_Recog_Images/bg_img.jpg")
        img3 = img3.resize((1920, 1080), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1920, height=1080)

        # Title
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=(
            "Sans Serif", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1920, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1890, height=1030)

        # left label frame
        Left_frame = LabelFrame(main_frame, bd=4, bg="white", relief=RIDGE,
                                text="Student Deatils", font=("times new roman", 18, "bold"))
        Left_frame.place(x=20, y=10, width=850, height=800)

        # Frame Image
        img_left = Image.open(
            "C:/Users/Abhay/PycharmProjects/Advance_Face_Recognition_Project/Face_Recog_Images/Frame1.jpg")
        img_left = img_left.resize((900, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=10, y=0, width=820, height=130)

        # Current Course
        Curr_course_frame = LabelFrame(Left_frame, bd=4, bg="white", relief=RIDGE,
                                       text="Current Course Information", font=("times new roman", 18, "bold"))
        Curr_course_frame.place(x=5, y=150, width=830, height=150)

        # Course
        Course_label = Label(Curr_course_frame, text="Course", font=(
            "times new roman", 15, "bold"), bg="white")
        Course_label.grid(row=0, column=0, padx=10)

        Course_combo = ttk.Combobox(Curr_course_frame, textvariable=self.var_Course, font=(
            "times new roman", 15, "bold"), width=17, state="readonly")
        Course_combo['values'] = (
            "Select Course", "BSc IT", "BA", "BCom", "BMM", "BMS", "BBI", "MCOM", "BAF")
        Course_combo.current(0)
        Course_combo.grid(row=0, column=1, padx=5, pady=15)

        # Year
        course_label = Label(Curr_course_frame, text="Year", font=(
            "times new roman", 15, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        Year_combo = ttk.Combobox(Curr_course_frame, textvariable=self.var_Year, font=(
            "times new roman", 15, "bold"), width=17, state="readonly")
        Year_combo['values'] = ("Select Year", "FY", "SY", "TY")
        Year_combo.current(0)
        Year_combo.grid(row=0, column=3, padx=5, pady=15, sticky=W)

        # Semester
        sem_label = Label(Curr_course_frame, text="Semester", font=(
            "times new roman", 15, "bold"), bg="white")
        sem_label.grid(row=1, column=0, padx=10, sticky=W)

        Semester_combo = ttk.Combobox(Curr_course_frame, textvariable=self.var_Sem, font=(
            "times new roman", 15, "bold"), width=17, state="readonly")
        Semester_combo['values'] = (
            "Select Semester", "Sem-I", "Sem-II", "Sem-III", "Sem-IV", "Sem-V", "Sem-VI")
        Semester_combo.current(0)
        Semester_combo.grid(row=1, column=1, padx=5, pady=15, sticky=W)

        # Class Student Information
        Class_student_frame = LabelFrame(Left_frame, bd=4, bg="white", relief=RIDGE,
                                         text="Class Student Information", font=("times new roman", 18, "bold"))
        Class_student_frame.place(x=5, y=310, width=830, height=450)

        # Student ID
        stud_id_label = Label(Class_student_frame, text="Student ID:", font=(
            "times new roman", 15, "bold"), bg="white")
        stud_id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        student_entry = ttk.Entry(Class_student_frame, textvariable=self.var_Id, width=20, font=(
            "times new roman", 15, "bold"))
        student_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        stud_name_label = Label(Class_student_frame, text="Student Name:", font=(
            "times new roman", 15, "bold"), bg="white")
        stud_name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        stud_name_entry = ttk.Entry(Class_student_frame, textvariable=self.var_Name, width=20, font=(
            "times new roman", 15, "bold"))
        stud_name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Roll No
        roll_no_label = Label(Class_student_frame, text="Roll No:", font=(
            "times new roman", 15, "bold"), bg="white")
        roll_no_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(Class_student_frame, textvariable=self.var_RollNo, width=20, font=(
            "times new roman", 15, "bold"))
        roll_no_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Gender
        Gender_label = Label(Class_student_frame, text="Gender:", font=(
            "times new roman", 15, "bold"), bg="white")
        Gender_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        Gender_combo = ttk.Combobox(Class_student_frame, textvariable=self.var_Gender, font=(
            "times new roman", 15, "bold"), width=18, state="readonly")
        Gender_combo['values'] = ("Male", "Female", "Other")
        Gender_combo.current(0)
        Gender_combo.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        # Email
        Email_label = Label(Class_student_frame, text="Email:", font=(
            "times new roman", 15, "bold"), bg="white")
        Email_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        Email_entry = ttk.Entry(Class_student_frame, textvariable=self.var_Email, width=20, font=(
            "times new roman", 15, "bold"))
        Email_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Phone No
        PhoneNo_label = Label(Class_student_frame, text="Phone No:", font=(
            "times new roman", 15, "bold"), bg="white")
        PhoneNo_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        PhoneNo_entry = ttk.Entry(Class_student_frame, textvariable=self.var_PhoneNo, width=20, font=(
            "times new roman", 15, "bold"))
        PhoneNo_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Address
        Addr_label = Label(Class_student_frame, text="Address:", font=(
            "times new roman", 15, "bold"), bg="white")
        Addr_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        Addr_entry = ttk.Entry(Class_student_frame, textvariable=self.var_Address, width=20, font=(
            "times new roman", 15, "bold"))
        Addr_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Teacher Name
        Teacher_label = Label(Class_student_frame, text="Teacher Name:", font=(
            "times new roman", 15, "bold"), bg="white")
        Teacher_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        Teacher_entry = ttk.Entry(Class_student_frame, textvariable=self.var_Teacher, width=20, font=(
            "times new roman", 15, "bold"))
        Teacher_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # DOB
        DOB_label = Label(Class_student_frame, text="DOB:", font=(
            "times new roman", 15, "bold"), bg="white")
        DOB_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        DOB_entry = ttk.Entry(Class_student_frame, textvariable=self.var_DOB, width=20, font=(
            "times new roman", 15, "bold"))
        DOB_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Radio Buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(Class_student_frame, text="Take Photo Sample", variable=self.var_radio1,
                                    value="Yes")
        radiobtn1.grid(row=6, column=0)

        radiobtn2 = ttk.Radiobutton(Class_student_frame, text="No Photo Sample", variable=self.var_radio1,
                                    value="No")
        radiobtn2.grid(row=6, column=1)

        # button frame
        btn_frame = Frame(Class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=260, width=810, height=35)

        # save button
        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=18, font=(
            "times new roman", 13, "bold"), bg="White")
        save_btn.grid(row=0, column=0, padx=5)

        # Update button
        update_btn = Button(btn_frame, text="Update",command=self.update_data, width=18, font=(
            "times new roman", 13, "bold"), bg="White")
        update_btn.grid(row=0, column=1, padx=5)

        # Delete
        Delete_btn = Button(btn_frame, text="Delete", width=18, font=(
            "times new roman", 13, "bold"), bg="White")
        Delete_btn.grid(row=0, column=2, padx=5)

        # Reset Button
        reset_btn = Button(btn_frame, text="Reset", width=18, font=(
            "times new roman", 13, "bold"), bg="White")
        reset_btn.grid(row=0, column=3, padx=5)

        # button frame1
        btn_frame1 = Frame(Class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=5, y=320, width=810, height=35)

        # Take Photo Sample
        take_photo_samp_btn = Button(btn_frame1, text="Take Photo Sample", width=39, font=(
            "times new roman", 13, "bold"), bg="White")
        take_photo_samp_btn.grid(row=0, column=0, padx=3)

        update_photo_samp_btn = Button(btn_frame1, text="Upadate Photo Sample", width=39, font=(
            "times new roman", 13, "bold"), bg="White")
        update_photo_samp_btn.grid(row=0, column=1, padx=3)

        # right label frame
        Right_frame = LabelFrame(main_frame, bd=4, bg="white", relief=RIDGE,
                                 text="Student Deatils", font=("times new roman", 18, "bold"))
        Right_frame.place(x=950, y=10, width=900, height=800)

        # Frame Right
        img_right = Image.open(
            "C:/Users/Abhay/PycharmProjects/Advance_Face_Recognition_Project/Face_Recog_Images/Frame2.jpg")
        img_right = img_right.resize((900, 130), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=10, y=0, width=850, height=130)

        # ==============================================            SEARCH SYSTEM             =================================================

        # Search frame
        Search_frame = LabelFrame(Right_frame, bd=4, bg="white", relief=RIDGE,
                                  text="Search System", font=("times new roman", 18, "bold"))
        Search_frame.place(x=5, y=150, width=885, height=100)

        Search_label = Label(Search_frame, text="Search By:", font=(
            "times new roman", 15, "bold"), bg="Grey")
        Search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        Seacrh_combo = ttk.Combobox(Search_frame, font=(
            "times new roman", 15, "bold"), width=17, state="readonly")
        Seacrh_combo['values'] = ("Select", "Roll No", "Phone No")
        Seacrh_combo.current(0)
        Seacrh_combo.grid(row=0, column=1, padx=5, pady=15)

        search_entry = ttk.Entry(
            Search_frame, width=20, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=5, pady=15)

        # Search Button
        search_btn = Button(Search_frame, text="Search", width=16, font=(
            "times new roman", 13, "bold"), bg="White")
        search_btn.grid(row=0, column=3, padx=4)

        # Show All
        showAll_btn = Button(Search_frame, text="Show All", width=16, font=(
            "times new roman", 13, "bold"), bg="White")
        showAll_btn.grid(row=0, column=4, padx=4)

        # ====================================Table Frame=======================================
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=255, width=885, height=510)

        # Scroll Bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,
                                          columns=("Course", "Year", "Sem", "Id", "Name", "Roll No", "Gender",
                                                   "Email", "Phone No", "Address", "Teacher", "DOB"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Course", text="Course"),
        self.student_table.heading("Year", text="Year"),
        self.student_table.heading("Sem", text="Sem"),
        self.student_table.heading("Id", text="Id"),
        self.student_table.heading("Name", text="Name"),
        self.student_table.heading("Roll No", text="Roll No"),
        self.student_table.heading("Gender", text="Gender"),
        self.student_table.heading("Email", text="Email"),
        self.student_table.heading("Phone No", text="Phone No"),
        self.student_table.heading("Address", text="Address"),
        self.student_table.heading("Teacher", text="Teacher"),
        self.student_table.heading("DOB", text="DOB")

        self.student_table["show"] = "headings"

        self.student_table.column("Course", width=150),
        self.student_table.column("Year", width=150),
        self.student_table.column("Sem", width=150),
        self.student_table.column("Id", width=150),
        self.student_table.column("Name", width=150),
        self.student_table.column("Roll No", width=150),
        self.student_table.column("Gender", width=150),
        self.student_table.column("Email", width=150),
        self.student_table.column("Phone No", width=150),
        self.student_table.column("Address", width=150),
        self.student_table.column("Teacher", width=150),
        self.student_table.column("DOB", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()



    # Function Declaration

    def add_data(self):
        if self.var_Course.get() == "Select Course" or self.var_Id.get() == "" or self.var_Name.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="08052002H@ck",
                                               database="facerecognizer",auth_plugin="mysql_native_password")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                                         self.var_Course.get(),
                                                                                                         self.var_Year.get(),
                                                                                                         self.var_Sem.get(),
                                                                                                         self.var_Id.get(),
                                                                                                         self.var_Name.get(),
                                                                                                         self.var_RollNo.get(),
                                                                                                         self.var_Gender.get(),
                                                                                                         self.var_Email.get(),
                                                                                                         self.var_PhoneNo.get(),
                                                                                                         self.var_Address.get(),
                                                                                                         self.var_Teacher.get(),
                                                                                                         self.var_DOB.get(),
                                                                                                         self.var_radio1.get()
            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

        #fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="08052002H@ck",
                                           database="facerecognizer", auth_plugin="mysql_native_password")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()


        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

          #=====================get cursor=========================================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_Course.set(data[0]),
        self.var_Year.set(data[1]),
        self.var_Sem.set(data[2]),
        self.var_Id.set(data[3]),
        self.var_Name.set(data[4]),
        self.var_RollNo.set(data[5]),
        self.var_Gender.set(data[6]),
        self.var_Email.set(data[7]),
        self.var_PhoneNo.set(data[8]),
        self.var_Address.set(data[9]),
        self.var_Teacher.set(data[10]),
        self.var_DOB.set(data[11]),
        self.var_radio1.set(data[12])

    #update function
    def update_data(self):
        if self.var_Course.get() == "Select Course" or self.var_Name.get() == "" or self.var_Id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="08052002H@ck",
                                                   database="facerecognizer", auth_plugin="mysql_native_password")
                    my_cursor = conn.cursor()
                    my_cursor.execute("Update student set Course=%s,Year=%s,Sem=%s,Id=%s,Name=%s,RollNo=%s,Gender=%s,Email=%s,PhoneNo=%s,Address=%s,Teacher=%s,DOB=%s,PhotoSample=%s where Student Id=%s",(
                        self.var_Course.get(),
                        self.var_Year.get(),
                        self.var_Sem.get(),
                        self.var_Name.get(),
                        self.var_RollNo.get(),
                        self.var_Gender.get(),
                        self.var_Email.get(),
                        self.var_PhoneNo.get(),
                        self.var_Address.get(),
                        self.var_Teacher.get(),
                        self.var_DOB.get(),
                        self.var_radio1.get(),
                        self.var_Id.get()

                    ))

                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Details successfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)













        if __name__ == "__main__":
            root = Tk()
            obj = student(root)
            root.mainloop()
