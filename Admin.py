import cv2,os
import numpy as np
from collections import Counter
import threading
from Tkinter import *
import datetime



def takeImageFun():
    
    global rightFrameADD,btnPress, idEntry, batchEntry, sectionEntry
    btnPress = btnPress + 1
    if (btnPress != 0):
        list = rightFrameADD.grid_slaves()
        for l in list:
            l.destroy()
    idEntry = StringVar()
    batchEntry = StringVar()
    sectionEntry = StringVar()
    
    Label(rightFrameADD, text="ID :", font='none 12 bold', fg='white', bg='#232F3B').grid(row=1, padx=(30, 30), pady=(30, 30))
    tafEntry1 = Entry(rightFrameADD, width=40, textvariable = idEntry).grid(row=1, column=1, ipady=5, padx=(30, 30), pady=(30, 30))

    Label(rightFrameADD, text="Batch :", font='none 12 bold', fg='white', bg='#232F3B').grid(row=2, padx=(30, 30), pady=(30, 30))
    tafEntry2 = Entry(rightFrameADD, width=40, textvariable = batchEntry).grid(row=2, column=1, ipady=5, padx=(30, 30), pady=(30, 30))

    Label(rightFrameADD, text="Section :", font='none 12 bold', fg='white', bg='#232F3B').grid(row=3, padx=(30, 30), pady=(30, 30))
    tafEntry3 = Entry(rightFrameADD, width=40, textvariable = sectionEntry).grid(row=3, column=1, ipady=5, padx=(30, 30), pady=(30, 30))

    takeImageBTN = Button(rightFrameADD, bg="#3b8bbc", fg="white", text="Submit", font="none 10 bold", width=20, height=2, command=takeImageFun).grid(row=4, column=1, ipady=5, padx=(30, 30), pady=(30, 30))

    
def takeReplaceFun():
    global rightFrameADD,btnPress, idEntry, batchEntry, sectionEntry
    btnPress = btnPress + 1
    if (btnPress != 0):
        list = rightFrameADD.grid_slaves()
        for l in list:
            l.destroy()
    idEntry = StringVar()
    batchEntry = StringVar()
    sectionEntry = StringVar()
    
    Label(rightFrameADD, text="R.ID :", font='none 12 bold', fg='white', bg='#232F3B').grid(row=1, padx=(30, 30), pady=(30, 30))
    tafEntry1 = Entry(rightFrameADD, width=40, textvariable = idEntry).grid(row=1, column=1, ipady=5, padx=(30, 30), pady=(30, 30))

    Label(rightFrameADD, text="R.Batch :", font='none 12 bold', fg='white', bg='#232F3B').grid(row=2, padx=(30, 30), pady=(30, 30))
    tafEntry2 = Entry(rightFrameADD, width=40, textvariable = batchEntry).grid(row=2, column=1, ipady=5, padx=(30, 30), pady=(30, 30))

    Label(rightFrameADD, text="R.Section :", font='none 12 bold', fg='white', bg='#232F3B').grid(row=3, padx=(30, 30), pady=(30, 30))
    tafEntry3 = Entry(rightFrameADD, width=40, textvariable = sectionEntry).grid(row=3, column=1, ipady=5, padx=(30, 30), pady=(30, 30))

    replaceImageBTN = Button(rightFrameADD, bg="#3b8bbc", fg="white", text="Replace", font="none 10 bold", width=20, height=2, command=takeReplaceFun).grid(row=4, column=1, ipady=5, padx=(30, 30), pady=(30, 30))

def advisorInterface(advisorName):
    global app, rightFrameADD, btnPress
    btnPress = 0
    topFrameWC = Frame(app, borderwidth=1, relief="solid")
    topFrameWC.pack(expand=False, fill="both")
    topFrameWC.configure(background="#232F3B")

    leftFrameBTN = Frame(app, borderwidth=1, relief="solid")
    leftFrameBTN.pack(side='left', expand=False, fill="both")
    leftFrameBTN.configure(background="#232F3B")

    rightFrameADD = Frame(app, borderwidth=1, relief="solid")
    rightFrameADD.pack(side='right', expand=True, fill="both")
    rightFrameADD.configure(background="#232F3B")
    
    list = app.grid_slaves()
    for l in list:
        l.destroy()
        
    print "Hello admin"
    teacherID = userIdField.get()
    Label(topFrameWC, text='Welcome Advisor: ' + advisorName, fg='white', bg='#232F3B', font='none 10 bold').grid(row=0, column=4, pady=(10, 10), padx=(100, 100))

    Button(topFrameWC, bg="#232F3B", fg="white", text="Logout", font="none 10 bold", width=10, height=1, command=signoutCommand).grid(row=0, column=5, pady=(10, 10))
    
    #Advisor button .....................................
    studentAssignBTN = Button(leftFrameBTN, bg="#3b8bbc", fg="white", text="Assign Student",relief=RAISED, borderwidth=1, font="none 10 bold", width=20, height=2, command=studentAssignFun).grid(row=1, column=3, padx=(10, 10), pady=(40, 10))
    takeImageBTN = Button(leftFrameBTN, bg="#3b8bbc", fg="white", text="Take Image",relief=RAISED, borderwidth=1, font="none 10 bold", width=20, height=2, command=takeImageFun).grid(row=2, column=3, padx=(10, 10), pady=(40, 10))
    replaceImageBTN = Button(leftFrameBTN, bg="#3b8bbc", fg="white", text="Replace Image", font="none 10 bold", width=20, height=2, command=takeReplaceFun).grid(row=3, column=3, padx=(10, 10), pady=(40, 10))
    


def studentDetailsBTN():
    global rightFrameADD
    print "Done"        
    checkStatus=0

    idEntryD = idEntry.get()
    nameEntryD = nameEntry.get()
    phoneEntryD = phoneEntry.get()
    
    emailEntryD = emailEntry.get()
    fatherEntryD = fatherEntry.get()
    fPhoneEntryD = fPhoneEntry.get()
    motherEntryD = motherEntry.get()
    
    facultyEntryD = facultyEntry.get()
    programEntryD = programEntry.get()
    
    batchEntryD = batchEntry.get()
    enrollEntryD = enrollEntry.get()
    presentEntryD = presentEntry.get()
    
    villageEntryD = villageEntry.get()
    postEntryD = postEntry.get()
    postNoEntryD = postNoEntry.get()
    
    thanaEntryD = thanaEntry.get()
    districtEntryD = districtEntry.get()    
    
    if (idEntryD != '' and nameEntryD != '' and phoneEntryD != '' and fatherEntryD != '' and fPhoneEntryD != '' and motherEntryD != '' and programEntryD != '' and batchEntryD != '' and enrollEntryD != ''):
        import pymysql
        conn = pymysql.connect("localhost","root","","project")
        assignR = conn.cursor()
        show = conn.cursor()
        show.execute("select * from student_details")
        
        for showR in show:
            
            if (idEntryD == showR[0]):
                checkStatus=1
        if(checkStatus != 1):        
            
            insertStudentDetails = "insert into student_details(id,name,phone_no,email,father_name,father_phone_no,mother_name,faculty,program,batch,enrollment,present_address,village,post_office,post_code,thana,district) values ('"+idEntryD+"','"+nameEntryD+"','"+phoneEntryD+"','"+emailEntryD+"','"+fatherEntryD+"','"+fPhoneEntryD+"','"+motherEntryD+"','"+facultyEntryD+"','"+programEntryD+"','"+batchEntryD+"','"+enrollEntryD+"','"+presentEntryD+"','"+villageEntryD+"','"+postEntryD+"','"+postNoEntryD+"','"+thanaEntryD+"','"+districtEntryD+"')";
            assignR.execute(insertStudentDetails)        
            conn.commit()
        conn.close()
    

