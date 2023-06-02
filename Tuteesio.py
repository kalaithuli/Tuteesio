from tkinter import *
import mysql.connector as sqltor
from plyer import notification
import matplotlib.pyplot as plt
from tkinter import messagebox

# opening window
window1 = Tk()
window1.title("Our App")
window1.geometry('1050x1000')

# main window with the menu
def Main_Window():
    top1 = Toplevel(window1)
    top1.title("Tuteesio")
    top1.geometry('1050x500')
    filename = PhotoImage(file="C:\\Users\\Shivakumar\\Downloads\\Motivate-Me-master\login_background.png")
    background_label = Label(top1, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    btn1 = Button(top1, text="Profile", command=profile).place(x=330,y=5)
    btn2 = Button(top1, text="To-Do Lists", command=Open_window2).place(x=410,y=5)
    btn3 = Button(top1, text="Progress Report", command=Open_window3).place(x=520,y=5)
    btn4 = Button(top1, text='Exit', command=top1.destroy).place(x=650,y=5)
    hydrate()
    top1.mainloop()

# Sign Up Form
def Open_window1():
    global top4
    top4 = Toplevel()
    top4.geometry("500x1000+200+0")
    filename = PhotoImage(file="C:\\Users\\Shivakumar\\Downloads\\Bg.png")
    background_label = Label(top4, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    top4.title('SIGNUP FORM')

    label_0 = Label(top4, text="SIGNUP FORM", width=20, font=("bold", 20), fg='orange')
    label_0.config(bg='#223441')
    label_0.place(x=90, y=60)

    label_1 = Label(top4, text="Name", width=20, font=("bold", 10))
    label_1.place(x=80, y=130)
    global entry_1
    entry_1 = StringVar()
    Entry(top4,textvariable = entry_1).place(x=240, y=130)


    label_3 = Label(top4, text="Email", width=20, font=("bold", 10))
    label_3.place(x=68, y=180)
    global entry_3
    entry_3 = StringVar()
    Entry(top4,textvariable = entry_3).place(x=240, y=180)


    label_4 = Label(top4, text="Gender", width=20, font=("bold", 10))
    label_4.place(x=70, y=230)
    global var
    var = IntVar()
    Radiobutton(top4, text="Male", padx=5, variable=var, value=1).place(x=235, y=230)
    Radiobutton(top4, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)
    Radiobutton(top4, text="Other", padx=35, variable=var, value=3).place(x=370, y=230)


    label_5 = Label(top4, text="Country", width=20, font=("bold", 10))
    label_5.place(x=70, y=280)
    list_of_country = ['India', 'US', 'UK', 'Germany', 'Austria', 'France', 'Italy', 'Brazil']
    global c
    c = StringVar()
    droplist = OptionMenu(top4, c, *list_of_country )
    droplist.config(width=18)
    c.set('Select your Country')
    droplist.place(x=240, y=280)

    label_6 = Label(top4, text="Education", width=20, font=('bold', 10))
    label_6.place(x=75, y=330)
    global var1
    var1 = IntVar()
    Radiobutton(top4, text="School",padx=1, variable=var1 , value = 1 ).place(x=230, y=330)
    Radiobutton(top4, text="College",padx=20, variable=var1 , value = 2).place(x=290, y=330)
    global var3
    global var4
    global var5
    global var6
    global var7
    global var8
    global var9
    global var10
    global var11
    global var12
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    var10 = IntVar()
    var11 = IntVar()
    var12 = IntVar()
    label_7 = Label(top4, text="Subjects", width=20, font=('bold', 10))
    label_7.place(x=75, y=380)
    Checkbutton(top4, text="English", variable=var3).place(x=230, y=380)
    Checkbutton(top4, text="Physics", variable=var4).place(x=290, y=380)
    Checkbutton(top4, text="Hindi", variable=var5).place(x=230, y=400)
    Checkbutton(top4, text="Chemistry", variable=var6).place(x=290, y=400)
    Checkbutton(top4, text="Maths", variable=var7).place(x=230, y=420)
    Checkbutton(top4, text="Computer Science", variable=var8).place(x=290, y=420)

    label_8 = Label(top4, text="Address", width=20, font=("bold", 10))
    label_8.place(x=75, y=450)
    global entry8
    entry8 = StringVar()
    global entry9
    entry9 = StringVar()
    global entry10
    entry10 = StringVar()
    entry_8 = Entry(top4,textvariable = entry8)
    entry_8.place(x=240, y=450)
    entry_8 = Entry(top4, textvariable = entry9)
    entry_8.place(x=240, y=470)
    entry_8 = Entry(top4, textvariable = entry10)
    entry_8.place(x=240, y=490)

    label_9 = Label(top4, text="Choose the help", width=20, font=('bold', 10))
    label_9.place(x=75, y=510)
    Checkbutton(top4, text="Timetable", variable=var9).place(x=230, y=510)
    Checkbutton(top4, text="Progess Report", variable=var10).place(x=230, y=530)
    Checkbutton(top4, text="To do List", variable=var11).place(x=230, y=550)
    Checkbutton(top4, text="PieChart", variable=var12).place(x=230, y=570)

    global labelp
    labelp = Label(top4, text="Password", width=20, font=("bold", 10))
    labelp.place(x=75, y=600)
    labelp = StringVar()
    Entry(top4,textvariable = labelp).place(x=250, y=600)

    Button(top4, text='Submit', width=20, bg="black", fg='white',command=sql_tab).place(x=180, y=650)
    top4.mainloop()

# Linking Database
def sql_tab():
    global e2
    e2 = entry_3.get()
    pas = labelp.get()
    cs = False
    cc = False
    cn = False
    cp = False
    if (e2.endswith('.com')):
        for i in range(len(pas)):
            if pas[i] >= 'a' and pas[i] <= 'z':
                cs = 'True'
            if pas[i] >= 'A' and pas[i] <= 'Z':
                cc = 'True'
            if pas[i] >= '0' and pas[i] <= '9':
                cn = 'True'
            if pas[i] == '@' or pas[i] == '$':
                cp = 'True'
        if cs != 'True' or cc != 'True' or cn != 'True' or cp != 'True' :
            messagebox.showwarning("Warning", "Enter a valid password with number , capital and small letter and special characters - '@' or '$'")
        else :
            mycon = sqltor.connect(host='localhost', user='root', passwd='thuli@4132', database='TUT')
            if mycon.is_connected == False:
                print("Error connecting ")
            cursor = mycon.cursor()
            global e7, e8, e9, e10, e11, e12
            e1 = entry_1.get()

            e3 = var.get()
            e4 = c.get()
            e5 = var1.get()
            e6 = entry8.get() + " " + entry9.get() + " " + entry10.get()
            e7 = var3.get()
            e8 = var4.get()
            e9 = var5.get()
            e10 = var6.get()
            e11 = var7.get()
            e12 = var8.get()
            e13 = var9.get()
            e14 = var10.get()
            e15 = var11.get()
            e16 = var12.get()
            global e
            e = []
            ee = []

            # Gender
            if e3 == 1:
                egen = "Male"
            elif e3 == 2:
                egen = "Female"
            else:
                egen = "Other"

            # Education
            if e5 == 1:
                eedu = "School"
            else:
                eedu = "College"

            # Subjects
            esub = ["English", "Physics", "Hindi", "Chemistry", "Maths", "Computer Science"]
            if e7 != 0:
                e.append(esub[0])
            if e8 != 0:
                e.append(esub[1])
            if e9 != 0:
                e.append(esub[2])
            if e10 != 0:
                e.append(esub[3])
            if e11 != 0:
                e.append(esub[4])
            if e12 != 0:
                e.append(esub[5])
            es = ""
            for i in range(len(e)):
                es = es + " " + e[i]
            # Help
            ehelp = ["Timetable", "Progress Report", "To do List", "Pie Chart"]
            if e13 != 0:
                ee.append(ehelp[0])
            if e14 != 0:
                ee.append(ehelp[1])
            if e15 != 0:
                ee.append(ehelp[2])
            if e16 != 0:
                ee.append(ehelp[3])
            ees = ''
            for i in range(len(ee)):
                ees = ees + " " + ee[i]
            message = StringVar()
            print(e1, e2, egen, e4, eedu, e6, e, ee)
            data = (e1, e2, egen, e4, eedu, es, e6, ees, pas)
            insert_stmt = (
                "INSERT INTO STUD (Name , Email , Gender , Country , Education , Subjects , Address , Help , Password) "
                "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            cursor.execute(insert_stmt, data)
            print("Signed Up Successfully")
            message.set("Signed Up Successfully!")
            Label(top4, text="", textvariable=message).place(x=190, y=620)
            marks()
            mycon.commit()
    else:
        messagebox.showwarning("Warning","Enter a valid email")
# Total
def marks():
    global m
    global p
    global c
    global t
    global a
    global t1
    global t2
    win = Toplevel()
    win.title("Marks")
    win.geometry("1000x1000")
    win.maxsize(1000, 1000)
    win.minsize(1000, 1000)
    filename = PhotoImage(file="C:\\Users\\Shivakumar\\Downloads\\Bg.png")
    background_label = Label(win, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    # labels and texts

    l1 = Label(win, text="Name", font=("verdana", 12, "bold"), borderwidth=5).place(x = 80 , y = 150)
    t1 = Label(win, text =entry_1.get() ,borderwidth=7, width=20, font=("verdana 10 bold"))
    t1.place(x = 200 , y = 150)

    # marks space

    global eng1
    global phy1
    global hind1
    global chemistry1
    global math1
    global comp1
    Label(win, text="English", font=("verdana", 12, "bold"), borderwidth=5).place(x=475, y=150)
    eng1 = Entry(win, borderwidth=7, width=15, font=("verdana 10 bold"))
    eng1.place(x=590, y=150)

    Label(win, text="Physics", font=("verdana", 12, "bold"), borderwidth=5).place(x=475, y=210)
    phy1 = Entry(win, borderwidth=7, width=15, font=("verdana 10 bold"))
    phy1.place(x=590, y=210)

    Label(win, text="Hindi", font=("verdana", 12, "bold"), borderwidth=5).place(x=475, y=270)
    hind1 = Entry(win, borderwidth=7, width=15, font=("verdana 10 bold"))
    hind1.place(x=590, y=270)

    Label(win, text="Chemistry", font=("verdana", 12, "bold"), borderwidth=5).place(x=475, y=330)
    chemistry1 = Entry(win, borderwidth=7, width=15, font=("verdana 10 bold"))
    chemistry1.place(x=590, y=330)

    Label(win, text="Math", font=("verdana", 12, "bold"), borderwidth=5).place(x=475, y=390)
    math1 = Entry(win, borderwidth=7, width=15, font=("verdana 10 bold"))
    math1.place(x=590, y=390)

    Label(win, text="Computer", font=("verdana", 12, "bold"), borderwidth=5).place(x=475, y=450)
    comp1 = Entry(win, borderwidth=7, width=15, font=("verdana 10 bold"))
    comp1.place(x=590, y=450)

    # result space
    global total1
    global avg1
    global grade1
    total = Label(win, text="Total", font=("verdana", 12, "bold"), borderwidth=5).place(x=80, y=300)
    total1 = Entry(win, borderwidth=7, width=20, font=("verdana 10 bold"))
    total1.place(x=200, y=300)

    avg = Label(win, text="Average", font=("verdana", 12, "bold"), borderwidth=5).place(x=80, y=360)
    avg1 = Entry(win, borderwidth=7, width=20, font=("verdana 10 bold"))
    avg1.place(x=200, y=360)

    grade = Label(win, text="Grade", font=("verdana", 12, "bold"), borderwidth=5).place(x=80, y=420)
    grade1 = Entry(win, borderwidth=7, width=20, font=("verdana 10 bold"))
    grade1.place(x=200, y=420)

    # buttons

    calculate = Button(win, text="Calculate", width=12, borderwidth=5, font=("verdana 8 bold"), command=calc).place(
        x=200,
        y=550)

    clear = Button(win, text="Clear", width=12, borderwidth=5, font=("verdana 8 bold"), command=delete).place(x=350,
                                                                                                              y=550)
    piec = Button(win, text='Commit', width=20, borderwidth=5, font=("verdana 8 bold"), command=sql_tab1).place(
        x=500, y=550)

    win.mainloop()

def sql_tab1():
    mycon = sqltor.connect(host='localhost', user='root', passwd='thuli@4132', database='TUT')
    if mycon.is_connected == False:
        print("Error connecting ")
    cursor = mycon.cursor()
    data = (e2,(eng1.get()+ ' ' + phy1.get()+ ' ' +hind1.get()+ ' ' +chemistry1.get()+ ' ' +math1.get()+ ' ' +comp1.get()))
    insert_stmt = ("INSERT INTO STUDMARK (EMAIL,MARKS) "
                   "VALUES(%s,%s)")
    cursor.execute(insert_stmt, data)
    mycon.commit()

def calc():
    t = 0
    count = 0
    if eng1.get() != '0':
        en = float(eng1.get())
        t = t + en
        count = count + 1
    if phy1.get() != '0':
        ph = float(phy1.get())
        t = t + ph
        count = count + 1
    if hind1.get() != '0':
        hi = float(hind1.get())
        t = t + hi
        count = count + 1
    if chemistry1.get() != '0':
        ch = float(chemistry1.get())
        t = t + ch
        count = count + 1
    if math1.get() != '0':
        ma = float(math1.get())
        t = t + ma
        count = count + 1
    if comp1.get() != '0':
        co = float(comp1.get())
        t = t + co
        count = count + 1
    a = t / count
    total1.insert(0, t)
    avg1.insert(0, a)
    if (a >= 95):
        grade1.insert(0, "O")
    elif (a >= 90 and a < 95):
        grade1.insert(0, "A+")
    elif (a >= 80 and a < 90):
        grade1.insert(0, "A")
    elif (a >= 70 and a < 80):
        grade1.insert(0, "B+")
    elif (a >= 60 and a < 70):
        grade1.insert(0, "B")
    elif (a >= 50 and a < 60):
        grade1.insert(0, "C")
    elif (a >= 40 and a < 50):
        grade1.insert(0, "P")
    else:
        grade1.insert(0, "Fail")

def delete():
    math1.delete(0, 'end')
    phy1.delete(0, 'end')
    chemistry1.delete(0, 'end')
    eng1.delete(0, 'end')
    hind1.delete(0,'end')
    comp1.delete(0,'end')
    total1.delete(0, 'end')
    avg1.delete(0, 'end')
    grade1.delete(0, 'end')
    t1.delete(0, 'end')
    t2.delete(0, 'end')

# To-Do List
def Open_window2():

    connection = sqltor.connect(host="localhost", user="root", passwd="thuli@4132", database="TUT")
    sql_select_Query = "SELECT * FROM STUDMARK"
    cursor = connection.cursor()
    val = log1.get()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    for rows in records:
        global tasklist
        if (rows[0] == val):
            task_list = rows[2].split()
            print(task_list)
        else:
            continue

    def newTask():
        connection = sqltor.connect(host="localhost", user="root", passwd="thuli@4132", database="TUT")
        sql_select_Query = "SELECT * FROM STUDMARK"
        cursor = connection.cursor()
        val = log1.get()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for rows in records:
            if (rows[0] == val):
                task_list = rows[2].split()
                print(task_list)
            else:
                continue
        task = my_entry.get() + ' '
        if task != "":
            lb.insert(END, task)
            task_list.append(task)
            my_entry.delete(0, "end")
            upd(task_list)
        else:
            messagebox.showwarning("Warning", "Please enter some task.")

    def deleteTask():
        connection = sqltor.connect(host="localhost", user="root", passwd="thuli@4132", database="TUT")
        sql_select_Query = "SELECT * FROM STUDMARK"
        cursor = connection.cursor()
        val = log1.get()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for rows in records:
            if (rows[0] == val):
                task_list = rows[2].split()
                print(task_list)
            else:
                continue
        a=lb.get(ANCHOR)
        print(a)
        lb.delete(ANCHOR)
        task_list.remove(a)
        upd(task_list)

    def upd(task_list1):
        connection = sqltor.connect(host="localhost", user="root", passwd="thuli@4132", database="TUT")
        sql_select_Query = "SELECT * FROM STUDMARK"
        cursor = connection.cursor()
        val = log1.get()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print(records)
        tkl =''
        v = log1.get()
        sql_select_Query = "UPDATE STUDMARK SET TODO =%s WHERE EMAIL =%s"
        for i in range(len(task_list1)):
            tkl = tkl + task_list1[i] + ' '
        val = (tkl, v)
        cursor.execute(sql_select_Query, val)
        connection.commit()

    ws = Tk()
    ws.geometry('500x450+500+200')
    ws.title('ToDo List')
    ws.config(bg='#223441')
    ws.resizable(width=False, height=False)
    frame = Frame(ws)
    frame.pack(pady=10)

    lb = Listbox(
        frame,
        width=25,
        height=8,
        font=('Times', 18),
        bd=0,
        fg='#464646',
        highlightthickness=0,
        selectbackground='#a6a6a6',
        activestyle="none")
    lb.pack(side=LEFT, fill=BOTH)


    for item in task_list:
        lb.insert(END,item)

    sb = Scrollbar(frame)
    sb.pack(side=RIGHT, fill=BOTH)

    lb.config(yscrollcommand=sb.set)
    sb.config(command=lb.yview)

    my_entry = Entry(ws, font=('times', 24))
    my_entry.pack(pady=20)

    button_frame = Frame(ws)
    button_frame.pack(pady=20)

    addTask_btn = Button(button_frame, text='Add Task', font=('times 14'),
                         bg='#c5f776', padx=20, pady=10, command=newTask
                         )
    addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

    delTask_btn = Button(button_frame, text='Delete Task', font=('times 14'),
                         bg='#ff8b61', padx=20, pady=10, command=deleteTask)
    delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


    connection.commit()
    motivate1()
    ws.mainloop()

# Progress Report
def Open_window3():
    top3 = Toplevel()

    filename = PhotoImage(file="C:\\Users\\Shivakumar\\Downloads\\Motivate-Me-master\\music_background.png")
    background_label = Label(top3, image=filename)
    background_label.place(x=0, y=0)

    top3.title("Progress Report")
    top3.geometry('550x300')

    btn2 = Button(top3, text="Time You Need To Spend On Each Subject", command = piechart).place(x = 50 , y = 50)
    btn3 = Button(top3, text="Check Your Progress", command = prog).place(x = 50 , y = 80)
    btn1 = Button(top3, text="Back", command=top3.destroy)
    btn1.place(x=220, y=250)
    motivate2()
    top3.mainloop()

def piechart():
    Subjects = ["English" , "Physics" , "Hindi", "Chemistry" , "Maths" , "Computer Science"]
    # eng1.get(),phy1.get(),hind1.get(),chemistry1.get(),math1.get(),comp1.get()

    try:
        connection = sqltor.connect(host="localhost", user="root", passwd="thuli@4132", database="TUT")
        sql_select_Query = "SELECT * FROM STUDMARK"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()

        for row in records:
            a = row[1].split()
        for i in range(len(a)):
            a[i] = (105 - int(a[i]))

    except sqltor.Error as e:
        print("Error reading data from MySQL table", e)

    fig = plt.figure(figsize=(10, 7))
    plt.pie(a, labels=Subjects , autopct='%1.0f%%')
    plt.show()

# line



# Profile
def profile():
    my_w = Toplevel()
    filename = PhotoImage(file="C:\\Users\\Shivakumar\\Downloads\\Motivate-Me-master\\goals_background.png")
    background_label = Label(my_w, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    my_w.geometry('750x500')
    my_connect = sqltor.connect(host="localhost",user="root",passwd="thuli@4132",database="TUT")
    my_conn = my_connect.cursor()
    my_conn.execute("SELECT * FROM STUD ")

    e = Label(my_w, width=20, text='Name', borderwidth=2, relief='ridge', anchor='w')
    e.grid(row=0, column=3)
    e = Label(my_w, width=20, text='Email', borderwidth=2, relief='ridge', anchor='w')
    e.grid(row=1, column=3)
    e = Label(my_w, width=20, text='Gender', borderwidth=2, relief='ridge', anchor='w' )
    e.grid(row=2, column=3)
    e = Label(my_w, width=20, text='Country', borderwidth=2, relief='ridge', anchor='w' )
    e.grid(row=3, column=3)
    e = Label(my_w, width=20, text='Education', borderwidth=2, relief='ridge', anchor='w')
    e.grid(row=4, column=3)
    e = Label(my_w, width=20, text='Subjects', borderwidth=2, relief='ridge', anchor='w' )
    e.grid(row=5, column=3)
    e = Label(my_w, width=20, text='Address', borderwidth=2, relief='ridge', anchor='w')
    e.grid(row=6, column=3)
    e = Label(my_w, width=20, text='Help', borderwidth=2, relief='ridge', anchor='w' )
    e.grid(row=7, column=3)
    e = Label(my_w, width=20, text='Password', borderwidth=2, relief='ridge', anchor='w')
    e.grid(row=8, column=3)

    for student in my_conn:
        for k in student[1]:
            if student[1] == log1.get():
                for j in range(len(student)):
                    e = Label(my_w, width=50, text=student[j], borderwidth=2, relief='ridge', anchor="w", fg='blue')
                    e.grid(row=j, column=6)

    motivate()
    my_w.mainloop()

def login():
    win = Toplevel()
    win.title("Login")
    win.geometry("500x250")
    win.maxsize(500, 300)
    win.minsize(500, 300)

    filename = PhotoImage(file="C:\\Users\\Shivakumar\\Downloads\\Motivate-Me-master\\timetable_saved_background.png")
    background_label = Label(win, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    label_0 = Label(win, text="WELCOME TO TUTEESIO", font=("bold", 20), fg='orange')
    label_0.config(bg='#223441')
    label_0.place(x=90, y=60)

    global log1
    global log2
    label_1 = Label(win, text="Email", width=20, font=("bold", 10))
    label_1.place(x=80, y=130)
    log1 = StringVar()
    Entry(win, textvariable=log1).place(x=240, y=130)

    label_2 = Label(win, text="Password", width=20, font=("bold", 10))
    label_2.place(x=80, y=150)
    log2 = StringVar()
    Entry(win, textvariable=log2).place(x=240, y=150)

    btn = Button(win, text="Login", command=check).place(x=300 , y = 200)


def check():
    flag = False
    try:
        connection = sqltor.connect(host="localhost", user="root", passwd="thuli@4132", database="TUT")
        sql_select_Query = "SELECT * FROM STUD"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        record = cursor.fetchall()
        a = log1.get()
        b= log2.get()
        for row in record:
            if row[1] == a:
                flag = True
                if row[8] == b:
                    Main_Window()
                else :
                    messagebox.showwarning("Warning", "Wrong Password!")
        if flag == False:
            messagebox.showwarning("Warning", "Email does not exist!")
    except sqltor.Error as e:
        print("Error reading data from MySQL table", e)

def hydrate():
    notification.notify(
        title="Stay Hydrated!",
        message="The National Academies of Sciences determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) for men & 11.5 cups (2.7 liters) for women.",
        app_icon="C:\\Users\\Shivakumar\\Downloads\\Iconsmind-Outline-Glass-Water.ico",
        timeout=10
    )
def motivate():
    notification.notify(
        title="",
        message="The Secret Of Getting Ahead Is Getting Started!",
        app_icon="C:\\Users\\Shivakumar\\Downloads\\Iconsmind-Outline-Books-2.ico",
        timeout=10
    )
def motivate1():
    notification.notify(
        title="",
        message="The Key To Success Is To Focus On Goals , Not Obstacles!",
        app_icon="C:\\Users\\Shivakumar\\Downloads\\Designcontest-Outline-Sketch-Book.ico",
        timeout=10
    )
def motivate2():
    notification.notify(
        title="",
        message="Ask Yourself If What You Are Doing Today Is Getting You Closer To Where You Want To Be Tomorrow!",
        app_icon="C:\\Users\\Shivakumar\\Downloads\\Icons8-Windows-8-Sports-Running-Man.ico",
        timeout=10
    )
def prog():
    win = Toplevel()
    win.title("Marks Update")
    win.geometry("1000x1000")
    win.maxsize(1000, 1000)
    win.minsize(1000, 1000)
    filename = PhotoImage(file="C:\\Users\\Shivakumar\\Downloads\\Bg.png")
    background_label = Label(win, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    # labels and texts
    connection = sqltor.connect(host="localhost", user="root", passwd="thuli@4132", database="TUT")
    sql_select_Query = "SELECT * FROM STUDMARK"
    cursor = connection.cursor()
    val = log1.get()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    for rows in records:
        if(rows[0]==val):
            m = rows[1].split()
        else:
            continue

    lbl = Label(win,text="Old Marks", font=("verdana",12,"bold"),borderwidth=5).place(x=200,y=150)
    l2 = Label(win, text="English", font=("verdana", 12, "bold"), borderwidth=5).place(x=80, y=200)
    t2 = Label(win, text=m[0], borderwidth=7, width=20, font=("verdana 10 bold"))
    t2.place(x=200, y=200)

    l2 = Label(win, text="Physics", font=("verdana", 12, "bold"), borderwidth=5).place(x=80, y=260)
    t2 = Label(win, text=m[1], borderwidth=7, width=20, font=("verdana 10 bold"))
    t2.place(x=200, y=260)

    l3 = Label(win, text="Hindi", font=("verdana", 12, "bold"), borderwidth=5).place(x=80, y=320)
    t3 = Label(win, text=m[2], borderwidth=7, width=20, font=("verdana 10 bold"))
    t3.place(x=200, y=320)

    l4 = Label(win, text="Chemistry", font=("verdana", 12, "bold"), borderwidth=5).place(x=80, y=380)
    t4 = Label(win, text=m[3], borderwidth=7, width=20, font=("verdana 10 bold"))
    t4.place(x=200, y=380)

    l5 = Label(win, text="Math", font=("verdana", 12, "bold"), borderwidth=5).place(x=80, y=440)
    t5 = Label(win, text=m[4], borderwidth=7, width=20, font=("verdana 10 bold"))
    t5.place(x=200, y=440)

    l6 = Label(win, text="Computer", font=("verdana", 12, "bold"), borderwidth=5).place(x=80, y=500)
    t6 = Label(win, text=m[5], borderwidth=7, width=20, font=("verdana 10 bold"))
    t6.place(x=200, y=500)
    # marks space

    global eng2
    global phy2
    global hind2
    global chemistry2
    global math2
    global comp2

    lbl2 = Label(win,text="New Marks", font=("verdana",12,"bold"),borderwidth=5).place(x=475,y=150)
    eng2 = Entry(win, borderwidth=7, width=15, font=("verdana 10 bold"))
    eng2.place(x=475, y=200)

    phy2 = Entry(win, borderwidth=7, width=15, font=("verdana 10 bold"))
    phy2.place(x=475, y=260)

    hind2 = Entry(win, borderwidth=7, width=15, font=("verdana 10 bold"))
    hind2.place(x=475, y=320)

    chemistry2 = Entry(win, borderwidth=7, width=15, font=("verdana 10 bold"))
    chemistry2.place(x=475, y=380)

    math2 = Entry(win, borderwidth=7, width=15, font=("verdana 10 bold"))
    math2.place(x=475, y=440)

    comp2 = Entry(win, borderwidth=7, width=15, font=("verdana 10 bold"))
    comp2.place(x=475, y=500)

    # result space
    global total2
    global avg2
    global grade2
    total = Label(win, text="Total , Average , Grade", font=("verdana", 12, "bold"), borderwidth=5).place(x=80, y=560)
    total2 = Entry(win, borderwidth=7, width=20, font=("verdana 10 bold"))
    total2.place(x=200, y=600)

    avg2 = Entry(win, borderwidth=7, width=20, font=("verdana 10 bold"))
    avg2.place(x=400, y=600)

    grade2 = Entry(win, borderwidth=7, width=20, font=("verdana 10 bold"))
    grade2.place(x=600, y=600)
    global lbe
    global lbp
    global lbh
    global lbc
    global lbm
    global lba
    lbl3 = Label(win, text="Progress", font=("verdana", 12, "bold"), borderwidth=5).place(x=750, y=150)
    lbe = Entry(win, borderwidth=5 , font=("verdana 10 bold"))
    lbe.place(x=750, y=200)
    lbp= Entry(win, borderwidth=5 , font=("verdana 10 bold"))
    lbp.place(x=750, y=260)
    lbh= Entry(win, borderwidth=5, font=("verdana 10 bold"))
    lbh.place(x=750, y=320)
    lbc= Entry(win, borderwidth=5 , font=("verdana 10 bold"))
    lbc.place(x=750, y=380)
    lbm= Entry(win, borderwidth=5, font=("verdana 10 bold"))
    lbm.place(x=750, y=440)
    lba= Entry(win,  borderwidth=5, font=("verdana 10 bold"))
    lba.place(x=750, y=500)

    # buttons

    calculate = Button(win, text="Calculate", width=12, borderwidth=5, font=("verdana 8 bold"), command=calc1).place(x=200,y=640)

    clear = Button(win, text="Clear", width=12, borderwidth=5, font=("verdana 8 bold"), command=delete1).place(x=350,
                                                                                                              y=640)
    upd = Button(win, text='Update', width=20, borderwidth=5, font=("verdana 8 bold"), command=report).place(
        x=500, y=640)

    win.mainloop()
def report():
    try:
        connection = sqltor.connect(host="localhost", user="root", passwd="thuli@4132", database="TUT")
        cursor = connection.cursor()
        sql_select_Query = "UPDATE STUDMARK SET MARKS =%s WHERE EMAIL =%s"
        v = log1.get()
        val = ((eng2.get()+ ' ' + phy2.get()+ ' ' +hind2.get()+ ' ' +chemistry2.get()+ ' ' +math2.get()+ ' ' +comp2.get()),v)
        cursor.execute(sql_select_Query,val)
        connection.commit()
    except sqltor.Error as e:
        print("Error reading data from MySQL table", e)

def calc1():
    t = 0
    count = 0
    if eng2.get() != '0':
        en = float(eng2.get())
        t = t + en
        count = count + 1
    if phy2.get() != '0':
        ph = float(phy2.get())
        t = t + ph
        count = count + 1
    if hind2.get() != '0':
        hi = float(hind2.get())
        t = t + hi
        count = count + 1
    if chemistry2.get() != '0':
        ch = float(chemistry2.get())
        t = t + ch
        count = count + 1
    if math2.get() != '0':
        ma = float(math2.get())
        t = t + ma
        count = count + 1
    if comp2.get() != '0':
        co = float(comp2.get())
        t = t + co
        count = count + 1
    a = t / count
    total2.insert(0, t)
    avg2.insert(0, a)
    if (a >= 95):
        grade2.insert(0, "O")
    elif (a >= 90 and a < 95):
        grade2.insert(0, "A+")
    elif (a >= 80 and a < 90):
        grade2.insert(0, "A")
    elif (a >= 70 and a < 80):
        grade2.insert(0, "B+")
    elif (a >= 60 and a < 70):
        grade2.insert(0, "B")
    elif (a >= 50 and a < 60):
        grade2.insert(0, "C")
    elif (a >= 40 and a < 50):
        grade2.insert(0, "P")
    else:
        grade2.insert(0, "Fail")

    connection = sqltor.connect(host="localhost", user="root", passwd="thuli@4132", database="TUT")
    sql_select_Query = "SELECT * FROM STUDMARK"
    cursor = connection.cursor()
    val = log1.get()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    for rows in records:
        if (rows[0] == val):
            m = rows[1].split()
        else:
            continue

    ep = en - int(m[0])
    pp = ph - int(m[1])
    hp = hi - int(m[2])
    cp = ch - int(m[3])
    mp = ma - int(m[4])
    ap = co - int(m[5])
    lbe.insert(0,ep)
    lbp.insert(0,pp)
    lbh.insert(0,hp)
    lbc.insert(0,cp)
    lbm.insert(0,mp)
    lba.insert(0,ap)

    y1 = [int(m[0]),int(m[1]),int(m[2]),int(m[3]),int(m[4]),int(m[5])]
    x1 = [en , ph , hi , ch , ma , co]
    subjects = ["English" , "Physics", "Hindi" ,"Chemistry" , "Mathematics" , "Computer"]
    plt.plot(subjects,x1,label = "This term marks",marker='o',markerfacecolor='green')
    plt.plot(subjects,y1,label="Last term marks",marker='o',markerfacecolor='green')
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.title("Comparison")
    plt.legend()
    plt.show()


def delete1():
    math2.delete(0, 'end')
    phy2.delete(0, 'end')
    chemistry2.delete(0, 'end')
    eng2.delete(0, 'end')
    hind2.delete(0, 'end')
    comp2.delete(0, 'end')
    total2.delete(0, 'end')
    avg2.delete(0, 'end')
    grade2.delete(0, 'end')
    lbe.delete(0,'end')
    lbp.delete(0,'end')
    lbh.delete(0,'end')
    lbc.delete(0,'end')
    lbm.delete(0,'end')
    lba.delete(0,'end')

filename = PhotoImage(file="C:\\Users\\Shivakumar\\Downloads\\My project.png")
background_label = Label(window1, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
btn = Button(window1,borderwidth =5, text="LOG IN", fg = 'white', command=login)
btn.place(x = 450 , y = 10)
btn.config(bg='#223450')
btn1 = Button(window1,borderwidth =5, text="SIGN UP", fg = 'white' ,command=Open_window1)
btn1.place(x = 550 , y = 10)
btn1.config(bg='#223450')
window1.mainloop()
