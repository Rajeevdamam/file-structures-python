import tkinter as tk
from tkinter import Frame,Button,Label,Entry,PhotoImage,Text,WORD,Toplevel,StringVar
from tkinter.ttk import Combobox
import re
import json
window=tk.Tk()
window.title('STUDENT DATABASE SYSTEM')
#window.wm_attributes('-fullscreen','true')
frame=Frame(window)
stu_id=0

f=open("stud_file.txt",'r')
for line in f:
    stu_id+=1
pic=PhotoImage(file='C:\\Users\\raj\\Downloads\\UNI-CITY.png')
photo=Label(image=pic)
photo.pack()

def win1():
    top=Toplevel()
    top.title('Insert Student Details')
    key=Create(top)
    top.geometry('500x500')
    button = Button(top, text="Home", command=top.destroy,fg='white',bg='black')
    button.place(x=42,y=360)
    top.mainloop()

def win2():
    top = Toplevel()
    top.title('Search Student')
    key = Search(top)
    top.geometry('500x500')
    button = Button(top, text="Home", command=top.destroy,fg='white',bg='black')
    button.place(x=42,y=200)
    top.mainloop()
def win3():
    top = Toplevel()
    top.title('Delete Student')
    key = Delete(top)
    top.geometry('500x500')
    button = Button(top, text="Home", command=top.destroy,fg='white',bg='black')
    button.place(x=42,y=170)
    top.mainloop()

def win4():
    top = Toplevel()
    top.title('Edit Student Details')
    key = Edit(top)
    top.geometry('500x500')
    button = Button(top, text="Home", command=top.destroy,fg='white',bg='black')
    button.place(x=50,y=300)
    top.mainloop()

def win5():
    top = Toplevel()
    top.title('Display Student Details')
    key = Display(top)
    top.geometry('500x500')
    button = Button(top, text="Home", command=top.destroy,fg='white',bg='black')
    button.place(x=450,y=340)
    top.mainloop()


button1=Button(height=3,width=50,fg='white',bg='black')
button1['text']='Insert Student'
button1['command']=win1
button1.place(x=455,y=70)

button1=Button(height=3,width=50,fg='black',bg='snow')
button1['text']='Search Student'
button1['command']=win2
button1.place(x=455,y=160)

button1=Button(height=3,width=50,fg='white',bg='red')
button1['text']='Delete Student'
button1['command']=win3
button1.place(x=455,y=250)

button1=Button(height=3,width=50,fg='black',bg='deep sky blue')
button1['text']='Edit Student'
button1['command']=win4
button1.place(x=455,y=340)

button1=Button(height=3,width=50,fg='white',bg='black')
button1['text']='Display Students'
button1['command']=win5
button1.place(x=455,y=430)

button1=Button(height=3,width=50,fg='black',bg='red')
button1['text']='Quit'
button1['command']=quit
button1.place(x=455,y=520)