def studentDetailsFun():
    global rightFrameADD,btnPress, idEntry, nameEntry, phoneEntry, emailEntry, fatherEntry, fPhoneEntry, motherEntry, facultyEntry, programEntry, batchEntry, enrollEntry, presentEntry, villageEntry, postEntry, postNoEntry, thanaEntry, districtEntry
    btnPress = btnPress + 1
    if (btnPress != 0):
        list = rightFrameADD.grid_slaves()
        for l in list:
            l.destroy()
    idEntry = StringVar()
    nameEntry = StringVar()
    phoneEntry = StringVar()
    emailEntry = StringVar()
    
    fatherEntry = StringVar()
    fPhoneEntry = StringVar()
    motherEntry = StringVar()
    
    facultyEntry = StringVar()
    programEntry = StringVar()
    batchEntry = StringVar()
    enrollEntry = StringVar()
    
    presentEntry = StringVar()
    
    villageEntry = StringVar()
    postEntry = StringVar()
    postNoEntry = StringVar()
    thanaEntry = StringVar()
    districtEntry = StringVar()
    
    
    Label(rightFrameADD, text="ID :", font='none 12 bold', fg='white', bg='#232F3B').grid(row=1)
    tafEntry1 = Entry(rightFrameADD, width=40, textvariable = idEntry).grid(row=1, column=1)

    Label(rightFrameADD, text="Name :", font='none 12 bold', fg='white', bg='#232F3B').grid(row=2)
    tafEntry2 = Entry(rightFrameADD, width=40, textvariable = nameEntry).grid(row=2, column=1)

    Label(rightFrameADD, text="Phone No :", font='none 12 bold', fg='white', bg='#232F3B').grid(row=3)
    tafEntry3 = Entry(rightFrameADD, width=40, textvariable = phoneEntry).grid(row=3, column=1)

    Label(rightFrameADD, text="Email :", font='none 12 bold', fg='white', bg='#232F3B').grid(row=4)
    tafEntry4 = Entry(rightFrameADD, width=40, textvariable = emailEntry).grid(row=4, column=1)

    Label(rightFrameADD, font='none 12 bold', fg='white', bg='#232F3B').grid(row=5)


    Label(rightFrameADD,text='Father name :', font='none 12 bold', fg='white', bg='#232F3B').grid(row=6, padx=(10, 10))
    tafEntry5 = Entry(rightFrameADD, width=40, textvariable = fatherEntry).grid(row=6, column=1, padx=(10, 10))

    Label(rightFrameADD, text="Father Phone No :", font='none 12 bold', fg='white', bg='#232F3B').grid(row=7, padx=(10, 10))
    tafEntry6 = Entry(rightFrameADD, width=40, textvariable = fPhoneEntry).grid(row=7, column=1, padx=(10, 10))

    Label(rightFrameADD, text="Mother Name :", font='none 12 bold', fg='white', bg='#232F3B').grid(row=8, padx=(10, 10))
    tafEntry7 = Entry(rightFrameADD, width=40, textvariable = motherEntry).grid(row=8, column=1, padx=(10, 10))


    Label(rightFrameADD, font='none 12 bold', fg='white', bg='#232F3B').grid(row=9, padx=(10, 10))
    

    Label(rightFrameADD, text="Faculty :", font='none 12 bold', fg='white', bg='#232F3B').grid(row=10, padx=(10, 10))
    tafEntry8 = Entry(rightFrameADD, width=40, textvariable = facultyEntry).grid(row=10, column=1, padx=(10, 10))

    Label(rightFrameADD, text="Program :", font='none 12 bold', fg='white', bg='#232F3B').grid(row=11, padx=(10, 10))
    tafEntry9 = Entry(rightFrameADD, width=40, textvariable = programEntry).grid(row=11, column=1, padx=(10, 10))

    Label(rightFrameADD, text="Batch :", font='none 12 bold', fg='white', bg='#232F3B').grid(row=12, padx=(10, 10))
    tafEntry10 = Entry(rightFrameADD, width=40, textvariable = batchEntry).grid(row=12, column=1, padx=(10, 10))

    Label(rightFrameADD, text="Enrollment :", font='none 12 bold', fg='white', bg='#232F3B').grid(row=13, padx=(10, 10))
    tafEntry11 = Entry(rightFrameADD, width=40, textvariable = enrollEntry).grid(row=13, column=1, padx=(10, 10))


    Label(rightFrameADD, font='none 12 bold', fg='white', bg='#232F3B').grid(row=14, padx=(10, 10))

    

    Label(rightFrameADD, text="Present Address :", font='none 12 bold', fg='white', bg='#232F3B').grid(row=15, padx=(10, 10))
    tafEntry12 = Entry(rightFrameADD, width=40, textvariable = presentEntry).grid(row=15, column=1, ipady=10, padx=(10, 10))


    Label(rightFrameADD, font='none 12 bold', fg='white', bg='#232F3B').grid(row=16) 

    Label(rightFrameADD, text='Permanent Address', font='none 12 bold', fg='white', bg='#232F3B').grid(row=17, column=1) 
    
    Label(rightFrameADD, text="Village :", font='none 12 bold', fg='white', bg='#232F3B').grid(row=18, padx=(10, 10))
    tafEntry13 = Entry(rightFrameADD, width=40, textvariable = villageEntry).grid(row=18, column=1, padx=(10, 10))

    Label(rightFrameADD, text="Post Office :", font='none 12 bold', fg='white', bg='#232F3B').grid(row=19, padx=(10, 10))
    tafEntry14 = Entry(rightFrameADD, width=40, textvariable = postEntry).grid(row=19, column=1, padx=(10, 10))

    Label(rightFrameADD, text="Post Code :", font='none 12 bold', fg='white', bg='#232F3B').grid(row=20, padx=(10, 10))
    tafEntry15 = Entry(rightFrameADD, width=40, textvariable = postNoEntry).grid(row=20, column=1, padx=(10, 10))

    Label(rightFrameADD, text="Thana :", font='none 12 bold', fg='white', bg='#232F3B').grid(row=21, padx=(10, 10))
    tafEntry16 = Entry(rightFrameADD, width=40, textvariable = thanaEntry).grid(row=21, column=1, padx=(10, 10))

    Label(rightFrameADD, text="District :", font='none 12 bold', fg='white', bg='#232F3B').grid(row=22, padx=(10, 10))
    tafEntry17 = Entry(rightFrameADD, width=40, textvariable = districtEntry).grid(row=22, column=1, padx=(10, 10))


    Button(rightFrameADD, bg="#3b8bbc", fg="white", text="Submit", font="none 10 bold", width=18, height=2, command=studentDetailsBTN).grid(row=23, column=1, padx=(10, 10), pady=(10, 10))





def courseDetailsBTN():
    global rightFrameADD
    print "Done"
        
    checkStatus=0
    takeCourseID = courseID.get()
    takeCourseName = courseName.get()
    takeCourseCredit = courseCredit.get()
    
    if (takeCourseID != '' and takeCourseName != '' and takeCourseCredit != ''):
        import pymysql
        conn = pymysql.connect("localhost","root","","project")
        assignR = conn.cursor()
        show = conn.cursor()
        show.execute("select * from course_details")
        
        for showR in show:
            
            if (takeCourseID == showR[0]):
                checkStatus=1
        if(checkStatus != 1):
            insertCourseDetails = "insert into course_details(id,course_name,credit) values ('"+takeCourseID+"','"+takeCourseName+"','"+takeCourseCredit+"')";
            assignR.execute(insertCourseDetails)        
            conn.commit()
        conn.close()


def courseDetailsFun():
    global rightFrameADD, courseID, courseName, courseCredit, btnPress
    btnPress = btnPress + 1
    if (btnPress != 0):
        list = rightFrameADD.grid_slaves()
        for l in list:
            l.destroy()
    
    courseID = StringVar()
    courseName = StringVar()
    courseCredit = StringVar()
    
    
    Label(rightFrameADD, text="Course Code :", font='none 14 bold', fg='white', bg='#232F3B').grid(row=5, padx=(10, 10), pady=(40, 10))
    tafEntry1 = Entry(rightFrameADD, width=40, textvariable = courseID).grid(row=5, ipady=5, column=1, padx=(10, 10), pady=(40, 10))

    Label(rightFrameADD, text="Course Name :", font='none 14 bold', fg='white', bg='#232F3B').grid(row=6, padx=(10, 10), pady=(40, 10))
    tafEntry2 = Entry(rightFrameADD, width=40, textvariable = courseName).grid(row=6, column=1, ipady=5, padx=(10, 10), pady=(40, 10))

    Label(rightFrameADD, text="Credit :", font='none 14 bold', fg='white', bg='#232F3B').grid(row=7, padx=(10, 10), pady=(40, 10))
    tafEntry3 = Entry(rightFrameADD, width=40, textvariable = courseCredit).grid(row=7, column=1, ipady=5, padx=(10, 10), pady=(40, 10))

    Button(rightFrameADD, bg="#3b8bbc", fg="white", text="Submit", font="none 10 bold", width=18, height=2, command=courseDetailsBTN).grid(row=10, column=1, padx=(10, 10), pady=(40, 10))




