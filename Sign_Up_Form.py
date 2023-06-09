from tkinter import *
import mysql.connector as sqltor

root = Tk()
root.geometry("500x1000+200+0")
c = Canvas(root, bg="gray16", height=10, width=10)
filename = PhotoImage(file="C:\\Users\\Shivakumar\\Downloads\\Bg.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.title('SIGNUP FORM')

label_0 = Label(root, text="SIGNUP FORM", width=20, font=("bold", 20), fg='orange')
label_0.config(bg='#223441')
label_0.place(x=90, y=60)

label_1 = Label(root, text="Name", width=20, font=("bold", 10))
label_1.place(x=80, y=130)
entry_1 = Entry(root)
entry_1.place(x=240, y=130)

label_3 = Label(root, text="Email", width=20, font=("bold", 10))
label_3.place(x=68, y=180)
entry_3 = Entry(root)
entry_3.place(x=240, y=180)

label_4 = Label(root, text="Gender", width=20, font=("bold", 10))
label_4.place(x=70, y=230)
var = IntVar()
Radiobutton(root, text="Male", padx=5, variable=var, value=1).place(x=235, y=230)
Radiobutton(root, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)
Radiobutton(root, text="Other", padx=35, variable=var, value=3).place(x=370, y=230)

label_5 = Label(root, text="Country", width=20, font=("bold", 10))
label_5.place(x=70, y=280)
list_of_country = ['India', 'US', 'UK', 'Germany', 'Austria', 'France', 'Italy', 'Brazil']
c = StringVar()
droplist = OptionMenu(root, c, *list_of_country)
droplist.config(width=18)
c.set('Select your Country')
droplist.place(x=240, y=280)

label_6 = Label(root, text="Education", width=20, font=('bold', 10))
label_6.place(x=75, y=330)
var1 = IntVar()
Checkbutton(root, text="School", variable=var1).place(x=230, y=330)
var2 = IntVar()
Checkbutton(root, text="College", variable=var2).place(x=290, y=330)
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
label_7 = Label(root, text="Subjects", width=20, font=('bold', 10))
label_7.place(x=75, y=380)
Checkbutton(root, text="English", variable=var3).place(x=230, y=380)
Checkbutton(root, text="Physics", variable=var4).place(x=290, y=380)
Checkbutton(root, text="Hindi", variable=var5).place(x=230, y=400)
Checkbutton(root, text="Chemistry", variable=var6).place(x=290, y=400)
Checkbutton(root, text="Maths", variable=var7).place(x=230, y=420)
Checkbutton(root, text="Computer Science", variable=var8).place(x=290, y=420)

label_8 = Label(root, text="Address", width=20, font=("bold", 10))
label_8.place(x=75, y=450)
entry_8 = Entry(root)
entry_8.place(x=240, y=450)
entry_8 = Entry(root)
entry_8.place(x=240, y=470)
entry_8 = Entry(root)
entry_8.place(x=240, y=490)

label_9 = Label(root, text="Choose the help", width=20, font=('bold', 10))
label_9.place(x=75, y=510)
Checkbutton(root, text="Timetable", variable=var9).place(x=230, y=510)
Checkbutton(root, text="Progess Report", variable=var10).place(x=230, y=530)
Checkbutton(root, text="To do List", variable=var11).place(x=230, y=550)
Checkbutton(root, text="PieChart", variable=var12).place(x=230, y=570)

Button(root, text='Submit', width=20, bg="black", fg='white').place(x=180, y=600)

root.mainloop()