class Create(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.mybranch=StringVar()
        self.stusn = Label(self)
        self.stusn['text'] = 'Enter student USN:'
        self.stusn.grid(column=0,row=1)
        self.usn = Entry(self)
        self.usn.grid(column=0,row=2)
        self.stuname = Label(self)
        self.stuname['text']='Enter Student Name:'
        self.stuname.grid(column=0,row=3)
        self.name=Entry(self)
        self.name.grid(column=0,row=4)
        self.staddr = Label(self)
        self.staddr['text'] = 'Enter Student Address:'
        self.staddr.grid(column=0,row=5)
        self.addr = Entry(self)
        self.addr.grid(column=0,row=6)
        self.stsem = Label(self)
        self.stsem['text'] = 'Enter Student Semester:'
        self.stsem.grid(column=0,row=7)
        self.sem = Entry(self)
        self.sem.grid(column=0,row=8)
        self.stclg = Label(self)
        self.stclg['text'] = 'Enter student College:'
        self.stclg.grid(column=0, row=9)
        self.clg = Entry(self)
        self.clg.grid(column=0, row=10)
        self.branch=Label(self)
        self.branch['text']='Enter Student Branch:'
        self.branch.grid(column=0, row=11)
        self.combo = Combobox(self,textvariable=self.mybranch)
        self.combo['values'] = ('None of below','CSE','ME','ISE','CIVIL','ECE','EEE')
        self.combo.grid(column=0, row=12)
        self.button = Button(self,fg='white',bg='black')
        self.button['text']='Submit'
        self.button['command']=self.get_data
        self.msg = Text(self, width=30, height=5, wrap=WORD)
        self.msg.insert(0.0, " ")
        self.msg.grid(row=13, column=9)
        self.button.grid(column=0,row=15)

    def get_data(self):
        global stu_id
        studentpresent=get_student_details()
        usn = self.usn.get()
        name = self.name.get()
        address = self.addr.get()
        sem = self.sem.get()
        clg = self.clg.get()
        studentIndex = search_student(studentpresent, usn)
        if studentIndex>=0:
            self.msg.insert(0.0, "student already exists:")
        else:
            if usn=='' or name=='' or address=='' or sem=='' or clg=='':
                self.msg.insert(0.0, 'Please Enter All Details')
            elif len(usn) > 10:
                self.msg.insert(0.0, "Enter Maximum 10 Characters:")
            else:
                stu_id = stu_id + 1
                update_hash(usn,stu_id)
                f = open('stud_file.txt', 'a+')
                f.write("{stu_id}|{usn}|{name}|{address}|{sem}|{clg}|{branch}$\n".format(stu_id=stu_id, usn=self.usn.get(), name=self.name.get(), address=self.addr.get(), sem=self.sem.get(), clg=self.clg.get(),branch=self.combo.get()))
                self.msg.insert(0.0, "your student id is:" + str(stu_id ))
        print('success')

class Search(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.stusn = Label(self)
        self.stusn['text'] = 'Enter student USN:'
        self.stusn.grid(column=0, row=1)
        self.usn = Entry(self)
        self.usn.grid(column=0, row=2)
        self.button = Button(self,fg='black',bg='snow')
        self.button['text'] = 'Search'
        self.button['command'] = self.search_data
        self.button.grid(column=0, row=11)
        self.msg = Text(self, width=40, height=8, wrap=WORD)
        self.msg.grid(row=3, column=1)
    def search_data(self):
        global stu_id
        studentDetails = get_student_details()
        usn=self.usn.get()
        self.msg.delete('1.0', tk.END)
        studentIndex = search_student(studentDetails, usn)
        if(studentIndex >= 0):
            self.msg.insert(0.0, "ID:" + str(studentDetails[studentIndex][0])+'\n' +  "USN: " + usn +'\n'+"NAME:" + str(studentDetails[studentIndex][2])+'\n'+"ADDRESS:" + str(studentDetails[studentIndex][3])+'\n'+"SEMESTER:" + str(studentDetails[studentIndex][4])+'\n'+"COLLEGE:" + str(studentDetails[studentIndex][5])+'\n'+"BRANCH:" + str(studentDetails[studentIndex][6])+'\n')
        else:
            self.msg.insert(0.0, "Record Not Found!!"'\n')

class Delete(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.stusn = Label(self)
        self.stusn['text'] = 'Enter student USN:'
        self.stusn.grid(column=0, row=1)
        self.usn = Entry(self)
        self.usn.grid(column=0, row=2)
        self.button = Button(self,fg='white',bg='red')
        self.button['text'] = 'Delete'
        self.button['command'] = self.delete_data
        self.button.grid(column=0, row=11)
        self.msg = Text(self, width=30, height=5, wrap=WORD)
        self.msg.grid(row=3, column=1)
    def delete_data(self):
        global stu_id
        studentDetails = get_student_details()
        usn = self.usn.get()
        self.msg.delete('1.0', tk.END)
        studentIndex = search_student(studentDetails, usn)
        if studentIndex >= 0:
            del studentDetails[studentIndex]
            stu_id-=1
            save_student_data(studentDetails)
            self.msg.insert(0.0, "Record Deleted!!"'\n')
        else:
            self.msg.insert(0.0, "Record Not Found!!"'\n')
        return

class Edit(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.stusn = Label(self)
        self.stusn['text'] = 'Enter student USN to edit:'
        self.stusn.grid(column=0,row=1)
        self.usn = Entry(self)
        self.usn.grid(column=0,row=2)
        self.button1 = Button(self,fg='black',bg='deep sky blue')
        self.button1['text']='Check'
        self.button1['command']=self.edit_confirmation
        self.msg = Text(self, width=30, height=5, wrap=WORD)
        self.msg.insert(0.0, " ")
        self.msg.grid(row=13, column=1)
        self.button1.grid(column=0, row=13)
    def edit_confirmation(self):
        global stu_id
        studentDetails = get_student_details()
        usn = self.usn.get()
        studentIndex = search_student(studentDetails, usn)
        if (studentIndex >= 0):
            self.button1.destroy()
            self.msg.insert(0.0, 'RECORD FOUND!! Carry On With Your Editing:\n')
            self.button = Button(self, fg='black', bg='deep sky blue')
            self.button['text'] = 'Edit'
            self.button['command'] = self.edit_widgets
            self.button.grid(column=0, row=14)
        else:
            self.msg.insert(0.0, "Record Not Found!!"'\n')

    def edit_widgets(self):
        self.mybranch=StringVar()
        self.stuname = Label(self)
        self.stuname['text'] = 'Enter Student Name:'
        self.stuname.grid(column=0, row=3)
        self.name = Entry(self)
        self.name.grid(column=0, row=4)
        self.staddr = Label(self)
        self.staddr['text'] = 'Enter Student Address:'
        self.staddr.grid(column=0, row=5)
        self.addr = Entry(self)
        self.addr.grid(column=0, row=6)
        self.stsem = Label(self)
        self.stsem['text'] = 'Enter Student Semester:'
        self.stsem.grid(column=0, row=7)
        self.sem = Entry(self)
        self.sem.grid(column=0, row=8)
        self.stclg = Label(self)
        self.stclg['text'] = 'Enter student College:'
        self.stclg.grid(column=0, row=9)
        self.clg = Entry(self)
        self.clg.grid(column=0, row=10)
        self.branch = Label(self)
        self.branch['text'] = 'Enter Student Branch:'
        self.branch.grid(column=0, row=11)
        self.combo = Combobox(self, textvariable=self.mybranch)
        self.combo['values'] = ('None of below', 'CSE', 'ME', 'ISE', 'CIVIL', 'ECE', 'EEE')
        self.combo.grid(column=0, row=12)
        self.button = Button(self,fg='black',bg='deep sky blue')
        self.button['text'] = 'Edit'
        self.button['command'] = self.get_data
        self.msg = Text(self, width=30, height=5, wrap=WORD)
        self.msg.insert(0.0, " ")
        self.msg.grid(row=13, column=1)
        self.button.grid(column=0, row=14)
    def get_data(self):
        global stu_id
        studentDetails = get_student_details()
        usn = self.usn.get()
        name = self.name.get()
        address = self.addr.get()
        sem = self.sem.get()
        clg = self.clg.get()
        self.msg.delete('1.0', tk.END)
        studentIndex = search_student(studentDetails, usn)
        if (studentIndex >= 0):
            if usn=='' or name=='' or address=='' or sem=='' or clg=='':
                self.msg.insert(0.0, 'Please Enter All Details')
            elif len(usn) > 10:
                self.msg.insert(0.0, "Enter Minimum 10 Characters:")
            else:
                studentDetails[studentIndex] = [str(studentDetails[studentIndex][0]),self.usn.get(),self.name.get(), self.addr.get(), self.sem.get(), self.clg.get(),self.combo.get()]
                save_student_data(studentDetails)
                print(studentDetails)
                self.msg.insert(0.0, "Student record edited is:" + str(studentDetails[studentIndex][0]))

class Display(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.msg = Text(self, width=180, height=15, wrap=WORD)
        self.msg.insert(0.0, " ")
        self.msg.grid(row=12, column=10)
        self.msg['command']=self.display_students()
    def display_students(self):
        global stu_id
        student_details = get_student_details()
        student_details = list_to_json(student_details)
        student_details = json_to_str_table(student_details)
        self.msg.insert(0.0, "The Student Details Are: \n\n" + str(student_details)+'\n')

def list_to_json(student_details):
    student_details_json = []
    for student in student_details:
        studentObj = {}
        studentObj['id'] = student[0]
        studentObj['usn'] = student[1]
        studentObj['name'] = student[2]
        studentObj['address'] = student[3]
        studentObj['semester'] = student[4]
        studentObj['college'] = student[5]
        studentObj['branch'] = student[6]
        student_details_json.append(studentObj)
    return student_details_json


def json_to_str_table(student_details):
    table_content = "ID\t\t|\tUSN\t\t|\tName\t\t|\tAddress\t\t|\tSemester\t\t|\tCollege\t\t|\tBranch\t| \n"
    for student in student_details:
        table_content += "{stu_id}\t\t|\t{usn}\t\t|\t{name}\t\t|\t{address}\t\t|\t{sem}\t\t|\t{clg}\t\t|\t{branch}\t| \n".format(stu_id=student['id'], usn=student['usn'], name=student['name'], address=student['address'], sem=student['semester'], clg=student['college'],branch=student['branch'])
    return table_content

def get_student_details():
    f = open("stud_file.txt", 'r').read()
    f = re.split("[" + "\\".join("$\\n") + "]", f)[:-2]
    f = filter(None, f)
    studentDetails = [re.split("[" + "\\".join("|") + "]", student) for student in f]
    return studentDetails

def save_student_data(student_details):
    student_details.append([])
    s="$\n".join(['|'.join(students) for students in student_details])
    savefile=open("stud_file.txt", 'w')
    savefile.write(s)
    return s

def search_student(studentDetails, usn):
    with open('hash_file.json') as hash_file:
        hash_data = json.load(hash_file)
    if(usn in hash_data):
        return hash_data[usn]
    else:
        return -1

def update_hash(usn,index = None):
    hash_data = {}
    with open('hash_file.json') as hash_file:
        hash_data = json.load(hash_file)
    if(index):
        hash_data[usn] = index - 1
        with open('hash_file.json', 'w') as hash_file:
            json.dump(hash_data, hash_file)
    else:
        del hash_data[usn]

def reindex_data():
    student_details = get_student_details()
    hash_data = {}
    for idx, student in enumerate(student_details):
        hash_data[student[1]] = idx
    with open('hash_file.json', 'w') as hash_file:
        json.dump(hash_data, hash_file)

reindex_data()
window.mainloop()