def teacherAssignBTN():
    global rightFrameADD
    print "Done"
        
    checkStatus=0
    tafTeacherID = teacherIDtaf.get()
    tafCourseCode = courseCodetaf.get()
    tafSection = sectiontaf.get()
    tafBatch = batchtaf.get()
    if (tafTeacherID != '' and tafCourseCode != '' and tafSection != '' and tafBatch != ''):
        import pymysql
        conn = pymysql.connect("localhost","root","","project")
        assignR = conn.cursor()
        show = conn.cursor()
        show.execute("select * from teacher_assign")
        
        for showR in show:
            
            if (tafTeacherID == showR[1] and tafCourseCode == showR[2] and tafSection == showR[3] and tafBatch == showR[4]):
                checkStatus=1
        if(checkStatus != 1):
            insertTeacherAssign = "insert into teacher_assign(teacher_id,course_id,section,batch) values ('"+tafTeacherID+"','"+tafCourseCode+"','"+tafSection+"','"+tafBatch+"')";
            assignR.execute(insertTeacherAssign)        
            conn.commit()
        conn.close()


def teacherAssignFun():
    global rightFrameADD, teacherIDtaf, courseCodetaf, sectiontaf, batchtaf, btnPress
    btnPress = btnPress + 1
    if (btnPress != 0):
        list = rightFrameADD.grid_slaves()
        for l in list:
            l.destroy()
    teacherIDtaf = StringVar()
    courseCodetaf = StringVar()
    sectiontaf = StringVar()
    batchtaf = StringVar()
    
    
    Label(rightFrameADD, text="Teacher ID :", font='none 14 bold', fg='white', bg='#232F3B').grid(row=5, padx=(10, 10), pady=(40, 10))
    tafEntry1 = Entry(rightFrameADD, width=40, textvariable = teacherIDtaf).grid(row=5, ipady=5, column=1, padx=(10, 10), pady=(40, 10))

    Label(rightFrameADD, text="Course Code :", font='none 14 bold', fg='white', bg='#232F3B').grid(row=6, padx=(10, 10), pady=(40, 10))
    tafEntry2 = Entry(rightFrameADD, width=40, textvariable = courseCodetaf).grid(row=6, column=1, ipady=5, padx=(10, 10), pady=(40, 10))

    Label(rightFrameADD, text="Section :", font='none 14 bold', fg='white', bg='#232F3B').grid(row=7, padx=(10, 10), pady=(40, 10))
    tafEntry3 = Entry(rightFrameADD, width=40, textvariable = sectiontaf).grid(row=7, column=1, ipady=5, padx=(10, 10), pady=(40, 10))

    Label(rightFrameADD, text="Batch :", font='none 14 bold', fg='white', bg='#232F3B').grid(row=8, padx=(10, 10), pady=(40, 10))
    tafEntry4 = Entry(rightFrameADD, width=40, textvariable = batchtaf).grid(row=8, column=1, ipady=5, padx=(10, 10), pady=(40, 10))

    Button(rightFrameADD, bg="#3b8bbc", fg="white", text="Submit", font="none 10 bold", width=18, height=2, command=teacherAssignBTN).grid(row=10, column=1, padx=(10, 10), pady=(40, 10))



def studentAssignBTN():
    global rightFrameADD
    print "Done"
        
    checkStatus=0
    safStudentID = studentIDsaf.get()
    safCourseCode = courseCodesaf.get()
    safSection = sectionsaf.get()
    safBatch = batchsaf.get()
    if (safStudentID != '' and safCourseCode != '' and safSection != '' and safBatch != ''):
        import pymysql
        conn = pymysql.connect("localhost","root","","project")
        assignR = conn.cursor()
        show = conn.cursor()
        show.execute("select * from student_assign")
        
        for showR in show:
            
            if (safStudentID == showR[1] and safCourseCode == showR[2]):
                checkStatus=1
        if(checkStatus != 1):
            insertStudentAssign = "insert into student_assign(student_id,course_code,section,batch) values ('"+safStudentID+"','"+safCourseCode+"','"+safSection+"','"+safBatch+"')";
            assignR.execute(insertStudentAssign)        
            conn.commit()
        conn.close()
    
def studentAssignFun():
    global rightFrameADD, studentIDsaf, courseCodesaf, sectionsaf, batchsaf, btnPress
    btnPress = btnPress + 1
    if (btnPress != 0):
        list = rightFrameADD.grid_slaves()
        for l in list:
            l.destroy()
    studentIDsaf = StringVar()
    courseCodesaf = StringVar()
    sectionsaf = StringVar()
    batchsaf = StringVar()
    
    
    Label(rightFrameADD, text="Student ID :", font='none 14 bold', fg='white', bg='#232F3B').grid(row=5, padx=(10, 10), pady=(40, 10))
    safEntry1 = Entry(rightFrameADD, width=40, textvariable = studentIDsaf).grid(row=5, ipady=5, column=1, padx=(10, 10), pady=(40, 10))

    Label(rightFrameADD, text="Course Code :", font='none 14 bold', fg='white', bg='#232F3B').grid(row=6, padx=(10, 10), pady=(40, 10))
    safEntry2 = Entry(rightFrameADD, width=40, textvariable = courseCodesaf).grid(row=6, column=1, ipady=5, padx=(10, 10), pady=(40, 10))

    Label(rightFrameADD, text="Section :", font='none 14 bold', fg='white', bg='#232F3B').grid(row=7, padx=(10, 10), pady=(40, 10))
    safEntry3 = Entry(rightFrameADD, width=40, textvariable = sectionsaf).grid(row=7, column=1, ipady=5, padx=(10, 10), pady=(40, 10))

    Label(rightFrameADD, text="Batch :", font='none 14 bold', fg='white', bg='#232F3B').grid(row=8, padx=(10, 10), pady=(40, 10))
    safEntry4 = Entry(rightFrameADD, width=40, textvariable = batchsaf).grid(row=8, column=1, ipady=5, padx=(10, 10), pady=(40, 10))

    Button(rightFrameADD, bg="#3b8bbc", fg="white", text="Submit", font="none 10 bold", width=18, height=2, command=studentAssignBTN).grid(row=10, column=1, padx=(10, 10), pady=(40, 10))


def registrationBTN():
    global rightFrameADD
    print "Done"
        
    checkStatus=0
    takenTeacherID = takeUserID.get()
    takenTeacherName = takeName.get()
    takenPassword = takePassword.get()
    takenPosition = variable3.get()
    
    if (takenTeacherID != '' and takenTeacherName != '' and takenPassword != '' and takenPosition != 'Select Position'):
        import pymysql
        conn = pymysql.connect("localhost","root","","project")
        assignR = conn.cursor()
        show = conn.cursor()
        show.execute("select * from login")
        
        for showR in show:
            
            if (takenTeacherID == showR[0]):
                checkStatus=1
                print "You enter duplicate faculty id !"
                Label(rightFrameADD, text="You enter duplicate teacher id !", font='none 10 bold', fg='red', bg='#232F3B').grid(row=12, column=0, padx=(10, 10))
                break
        
            
            
        if(checkStatus != 1):            
            insertRegistration = "insert into login(userId,name,password,position) values ('"+takenTeacherID+"','"+takenTeacherName+"','"+takenPassword+"','"+takenPosition+"')";
            assignR.execute(insertRegistration)        
            conn.commit()
            Label(rightFrameADD, text="Registration done sucessfully !", font='none 10 bold', fg='red', bg='#232F3B').grid(row=12, column=0, padx=(10, 10))
        conn.close()


def registrationFun():
    global rightFrameADD, btnPress,takeUserID, takeName, takePassword, variable3
    btnPress = btnPress + 1
    if (btnPress != 0):
        list = rightFrameADD.grid_slaves()
        for l in list:
            l.destroy()
    takeUserID = StringVar()
    takeName = StringVar()
    takePassword = StringVar()
    
    
    Label(rightFrameADD, text="Faculty ID :", font='none 14 bold', fg='white', bg='#232F3B').grid(row=5, padx=(10, 10), pady=(40, 10))
    regEntry1 = Entry(rightFrameADD, width=40, textvariable = takeUserID).grid(row=5, ipady=5, column=1, padx=(10, 10), pady=(40, 10))

    Label(rightFrameADD, text="Faculty Name :", font='none 14 bold', fg='white', bg='#232F3B').grid(row=6, padx=(10, 10), pady=(40, 10))
    regEntry2 = Entry(rightFrameADD, width=40, textvariable = takeName).grid(row=6, column=1, ipady=5, padx=(10, 10), pady=(40, 10))

    Label(rightFrameADD, text="Password :", font='none 14 bold', fg='white', bg='#232F3B').grid(row=7, padx=(10, 10), pady=(40, 10))
    regEntry3 = Entry(rightFrameADD, width=40, textvariable = takePassword).grid(row=7, column=1, ipady=5, padx=(10, 10), pady=(40, 10))

    variable3 = StringVar(rightFrameADD)
    variable3.set("Select Position") # default value

    wvv = OptionMenu(rightFrameADD, variable3, "Teacher", "Advisor")
    wvv.grid(column=1, row=9)
    
    Button(rightFrameADD, bg="#3b8bbc", fg="white", text="Submit", font="none 10 bold", width=18, height=2, command=registrationBTN).grid(row=10, column=1, padx=(10, 10), pady=(40, 10))
    Label(rightFrameADD, text="....... ........ ....... ........ ......... .......", font='none 10 bold', fg='#232F3B', bg='#232F3B').grid(row=12, column=0, padx=(10, 10))


#''''''''''''' Admin Interface '''''''''''''''''

def adminInterface(adminName):   
    global app, rightFrameADD, btnPress
    btnPress = 0
    topFrameWC = Frame(app, borderwidth=1, relief="solid")
    topFrameWC.pack(expand=False, fill="both")
    topFrameWC.configure(background="#232F3B")

    leftFrameBTN = Frame(app, borderwidth=1, relief="solid")
    leftFrameBTN.pack(side='left', expand=False, fill="both")
    leftFrameBTN.configure(background="#232F3B")

    rightFrameADD = Frame(app, borderwidth=1, relief="solid")
    rightFrameADD.pack(side='right', expand=True, fill="both")
    rightFrameADD.configure(background="#232F3B")
    
    list = app.grid_slaves()
    for l in list:
        l.destroy()
        
    print "Hello admin"
    teacherID = userIdField.get()
    Label(topFrameWC, text='Welcome Admin: ' + adminName, fg='white', bg='#232F3B', font='none 10 bold').grid(row=0, column=4, pady=(10, 10), padx=(100, 100))
    Button(topFrameWC, bg="#232F3B", fg="white", text="Logout", font="none 10 bold", width=10, height=1, command=signoutCommand).grid(row=0, column=5, pady=(10, 10))
    #Admin button .....................................
    
    studentDetailsBTN = Button(leftFrameBTN, bg="#3b8bbc", fg="white", text="Student Details", font="none 10 bold", width=20, height=2, command=studentDetailsFun).grid(row=2, column=3, padx=(10, 10), pady=(40, 10))
    teacherAssignBTN = Button(leftFrameBTN, bg="#3b8bbc", fg="white", text="Assign Teacher",relief=RAISED, borderwidth=1, font="none 10 bold", width=20, height=2, command=teacherAssignFun).grid(row=3, column=3, padx=(10, 10), pady=(40, 10))
    courseDetails = Button(leftFrameBTN, bg="#3b8bbc", fg="white", text="Course Details", font="none 10 bold", width=18, height=2, command=courseDetailsFun).grid(row=4, column=3, padx=(10, 10), pady=(40, 10))
    registration = Button(leftFrameBTN, bg="#3b8bbc", fg="white", text="Registration", font="none 10 bold", width=18, height=2, command=registrationFun).grid(row=5, column=3, padx=(10, 10), pady=(40, 10))
    
    


    



def takeAutoAttendance():
    global rightFrame,rightFrame1Box1,rightFrame1Box2,rightFrame1Box3,rightFrame1Box4,detailsDestroy,courseCode,course_section,course_batch
    now = datetime.datetime.now()
    current_Date = str(now.day) + '-' + str(now.month) + '-' + str(now.year)
    for i in range(cc):
        if (variable.get() == OPTIONS[i]):
            si=i
    list = rightFrame.grid_slaves()
    for l in list:
        l.destroy()
    if(detailsDestroy==1):
        rightFrame1Box1.destroy()
        rightFrame1Box2.destroy()
        rightFrame1Box3.destroy()
        rightFrame1Box4.destroy()
        detailsDestroy=0
    
    faceDetect = cv2.CascadeClassifier('C:\Python27\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml');
    cam = cv2.VideoCapture(0)
    recognizer=cv2.face.LBPHFaceRecognizer_create();
    recognizer.read('ImageFile/'+course_batch[si]+'/'+course_section[si]+'/trainner.yml')

    pias = 0
    sagor = 0
    alim=0
    capture=0
    sampleNum = 0
    sampleImageOut = 0
    highestImageDetect = 0
    highestImageDetectCount = 0
    priorityImage = []
    finalCountImage={}

    #Query START ..................................................................................
    import pymysql
    studentList = []
    studentListDivide = []
    attendanceList = []
    attendanceMissedList = []
    conn = pymysql.connect("localhost","root","","project")
    findTaken = conn.cursor()

    #show data of row
    stuRegistrationofTake = 'SELECT student_id from `student_assign` where section="'+course_section[si]+'" and batch="'+course_batch[si]+'" and course_code="'+courseCode[si]+'"'
    findTaken.execute(stuRegistrationofTake)
    for row in findTaken:
        studentListDivide.append(row[0])

    conn.close()
    #Query END ..................................................................................
    for splitID in range (len(studentListDivide)):
        studentList.append(int(os.path.split(studentListDivide[splitID])[-1].split("-")[2]))
        
    studentDetectCount = []
    print studentListDivide
    print studentList

    font = cv2.FONT_HERSHEY_SIMPLEX


    while(True):
        
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.2, 4)
        cv2.waitKey(100)
        if len(faces)>0:
            sampleNum +=1
            cv2.imwrite("cap/cap."+ str(sampleNum) + ".jpg",img) #save image
            cv2.imshow('img',img)
            if(sampleNum>30):
                break
    cam.release()


    while capture!= sampleNum:
        capture = capture + 1
        sampleImageOut = sampleImageOut + 1
        #ret, im =cam.read()
        im = cv2.imread("cap/cap."+str(sampleImageOut)+".jpg")
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.2,5)
        
        print "...................................."
        print "Image detect = ",len(faces)
        print "Capture Number = ",sampleImageOut
        priorityImage.append(len(faces))
        
        if(highestImageDetect < len(faces)):
            highestImageDetect = len(faces)
            highestImageDetectCount = highestImageDetectCount + 1
            
            
        print "HighestImageDetect : " + str(highestImageDetectCount)
        for(x,y,w,h) in faces:            
                
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            print "ID : " + str(id)
            print confidence
            if(confidence >= 20):
                for i in range (len(studentList)):
                    if(id == studentList[i]):
                        studentDetectCount.append(id)
                        break
                        
                    
                cv2.putText(im, str(id),(x,y+h), font, 1 ,(255,255,255),2,cv2.LINE_AA)
            else:
                id="Not"
                cv2.putText(im, str(id),(x,y+h), font, 1 ,(255,255,255),2,cv2.LINE_AA)
                        
            cv2.imshow('im',im)
            
       
        if cv2.waitKey(10) ==ord('q'):
            break
        elif sampleImageOut==sampleNum:
            print ""
            print "...................................."
            print "...................................."
            print "Number of highest detect change = ",highestImageDetect
            print "Number of highest = ",highestImageDetect
            print ""
            print "Sagor = ",sagor
            print "Pias = ",pias
            print "Alim = ",alim
            
            print priorityImage
            
            finalCountImage = Counter(priorityImage) 
            index =  max(finalCountImage, key=finalCountImage.get)

            print finalCountImage

            print finalCountImage.items()
            print index
            print finalCountImage[index]
            print "Final Detect of Image : " + str(index)
            print "...................................."
            print "...................................."


            print studentDetectCount
            finalstudentDetectCount = Counter(studentDetectCount) 
            indexNo =  sorted(((v,k) for k,v in finalstudentDetectCount.items()))
            print "FIrst :"
            print finalstudentDetectCount
            print "Second :"
            print indexNo
            print "divide"
            print len(studentListDivide)
            print "divide"
            print (range(index))
            
            

            import pymysql
            conn = pymysql.connect("localhost","root","","project")
            attendanceInput = conn.cursor()
            attendanceInput2 = conn.cursor()
            
            for k in range (len(studentListDivide)):
                
                for j in range (index):
                    print j
                    if((indexNo[-(j)][1]) == int(os.path.split(studentListDivide[k])[-1].split("-")[2])):                        
                        print "Attendace done : " + str(indexNo[-(j+1)][1])

                        #insertAttendance = "insert into attendance(student_id,course_code,section,batch,date,status) values ('"+studentListDivide[k]+"','"+courseCode[si]+"','"+course_section[si]+"','"+course_batch[si]+"','"+current_Date+"','T')";
                        #attendanceInput.execute(insertAttendance)    
                        attendanceList.append(studentListDivide[k])
                        print "done"
                        print attendanceList
                    #else:
                        
                        
                    #if ((indexNo[-(j)][1]) != int(os.path.split(studentListDivide[k])[-1].split("-")[2])):
                        #attendanceMissedList.append(studentListDivide[k])
                        #print attendanceMissedList
                        #insertAttendance = "insert into attendance(student_id,course_code,section,batch,date,status) values ('"+studentListDivide[k]+"','"+courseCode[si]+"','"+course_section[si]+"','"+course_batch[si]+"','"+current_Date+"','F')";
                        #attendanceInput.execute(insertAttendance)
                        
            

            #for k in range (len(attendanceMissedList)):            
                #insertAttendance2 = "insert into attendance(student_id,course_code,section,batch,date,status) values ('"+attendanceMissedList[k]+"','"+courseCode[si]+"','"+course_section[si]+"','"+course_batch[si]+"','"+current_Date+"','F')";
                #attendanceInput2.execute(insertAttendance2)
                        
                        
            
            conn.commit()
            conn.close()
            print attendanceList
            print attendanceMissedList
            Label(rightFrame, text='Attendace done : ' + str(len(attendanceList))).grid(row=10, column=0, pady=(40, 10))
            #Label(rightFrame, text='Attendace not done : ' + str(len(attendanceMissedList))).grid(row=11, column=0, pady=(40, 10))
            
            break
        
    cam.release()

    cv2.destroyAllWindows()



def studentShowIndividual():
    global rightFrame,userImageField,rightFrame,selectIndexNo,detailsDestroy,rightFrame1Box1,rightFrame1Box2,rightFrame1Box3,rightFrame1Box4
    list = rightFrame.grid_slaves()
    for l in list:
        l.destroy()
    if(detailsDestroy==1):
        rightFrame1Box1.destroy()
        rightFrame1Box2.destroy()
        rightFrame1Box3.destroy()
        rightFrame1Box4.destroy()
        detailsDestroy=0
        
    attendanceLbl = Label(rightFrame, text='Details of Student', font='none 15 bold')
    attendanceLbl.grid(row=0, column=1)
    
    userImageField=StringVar(rightFrame)       
    Label(rightFrame, text='Student ID  : ').grid(row=10, column=0, pady=(40, 10))
    Entry(rightFrame, width=40, textvariable = userImageField).grid(row=10, column=1, ipady=5, padx=(30, 30), pady=(40, 10))
    indiBtn = Button(rightFrame, text='Search', command=lambda sID=0: studentShowIndividualCommand(sID)).grid(row=11, column=1, ipady=5, padx=(30, 30), pady=(10, 10))



def attendanceShowIndividual():
    global rightFrame,getAttendID,rightFrame,selectIndexNo,detailsDestroy,rightFrame1Box1,rightFrame1Box2,rightFrame1Box3,rightFrame1Box4
    print str(detailsDestroy)
    list = rightFrame.grid_slaves()
    for l in list:
        l.destroy()
    if(detailsDestroy==1):
        rightFrame1Box1.destroy()
        rightFrame1Box2.destroy()
        rightFrame1Box3.destroy()
        rightFrame1Box4.destroy()
        detailsDestroy=0
        
    
    attendanceLbl = Label(rightFrame, text='Attendance of Student', font='none 15 bold')
    attendanceLbl.grid(row=0, column=1)
    
    getAttendID=StringVar(rightFrame)       
    Label(rightFrame, text='Student ID  : ').grid(row=10, column=0, pady=(40, 10))
    Entry(rightFrame, width=40, textvariable = getAttendID).grid(row=10, column=1, ipady=5, padx=(30, 30), pady=(40, 10))
    indiBtn = Button(rightFrame, text='Search', command=attendanceShowIndividualCommand).grid(row=11, column=1, ipady=5, padx=(30, 30), pady=(10, 10))



def studentShowTotal():
    global studentIdTake,rightFrame,rightFrame,selectIndexNo,detailsDestroy,rightFrame1Box1,rightFrame1Box2,rightFrame1Box3,rightFrame1Box4,courseCode,course_section,course_batch
    print str(detailsDestroy)
    for i in range(cc):
        if (variable.get() == OPTIONS[i]):
            si=i
    list = rightFrame.grid_slaves()
    for l in list:
        l.destroy()
    if(detailsDestroy==1):
        rightFrame1Box1.destroy()
        rightFrame1Box2.destroy()
        rightFrame1Box3.destroy()
        rightFrame1Box4.destroy()
        detailsDestroy=0

        
        
    attendanceLbl = Label(rightFrame, text='Student ID ', font='none 9 bold')
    attendanceLbl.grid(row=0, column=0)

    attendanceLbl = Label(rightFrame, text=' ',bg='#236F3B', font='none 9 bold')
    attendanceLbl.grid(row=0, column=1)

    attendanceLbl = Label(rightFrame, text=' Student Name ', font='none 9 bold')
    attendanceLbl.grid(row=0, column=2)

    attendanceLbl = Label(rightFrame, text=' ',bg='#236F3B', font='none 9 bold')
    attendanceLbl.grid(row=0, column=3)

    attendanceLbl = Label(rightFrame, text=' Student Email ', font='none 9 bold')
    attendanceLbl.grid(row=0, column=4)
    

    import pymysql
    studentAllID=[]
    studentAllName=[]
    studentAllEmail=[]
    studentTaken=[]
    takeName=[]
    takeEmail=[]
    takeID=[]
    finalDisplay=[]
    conn = pymysql.connect("localhost","root","","project")
    studentAll = conn.cursor()
    studentAssign = conn.cursor()
    takeNameEmail = conn.cursor()
    takeNameEmail2 = conn.cursor()

            

    #show data of row
    stuRegistration = 'SELECT * from `student_assign` where section="'+course_section[si]+'" and batch="'+course_batch[si]+'" and course_code="'+courseCode[si]+'"'
    studentAll.execute(stuRegistration)
    rowSizeAttendance = studentAll.execute(stuRegistration)
    for row in studentAll:
        studentTaken.append(row[1])        

    print studentTaken
    
    nameEmail = 'SELECT id from `student_details`'
    takeNameEmail.execute(nameEmail)
    for row in takeNameEmail:
        takeID.append(row[0])
    for i in range(len(studentTaken)):
        for j in range(len(takeID)):
            if(studentTaken[i] == takeID[j]):
                finalDisplay.append(studentTaken[i])

        
    print finalDisplay
    
    
    for i in range (len(finalDisplay)): 
        nameEmail2 = 'SELECT * from `student_details` where id="'+finalDisplay[i]+'"'
        takeNameEmail2.execute(nameEmail2)
        for row in takeNameEmail2:
            
            studentIdTake=studentTaken[i]    
            listBoxSelect=Listbox(rightFrame, font='none 10', height=1, width=12)
            listBoxSelect.grid(row=i+1, column=0)
            listBoxSelect.insert(i,row[0])
            
            listBoxSelect=Listbox(rightFrame, font='none 10', height=1, width=20)
            listBoxSelect.grid(row=i+1, column=2)
            listBoxSelect.insert(i,row[1])

            listBoxSelect=Listbox(rightFrame, font='none 10', height=1, width=25)
            listBoxSelect.grid(row=i+1, column=4)
            listBoxSelect.insert(i,row[3]) 

        
            Button(rightFrame, text="Details", bg="#3b8bbc", fg="white", font='none 9 bold', width=10, command=lambda sID=row[0]: gotoStudentDetails(sID)).grid(row=i+1, column=10)
      
    conn.close()

def gotoStudentDetails(sID):
    global takesID
    takesID=1    
    print sID
    studentShowIndividualCommand(sID)


def studentShowIndividualCommand(sID):
    global takesID,studentIdTake,individualStudentID,dateOfClass,rowStudentIndi,variable,OPTIONS,detailsDestroy,rightFrame1Box1,rightFrame1Box2,rightFrame1Box3,rightFrame1Box4
    detailsDestroy=1
    for i in range(cc):
        if (variable.get() == OPTIONS[i]):
            si=i        
    list = rightFrame.grid_slaves()
    for l in list:
        l.destroy()
    if(takesID==1):
        individualStudentID = sID
        takesID=0
        
    else:    
        individualStudentID = userImageField.get()
    print individualStudentID


    import pymysql
    i=0
    conn = pymysql.connect("localhost","root","","project")
    a = conn.cursor()
    getCol=conn.cursor()
    attenPer=conn.cursor()
    attenPer2=conn.cursor()

            
    attend = conn.cursor()
    attendIdName = conn.cursor()
            

    #show data of row
    sqlRow = 'SELECT * from `student_details` where id="'+individualStudentID+'"'
    a.execute(sqlRow)
    rowSizeAttendance = a.execute(sqlRow)



    attendancePercentage = 'SELECT date from `attendance` where course_code="' + courseCode[si] + '" and section="'+course_section[si]+'" and batch="'+course_batch[si]+'"'
    forAttendancePercentage = attenPer.execute(attendancePercentage)
    dayCount=''
    attendanceSizeof=0
    for h in range(forAttendancePercentage):
        for forAttendanceCount in attenPer:
            if(dayCount != forAttendanceCount[h]):
                dayCount = forAttendanceCount[h]
                attendanceSizeof = attendanceSizeof + 1
               
    attendancePercentage2 = 'SELECT status from `attendance` where student_id="'+ individualStudentID +'" and course_code="' + courseCode[si] + '" and section="'+course_section[si]+'" and batch="'+course_batch[si]+'"'
    forAttendancePercentage2 = attenPer2.execute(attendancePercentage2)
    dayCount2='T'
    attendanceSizeof2=0
    for h2 in range(forAttendancePercentage2):
        for forAttendanceCount2 in attenPer2:
            if(dayCount2 == forAttendanceCount2[h2]):
                print forAttendanceCount2[h2]
                attendanceSizeof2 = attendanceSizeof2 + 1
                



                    

    #header / title of table ..........................................................
    for rowStudentIndi in a:
        print rowStudentIndi

    conn.close()
            
           
    rightFrame1Box1 = Frame(rightFrame, borderwidth=2, relief="solid")
    rightFrame1Box2 = Frame(rightFrame, borderwidth=2, relief="solid")
    rightFrame1Box3 = Frame(rightFrame, borderwidth=2, relief="solid")
    rightFrame1Box4 = Frame(rightFrame, borderwidth=2, relief="solid")

    if(rowSizeAttendance > 0):
        #id,name,contact...................
        rightFrame1Label = Label(rightFrame1Box1, text="Student Identification :-", fg='black', font='none 14 bold').pack()
        rightFrame1Label = Label(rightFrame1Box1).pack()
        rightFrame1Label = Label(rightFrame1Box1, text="ID : "+rowStudentIndi[0], fg='black', font='none 14 bold').pack()
        rightFrame1Label = Label(rightFrame1Box1, text="Name : "+rowStudentIndi[1], fg='black', font='none 14 bold').pack()
        rightFrame1Label = Label(rightFrame1Box1, text="Contact No : "+rowStudentIndi[2], fg='black', font='none 12 bold').pack()
        rightFrame1Label = Label(rightFrame1Box1, text="Email : "+rowStudentIndi[3], fg='black', font='none 12 bold').pack()
        rightFrame1Label = Label(rightFrame1Box1, text="Attendance : "+str(int((float(attendanceSizeof2)/float(attendanceSizeof))*100))+"%", fg='black', font='none 12 bold').pack()


        #Gurdian ...................
        rightFrame1Label = Label(rightFrame1Box2, text="Father Name : "+rowStudentIndi[4], fg='black', font='none 9 bold').pack()
        rightFrame1Label = Label(rightFrame1Box2, text="Father cell no : "+rowStudentIndi[5], fg='black', font='none 9 bold').pack()
        rightFrame1Label = Label(rightFrame1Box2, text="Mother Name : "+rowStudentIndi[6], fg='black', font='none 9 bold').pack()
                
        #faculty--enrollment ...................
        rightFrame1Label = Label(rightFrame1Box3, text="Faculty : "+rowStudentIndi[7], fg='black', font='none 9 bold').pack()
        rightFrame1Label = Label(rightFrame1Box3, text="Program : "+rowStudentIndi[8], fg='black', font='none 9 bold').pack()
        rightFrame1Label = Label(rightFrame1Box3, text="Batch : "+rowStudentIndi[9], fg='black', font='none 11 bold').pack()
        rightFrame1Label = Label(rightFrame1Box3, text="Enrollment : "+rowStudentIndi[10], fg='black', font='none 11 bold').pack()

        #Present Address
        rightFrame1Label = Label(rightFrame1Box4, text="Present Address :-", fg='black', font='none 14 bold').pack()
        rightFrame1Label = Label(rightFrame1Box4, text=rowStudentIndi[11], fg='black').pack()
        rightFrame1Label = Label(rightFrame1Box4, text=' ', fg='black').pack()

                
        #Permanent Address ...................
        rightFrame1Label = Label(rightFrame1Box4, text="Permanent Address :-", fg='black', font='none 14 bold').pack()
        rightFrame1Label = Label(rightFrame1Box4, text="Village : "+rowStudentIndi[12], fg='black').pack()
        rightFrame1Label = Label(rightFrame1Box4, text="Post Office : "+rowStudentIndi[13], fg='black').pack()
        rightFrame1Label = Label(rightFrame1Box4, text="Post Code : "+str(rowStudentIndi[14]), fg='black').pack()
        rightFrame1Label = Label(rightFrame1Box4, text="Thana : "+rowStudentIndi[15], fg='black').pack()
        rightFrame1Label = Label(rightFrame1Box4, text="District : "+rowStudentIndi[16], fg='black').pack()
    else:
        rightFrame1Label = Label(rightFrame1Box1, text="Personal Information not abailable !", fg='black', font='none 14 bold').pack()
        rightFrame1Label = Label(rightFrame1Box1, text="Attendance : "+str((attendanceSizeof2/attendanceSizeof)*100)+"%", fg='black', font='none 12 bold').pack()   
    rightFrame1Box1.pack(expand=True, fill="both", padx=10, pady=10)
    rightFrame1Box2.pack(expand=True, fill="both", padx=10, pady=10)
    rightFrame1Box3.pack(expand=True, fill="both", padx=10, pady=10)
    rightFrame1Box4.pack(expand=True, fill="both", padx=10, pady=10)

            
            



def attendanceShowTotal():
    global variable,OPTIONS,detailsDestroy,rightFrame1Box1,rightFrame1Box2,rightFrame1Box3,rightFrame1Box4
    for i in range(cc):
        if (variable.get() == OPTIONS[i]):
            si=i
   
    list = rightFrame.grid_slaves()
    for l in list:
        l.destroy()
    if(detailsDestroy==1):
        rightFrame1Box1.destroy()
        rightFrame1Box2.destroy()
        rightFrame1Box3.destroy()
        rightFrame1Box4.destroy()
        detailsDestroy=0
                
            
    attendanceDataArrayID2=[]
    columnArray=[]
               
    import pymysql
    i=0
    conn = pymysql.connect("localhost","root","","project")
    a = conn.cursor()
    getCol=conn.cursor()
    attend = conn.cursor()
    attendIdName = conn.cursor()

    #show data of row
    sqlRow = 'SELECT * from `student_assign` where course_code="' + courseCode[si] + '" and section="'+course_section[si]+'" and batch="'+course_batch[si]+'"'
    a.execute(sqlRow)
    rowSizeAttendance = a.execute(sqlRow)
            
    #show column name of table ..........................................................
    sqlRowHeader = 'SELECT * from `attendance` where course_code="' + courseCode[si] + '" and section="'+course_section[si]+'" and batch="'+course_batch[si]+'"'
    colSizeAttendance = getCol.execute(sqlRowHeader)
    print colSizeAttendance
    print "student_assign Row size: " + str(rowSizeAttendance)


    #header / title of table ..........................................................
    for row in getCol:
        columnArray.append(row[5])



    Label(rightFrame, text = "ID", font='none 12 bold', bg='#232F3B', fg='white').grid(row=0, column=0)
    Label(rightFrame, text = "NAME", font='none 12 bold', bg='#232F3B', fg='white').grid(row=0, column=1)
    replaceRowName=''
    j=2
    for i in range(colSizeAttendance):
        if (columnArray[i] != replaceRowName):
            replaceRowName = columnArray[i]            
            Label(rightFrame, text = replaceRowName, font='none 10', bg='#232F3B', fg='white').grid(row=0, column=(j))
            Label(rightFrame, text = '', font='none 10', bg='#236F3B', fg='white').grid(row=0, column=(j+1))
            j = j+2
    print "j:" + str(j-2)   


    #body of table ....................................................................................
                    
    countRow = a.execute(sqlRow)
            
    for row in a:
        attendanceDataArrayID2.append(row[1])
                    
    print attendanceDataArrayID2
            


    i=0    
    while i!=(len(attendanceDataArrayID2)):
        print "pias: " + attendanceDataArrayID2[i]
        DateCount=2
        sqlBodyAttendance = 'SELECT * from `attendance` where student_id="' + attendanceDataArrayID2[i] + '" and course_code="' + courseCode[si] + '" and section="'+course_section[si]+'" and batch="'+course_batch[si]+'"'
        sqlBodyAttendanceSet = attend.execute(sqlBodyAttendance)

        sqlBodyStudentIDName = 'SELECT * from `student_details` where id="' + attendanceDataArrayID2[i] + '"'
        sqlBodyStudentName = attendIdName.execute(sqlBodyStudentIDName)
                
                
                
        listBoxSelect=Listbox(rightFrame, font='none 10', height=1, width=12)
        listBoxSelect.grid(row=i+1, column=0)
        listBoxSelect.insert(i,attendanceDataArrayID2[i])
                
        for rowIdName in attendIdName:
                
            listBoxSelect=Listbox(rightFrame, font='none 10', height=1, width=20)
            listBoxSelect.grid(row=i+1, column=1)
            listBoxSelect.insert(i,rowIdName[1])
                
        print "\n\n"
        for attendRow in attend:
            print attendRow
                    
            listBoxSelect=Listbox(rightFrame, font='none 10', height=1, width=5)
            listBoxSelect.grid(row=i+1, column=DateCount)
            listBoxSelect.insert(i,attendRow[6])
                    
            DateCount = DateCount + 2
            
                    
        i = i + 1  
    conn.close()


        


def attendanceShowIndividualCommand():
    
    global individualID,rightFrame,dateOfClass,rowStudentIndi,courseCode,course_section,course_batch,selectIndexNo,variable,OPTIONS
    for i in range(cc):
        if (variable.get() == OPTIONS[i]):
            si=i
    print si
    list = rightFrame.grid_slaves()
    for l in list:
        l.destroy()
        
    columnArray=[]
    replaceRowName=[]
    individualID = getAttendID.get()
    attendanceDataArrayID2=[]
    columnArray=[]      
              
    import pymysql
    conn = pymysql.connect("localhost","root","","project")
    studentAssignTable = conn.cursor()
    getDate=conn.cursor()
    attend=conn.cursor()
    attendIdName=conn.cursor()
    #attend = conn.cursor()
    #attendIdName = conn.cursor()

    #show data of row
    sqlRow = 'SELECT * from `student_assign` where student_id="'+individualID+'" and course_code="' + courseCode[si] + '" and section="'+course_section[si]+'" and batch="'+course_batch[si]+'"'
    studentAssignTable.execute(sqlRow)
    rowSizeAttendance = studentAssignTable.execute(sqlRow)
    
    #show column name of table ..........................................................
    sqlRowHeader = 'SELECT * from `attendance` where course_code="' + courseCode[si] + '" and section="'+course_section[si]+'" and batch="'+course_batch[si]+'"'
    colSizeAttendance = getDate.execute(sqlRowHeader)
    print getDate
    print selectIndexNo
    print courseCode[selectIndexNo]

    #header / title of table ..........................................................
    for row in getDate:
        columnArray.append(row[5])
        


    print len(columnArray)
    Label(rightFrame, text = "ID", font='none 12 bold', bg='#232F3B', fg='white').grid(row=0, column=0)
    Label(rightFrame, text = "NAME", font='none 12 bold', bg='#232F3B', fg='white').grid(row=0, column=1)
    replaceRowName=''
    j=2
    for i in range(colSizeAttendance):
        if (columnArray[i] != replaceRowName):
            replaceRowName = columnArray[i]
            print replaceRowName
            Label(rightFrame, text = replaceRowName, font='none 10', bg='#232F3B', fg='white').grid(row=0, column=(j))
            Label(rightFrame, text = '', font='none 10', bg='#236F3B', fg='white').grid(row=0, column=(j+1))
            j = j+2

    
            
    for row in studentAssignTable:
        attendanceDataArrayID2.append(row[1])
                    
    print "Data"
    print len(attendanceDataArrayID2)
            


    i=0    
    while i!=(len(attendanceDataArrayID2)):
        print "pias: " + attendanceDataArrayID2[i]
        DateCount=2
        sqlBodyAttendance = 'SELECT * from `attendance` where student_id="' + attendanceDataArrayID2[i] + '" and course_code="' + courseCode[si] + '" and section="'+course_section[si]+'" and batch="'+course_batch[si]+'"'
        sqlBodyAttendanceSet = attend.execute(sqlBodyAttendance)

        sqlBodyStudentIDName = 'SELECT * from `student_details` where id="' + attendanceDataArrayID2[i] + '"'
        sqlBodyStudentName = attendIdName.execute(sqlBodyStudentIDName)
                
                
                
        listBoxSelect=Listbox(rightFrame, font='none 10', height=1, width=12)
        listBoxSelect.grid(row=i+1, column=0)
        listBoxSelect.insert(i,attendanceDataArrayID2[i])
                
        for rowIdName in attendIdName:
                
            listBoxSelect=Listbox(rightFrame, font='none 10', height=1, width=20)
            listBoxSelect.grid(row=i+1, column=1)
            listBoxSelect.insert(i,rowIdName[1])
                
        print "\n\n"
        for attendRow in attend:
            print attendRow
                    
            listBoxSelect=Listbox(rightFrame, font='none 10', height=1, width=5)
            listBoxSelect.grid(row=i+1, column=DateCount)
            listBoxSelect.insert(i,attendRow[6])
                    
            DateCount = DateCount + 2
            
                    
        i = i + 1
   
    conn.close()



def signoutCommand():
    global app
    app.destroy()
    app=Tk()
    app.title("Login panel of Student Attendance System")
    app.geometry('%dx%d+%d+%d' % (w, h, x, y))
    app.configure(background="#232F3B")
    
    mainLoginPage()
    
    app.mainloop()

def initialCommand():
    
    global app,detailsDestroy
    app.destroy()
    app=Tk()
    app.title("Login panel of Student Attendance System")
    app.geometry('%dx%d+%d+%d' % (w, h, x, y))
    app.configure(background="#232F3B")
    detailsDestroy=0
    mainSubjectPage()
    
    app.mainloop()
    

    
def mainInterface():
    global leftFrame,rightFrame,upFrame,app
    
    list = app.grid_slaves()
    for l in list:
        l.destroy()
    
    upFrame.destroy()             
    leftFrame = Frame(app, borderwidth=1, relief="solid")
    rightFrame = Frame(app, borderwidth=1, relief="solid")
    leftFrame.pack(side="left", expand=False, fill="both")
    rightFrame.pack(side="right", expand=True, fill="both")
    leftFrame.configure(background="#232F3B")
    rightFrame.configure(background="#236F3B")


    #Top Menubar .........................................
    menu = Menu(app)
    app.config(menu=menu)

    #Menu >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    goToMenu = Menu(menu, tearoff=False)
    attendanceMenu = Menu(menu, tearoff=False)
    studentMenu = Menu(menu, tearoff=False)
    signoutMenu = Menu(menu, tearoff=False,fg='red')


    #Menu
    menu.add_cascade(label="Go To", menu=goToMenu, font = ('Verdana', 14))
    menu.add_cascade(label="Attendance Query", menu=attendanceMenu)
    menu.add_cascade(label="Student Query", menu=studentMenu)
    menu.add_cascade(label="Welcome, "+teacherNamebyId, menu=signoutMenu)


    #GoTo
    goToMenu.add_command(label="Home Page")
    goToMenu.add_separator()
    goToMenu.add_command(label="Initial Page", command=initialCommand)

    #Attendance
    attendanceMenu.add_command(label="Show All", command=attendanceShowTotal)
    attendanceMenu.add_command(label="Individual", command=attendanceShowIndividual)

    #Student
    studentMenu.add_command(label="Show All", command=studentShowTotal)
    studentMenu.add_command(label="Individual", command=studentShowIndividual)


    #signout
    signoutMenu.add_command(label="Signout", command=signoutCommand)
    

    #Left side button .....................................
    startAttendanceBTN = Button(leftFrame, bg="#3b8bbc", fg="white", text="ATTENDANCE",relief=RAISED, borderwidth=1, font="none 10 bold", width=20, height=2, command=takeAutoAttendance).grid(row=1, column=0, padx=(10, 10), pady=(40, 10))
    startManualAttendanceBTN = Button(leftFrame, bg="#3b8bbc", fg="white", text="MANUAL  ATTENDANCE", font="none 10 bold", width=20, height=2).grid(row=2, column=0, padx=(10, 10), pady=(40, 10))
    showAttendanceBTN = Button(leftFrame, bg="#3b8bbc", fg="white", text="SHOW  ATTENDANCE",relief=RAISED, borderwidth=1, font="none 10 bold", width=20, height=2).grid(row=3, column=0, padx=(10, 10), pady=(40, 10))
    showImageBTN = Button(leftFrame, bg="#3b8bbc", fg="white", text="SHOW IMAGE", font="none 10 bold", width=18, height=2).grid(row=4, column=0, padx=(10, 10), pady=(40, 10))
    showStatusBTN = Button(leftFrame, bg="#3b8bbc", fg="white", text="STATUS",relief=RAISED, borderwidth=1, font="none 10 bold", width=16, height=2).grid(row=5, column=0, padx=(10, 10), pady=(40, 10))




def mainSubjectPage():
    global cc,selectIndexNo,teacherNamebyId,upFrame,app,course_section,course_batch,courseCode,selectIndexNo,variable,OPTIONS
    course_section=[]
    course_batch=[]
    courseCode=[]
    OPTIONS=[]    
    selectIndexNo=-1
          
    
    upFrame = Frame(app, borderwidth=1, relief="solid")
    upFrame.pack(side="top", expand=True, fill="both")
    upFrame.configure(background="#232F3B")
    
    teacherID = userIdField.get()
    
    def optionsCall(event):
             
            for i in range(cc):
                if( variable.get() == OPTIONS[i] ):
                    selectIndexNo = i
    
            if(selectIndexNo > -1):
                print selectIndexNo
                subjectSubmitBTN = Button(upFrame,bg="#3b8bbc", fg="white", text="Submit",relief=RAISED,
                            borderwidth=1, font="none 15 bold", width=20, height=1, command=mainInterface).grid(row=18, column=1, padx=(200, 200), pady=(300, 300))


    list = app.grid_slaves()
    for l in list:
        l.destroy()

    import pymysql
    conn = pymysql.connect("localhost","root","","project")
    teacherName = conn.cursor()

    sql = 'SELECT name from login where userId="' + teacherID + '"'
        
        
    teacherName.execute(sql)
    for row in teacherName:
        teacherNamebyId = row[0]           
        
    conn.close()
    
    loginWelcome = Label(upFrame, bg="#232F3B", fg="white", text="Welcome , "+ teacherNamebyId , font="none 15 bold", width=20, height=1)
    loginWelcome.grid(row=1, column=1, padx=(200, 200), pady=(1, 1))

    import pymysql
    conn = pymysql.connect("localhost","root","","project")
    a = conn.cursor()
    b= conn.cursor()

    sql = 'SELECT * from teacher_assign where teacher_id="' + teacherID +'"'
        
        
    a.execute(sql)
    cc = a.execute(sql)
    for row in a:
        course_section.append(row[3])
        course_batch.append(row[4])
            
        sql2 = 'SELECT * from course_details where id="' + row[2] + '"'
        b.execute(sql2)
            
        for row2 in b: 
                
            print row
            OPTIONS.append(row[2]+' : '+row2[1]+ ' : '+row[3]+' : '+row[4]+ " batch")
            courseCode.append(row[2])
                
            
              
    variable = StringVar(upFrame)
    variable.set("Select Course") # default value

    w = OptionMenu(upFrame, variable, *OPTIONS, command=optionsCall)
    w.pack()
    w.place(relx=.5, rely=.2, anchor="n", width=300, height=50)
                
    enter2 = userIdField.get()          

    conn.close()
    
        
         


def mainLoginPage():
    global loginIdTaken,loginPassTaken,userIdField,passwordField,variable2
    def loginCheck():
        whoLogin = variable2.get()
        print whoLogin
        loginIdTaken = userIdField.get()
        loginPassTaken = passwordField.get()
        positionTaken = variable2.get()
        
        if(loginIdTaken == ''):
            print "Please enter your id !"

        elif(loginPassTaken == ''):
            print "Please enter your password !"

        elif(positionTaken == 'Select Position'):
            print "Please enter your position !"
            
        else:
            notDone = 0
            if (whoLogin == 'Teacher'):                
                import pymysql
                conn = pymysql.connect("localhost","root","","project")
                loginR = conn.cursor()

                sql = 'SELECT * from `login`'
                loginR.execute(sql)
                rowCount = loginR.execute(sql)
                    
                for loginRow in loginR:
                    if(loginIdTaken == loginRow[0] and loginPassTaken == loginRow[2] and positionTaken == loginRow[3]):                
                        print "Successfully Login"
                        notDone = 1
                        mainSubjectPage()
                        
                if (notDone == 0):
                    Label(app, text="You enter wrong id or password !", font='none 10 bold', fg='red', bg='#232F3B').grid(row=20, column=0, padx=(10, 10))       
                    #user1 = userIdField.get()
                    #print user1

                    #data = a.fetchall()
                    #print (data)          

                conn.close()

            elif (whoLogin == 'Admin'):
          
                positionTaken = variable2.get()
                print positionTaken
                import pymysql
                conn = pymysql.connect("localhost","root","","project")
                loginR = conn.cursor()

                sql = 'SELECT * from `login`'
                loginR.execute(sql)
                rowCount = loginR.execute(sql)
                    
                for loginRow in loginR:
                    if(loginIdTaken == loginRow[0] and loginPassTaken == loginRow[2] and positionTaken == loginRow[3]):                
                        print "Successfully Login"
                        notDone = 1
                        adminInterface(loginRow[1])
                        
                if (notDone == 0):
                        Label(app, text="You enter wrong id or password !", font='none 10 bold', fg='red', bg='#232F3B').grid(row=20, column=0, padx=(10, 10))       
                    #user1 = userIdField.get()
                    #print user1

                    #data = a.fetchall()
                    #print (data)          

                conn.close()

            elif (whoLogin == 'Advisor'):
          
                positionTaken = variable2.get()
                print positionTaken
                import pymysql
                conn = pymysql.connect("localhost","root","","project")
                loginR = conn.cursor()

                sql = 'SELECT * from `login`'
                loginR.execute(sql)
                rowCount = loginR.execute(sql)
                    
                for loginRow in loginR:
                    if(loginIdTaken == loginRow[0] and loginPassTaken == loginRow[2] and positionTaken == loginRow[3]):                
                        print "Successfully Login"
                        notDone = 1
                        advisorInterface(loginRow[1])
                        
                if (notDone == 0):
                        Label(app, text="You enter wrong id or password !", font='none 10 bold', fg='red', bg='#232F3B').grid(row=20, column=0, padx=(10, 10))       
                    #user1 = userIdField.get()
                    #print user1

                    #data = a.fetchall()
                    #print (data)          

                conn.close()
            
            

            
    
    variable2 = StringVar(app)
    variable2.set("Select Position") # default value

    wv = OptionMenu(app, variable2, "Teacher", "Admin", "Advisor")
    wv.grid(column=1, row=10)


    
    
    nameLabel1 = Label(app, text="Daffodil International University", font="none 15 bold", fg='white', bg='#232F3B')
    nameLabel1.grid(row=4,column=1)

    nameLabel2 = Label(app, text="Login Panel", width=10, font="none 15 bold", fg='white', bg='#232F3B')
    nameLabel2.grid(row=6,column=1)

    Label(app, text="", fg='red', bg='#232F3B').grid(row=3, column=2)
    Label(app, text="", fg='red', bg='#232F3B').grid(row=4, column=2)
    Label(app, text="", fg='red', bg='#232F3B').grid(row=5, column=2)
    Label(app, text="", fg='red', bg='#232F3B').grid(row=6, column=2)
    Label(app, text="", fg='red', bg='#232F3B').grid(row=7, column=2)
    Label(app, text="", fg='red', bg='#232F3B').grid(row=8, column=2)
    Label(app, text="", fg='red', bg='#232F3B').grid(row=9, column=2)
    Label(app, text="", fg='red', bg='#232F3B').grid(row=10, column=2)


    userIdField = StringVar()
    passwordField = StringVar()


    nameLabel3 = Label(app, text="User ID", font='none 15 bold', width=10, fg='white', bg='#232F3B').grid(row=14, padx=(30, 30), pady=(40, 10))
    nameEntry1 = Entry(app, width=40, textvariable = userIdField).grid(row=14, column=1, ipady=5, padx=(30, 30), pady=(40, 10))

    Label(app, text="", width=10, fg='white', bg='#232F3B').grid(row=15)

    Label(app, text="Password", font='none 15 bold', width=10, fg='white', bg='#232F3B').grid(row=16)
    Entry(app, width=40, textvariable = passwordField).grid(row=16, column=1, ipady=5)


    Label(app, text="", width=10, fg='red', bg='#232F3B').grid(row=17)


    
    loginSubmitBTN = Button(app,bg="#3b8bbc", fg="white", text="LOGIN",relief=RAISED,
                            borderwidth=1, font="none 15 bold", width=20, height=1, command=loginCheck).grid(row=18, column=1, padx=(10, 10), pady=(40, 10))
    Label(app, text="....... ........ ....... ........ ......... ....... ......", font='none 10 bold', fg='#232F3B', bg='#232F3B').grid(row=20, column=0, padx=(10, 10))








app=Tk()
app.title("Login panel of Student Attendance System")
userIdField=StringVar()
passwordField=StringVar()


teacherName=''
gotoPage=0
destroyValue=0
userImageField=StringVar()
takesID=0
selectIndexNo=-1
detailsDestroy=0
dateOfClass=0

w = 710
h = 700
ws = app.winfo_screenwidth()
hs = app.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

mainLoginPage()

app.geometry('%dx%d+%d+%d' % (w, h, x, y))
app.configure(background="#232F3B")
app.mainloop()





