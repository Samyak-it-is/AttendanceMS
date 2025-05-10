############################################# IMPORTING ################################################
from functions import *
import tkinter as tk
from tkinter import Menu, ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2,os
import csv
import numpy as np
from PIL import Image,ImageTk
import pandas as pd
import datetime
import time
from time import sleep
flag=True
############################################# FUNCTIONS ################################################
def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string,padx=0)
    clock.after(200,tick)

def changeOnHover(button, colorOnHover, colorOnLeave, fontcOnHover, fontcOnLeave):
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover,fg=fontcOnHover) if (button['state']!="disabled") else None)
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave, fg=fontcOnLeave) if flag else button.config(
            background="white", fg="black"))

def changeOnHoverClear(text,text2,button, colorOnHover, colorOnLeave, fontcOnHover, fontcOnLeave):
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover,fg=fontcOnHover))
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave, fg=fontcOnLeave))


    # button.bind("<Enter>", func=lambda e: button.config(
    #     background=colorOnHover,fg=fontcOnHover,text=text))
 
    # button.bind("<Leave>", func=lambda e: button.config(
    #     background=colorOnLeave, fg=fontcOnLeave,text=text2))
    
############################################################################

################################################################################

def mode(menu):
    global flag
    if(flag):
        
        window.configure(background='white')
        frame1['highlightbackground']="black"
        frame2['highlightbackground']="black"
        frame1['bg']="white"
        frame2['bg']="white"
        frame3['bg']="white"
        txt['relief']="solid"
        txt2['relief']="solid"
        txt['borderwidth']=2
        txt2['borderwidth']=2
        message3['bg']="white"
        message3['fg']="black"
        datef['bg']="white"
        clock['bg']="white"
        takeImg['bg']="white"
        trainImg['bg']="white"
        trackImg['bg']="white"
        Att['bg']="white"
        takeImg['fg']="black"
        trainImg['fg']="black"
        trackImg['fg']="black"
        Att['fg']="black"
        lbl['bg']="#262523"
        lbl['fg']="white"
        lbl2['bg']="#262523"
        lbl2['fg']="white"
        lbl3['bg']="#262523"
        lbl3['fg']="white"
        message['bg']="#262523"
        message['fg']="white"
        message1['bg']="white"
        message1['fg']="black"
        # m['text']="Dark Mode"
        Menu.entryconfigure(menu,index=0, label="Dark Mode")
        btn_day.place(x=0,y=0)
        btn_night.place_forget()
        lbl_mode.pack_forget()
        lbl_mode2.pack()
        flag=False
    else:
        window.configure(background='#262523')
        frame1['highlightbackground']="white"
        frame2['highlightbackground']="white"
        frame1['bg']="#262523"
        frame2['bg']="#262523"
        frame3['bg']="#262523"
        txt['relief']="solid"
        txt2['relief']="solid"
        txt['borderwidth']=2
        txt2['borderwidth']=2
        message3['bg']="#262523"
        message3['fg']="white"
        datef['bg']="#262523"
        clock['bg']="#262523"
        btn_night.place(x=40,y=0)
        btn_day.place_forget()
        lbl_mode2.pack_forget()
        lbl_mode.pack()
        takeImg['bg']="#262523"
        trainImg['bg']="#262523"
        trackImg['bg']="#262523"
        Att['bg']="#262523"
        takeImg['fg']="white"
        trainImg['fg']="white"
        trackImg['fg']="white"
        Att['fg']="white"
        lbl['bg']="#00aeff"
        lbl['fg']="black"
        lbl2['bg']="#00aeff"
        lbl2['fg']="black"
        lbl3['bg']="#00aeff"
        lbl3['fg']="black"
        message['bg']="#262523"
        message['fg']="white"
        message1['bg']="#262523"
        message1['fg']="white"
        # m['text']="Light Mode"
        menu.entryconfigure(0, label="Light Mode")
        flag=True
    # frame1.bind("<Enter>", func=lambda e: button.config(
    #     background=colorOnHover,fg=fontcOnHover,text=text))
 
    # button.bind("<Leave>", func=lambda e: button.config(
    #     background=colorOnLeave, fg=fontcOnLeave,text=text2))









# ######################################## USED STUFFS ############################################
    
# global key
# key = ''

# ts = time.time()
# date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
# day,month,year=date.split("-")

# mont={'01':'January',
#       '02':'February',
#       '03':'March',
#       '04':'April',
#       '05':'May',
#       '06':'June',
#       '07':'July',
#       '08':'August',
#       '09':'September',
#       '10':'October',
#       '11':'November',
#       '12':'December'
#       }
window = tk.Tk()
window.geometry("1280x720")
window.resizable(True,False)
window.title("Attendance System")
window.configure(background='#262523')



frame1 = tk.Frame(window, bg="#262523",highlightbackground="white", highlightthickness=2)
frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)

frame2 = tk.Frame(window, bg="#262523",highlightbackground="white", highlightthickness=2)
frame2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)

message3 = tk.Label(window, text="Face Recognition Based Attendance System" ,fg="white",bg="#262523" ,height=1,font=('times', 29, ' bold '))
message3.place(relx=0.28, y=10)

frame3 = tk.Frame(window, bg="#262523")
frame3.place(relx=0.31, rely=0.08, relwidth=0.35, relheight=0.07)

# frame4 = tk.Frame(window, bg="#c4c6ce")
# frame4.place(relx=0.37, rely=0.09, relwidth=0.14, relheight=0.07)

photo=Image.open("Picture1.png")
photo=photo.resize((80,40))
photo2=Image.open("Picture2.png")
photo2=photo2.resize((80,40))
photo_day=Image.open("Day1.png")
photo_day=photo_day.resize((40,40))
photo_night=Image.open("Night1.png")
photo_night=photo_night.resize((40,40))
img = ImageTk.PhotoImage(photo)
img2 = ImageTk.PhotoImage(photo2)
img_day = ImageTk.PhotoImage(photo_day)
img_night = ImageTk.PhotoImage(photo_night)
frame_mode = tk.Frame(window, bg="#262523")
frame_mode.place(relx=0.93, rely=0.03, width=80, height=40)
lbl_mode=tk.Label(frame_mode,image=img,borderwidth=0)
lbl_mode2=tk.Label(frame_mode,image=img2,borderwidth=0)
lbl_mode.pack()

btn_day=tk.Button(frame_mode,image=img_day,bd=0,highlightthickness=0)
# btn_day.place(x=0,y=0)
btn_night=tk.Button(frame_mode,image=img_night,highlightthickness=0,bd=0)
btn_night.place(x=40,y=0)


datef = tk.Label(frame3, text = day+"-"+mont[month]+"-"+year+"  |", fg="#e58905",bg="#262523",padx=10,height=1,font=('times', 22, ' bold '))
# datef.pack(fill='both',expand=1)
datef.place(relx=0.15,rely=0.18)

clock = tk.Label(frame3,fg="#e58905",bg="#262523",padx=10,height=1,font=('times', 22, ' bold '),justify='left')
# clock.pack(fill='both',expand=1)
clock.place(relx=0.65,rely=0.18)

tick()


head2 = tk.Label(frame2, text="", padx=1000,fg="black",bg="#dfdfdf" ,font=('times', 17, ' bold '))
head2.place(relx=0,rely=0)
head2 = tk.Label(frame2, text="For New Registrations", padx=10,fg="black",bg="#dfdfdf" ,font=('times', 17, ' bold '))
head2.place(relx=0.3,rely=0)

head1 = tk.Label(frame1, text="", padx=1000,fg="black",bg="#dfdfdf" ,font=('times', 17, ' bold '))
head1.place(x=0,y=0)
head1 = tk.Label(frame1, text="For Already Registered", padx=10,fg="black",bg="#dfdfdf" ,font=('times', 17, ' bold '))
head1.place(relx=0.3,rely=0)

lbl = tk.Label(frame2, text="Enter ID",width=20  ,height=1  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold ') )
lbl.place(relx=0.25, y=75)

txt = tk.Entry(frame2,width=28 ,fg="black",font=('times', 15, ' bold '))
txt.place(relx=0.25, y=108)

lbl2 = tk.Label(frame2, text="Enter Name",width=20  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold '))
lbl2.place(relx=0.25, y=160)

txt2 = tk.Entry(frame2,width=28 ,fg="black",font=('times', 15, ' bold ')  )
txt2.place(relx=0.25, y=193)

message1 = tk.Label(frame2, text="1)Take Images  >>>  2)Save Profile" ,bg="#262523" ,fg="white"  ,width=39 ,height=1, activebackground = "yellow" ,font=('times', 15, ' bold '))
message1.place(relx=0.09, y=250)

message = tk.Label(frame2, text="" ,bg="#00aeff" ,fg="black"  ,width=39,height=1, activebackground = "yellow" ,font=('times', 16, ' bold '))
message.place(relx=0.09, rely=0.9)

lbl3 = tk.Label(frame1, text="Attendance",width=20  ,fg="black"  ,bg="#00aeff"  ,height=1 ,font=('times', 17, ' bold '))
lbl3.place(relx=0.25, y=43)

res=0
exists = os.path.isfile("StudentDetails/StudentDetails.csv")
if exists:
    with open("StudentDetails/StudentDetails.csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for l in reader1:
            res = res + 1
    res = (res // 2)
    csvFile1.close()
else:
    res = 0
message.configure(text='Total Registrations till now  : '+str(res))

##################### MENUBAR #################################

menubar = tk.Menu(window,relief='ridge')
filemenu = tk.Menu(menubar,tearoff=0)
filemenu.add_command(label='Light Mode', command=lambda:mode(filemenu))
filemenu.add_command(label='Change Password', command = change_pass)
filemenu.add_command(label='Contact Us', command = contact)
filemenu.add_command(label='Exit',command = lambda:psw_quit(window))
menubar.add_cascade(label='Help',font=('times', 29, ' bold '),menu=filemenu)

################## TREEVIEW ATTENDANCE TABLE ####################
style=ttk.Style()
style.theme_use('clam')
style.configure("Treeview.Heading", background="#8fc42b")
tv= ttk.Treeview(frame1,height =13,columns = ('name','date','time'))

tv.column('#0',width=91)
tv.column('name',width=139)
tv.column('date',width=142)
tv.column('time',width=139)
tv.grid(row=2,column=0,padx=(40,0),pady=(80,0),columnspan=4)
tv.heading('#0',text ='ID')
tv.heading('name',text ='NAME')
tv.heading('date',text ='DATE')
tv.heading('time',text ='TIME')

###################### SCROLLBAR ################################

scroll=ttk.Scrollbar(frame1,orient='vertical',command=tv.yview)
scroll.grid(row=2,column=4,padx=(0,100),pady=(80,0),sticky='ns')
tv.configure(yscrollcommand=scroll.set)

###################### BUTTONS ##################################

clearButton = tk.Button(frame2, text="Clear", command=lambda:clear(txt,message1)  ,fg="black"  ,bg="#ff8d84"  ,width=6 ,activebackground = "white" ,font=('times', 10, ' bold '), borderwidth=6)
clearButton.place(relx=0.74, y=106)
clearButton2 = tk.Button(frame2, text="Clear", command=lambda:clear2(txt2,message1)  ,fg="black"  ,bg="#ff8d84"  ,width=6 , activebackground = "white" ,font=('times', 10, ' bold '), borderwidth=6)
clearButton2.place(relx=0.74, y=192)    
takeImg = tk.Button(frame2, text="Take Images", command=lambda:TakeImages(window,txt,txt2,message,message1,trainImg)  ,fg="white"  ,bg="#262523"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '), borderwidth=10)
takeImg.place(relx=0.13, y=300)
trainImg = tk.Button(frame2, text="Save Profile", command=lambda:psw(window,message,message1) ,fg="white"  ,bg="#262523"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '), borderwidth=10,state="disabled")
trainImg.place(relx=0.13, y=380)
trackImg = tk.Button(frame1, text="Take Attendance", command=lambda:TrackImages(window,tv)  ,fg="white"  ,bg="#262523"  ,width=35  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '), borderwidth=10)
trackImg.place(relx=0.13,y=400)
quitWindow = tk.Button(frame1, text="Quit", command=lambda:psw_quit(window)  ,fg="black"  ,bg="#ff8d84"  ,width=35 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '),borderwidth=10)
quitWindow.place(relx=0.13, y=550)
Att = tk.Button(frame1, text="Show Attendance", command=lambda:att(tv)  ,fg="white"  ,bg="#262523"  ,width=35 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '),borderwidth=10)
Att.place(relx=0.13, y=460)
# m = tk.Button(frame1, text="Light mode", command=lambda:mode(filemenu)  ,fg="white"  ,bg="#262523"  ,width=35 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '),borderwidth=10)
# m.place(x=30, y=490)
btn_day.bind("<Button-1>", func=lambda e: btn_day.config(
        command=mode(filemenu)))
btn_night.bind("<Button-1>", func=lambda e: btn_night.config(
        command=mode(filemenu)))
# btn_day.config(command=mode(filemenu))
# btn_night.config(command=mode(filemenu))

changeOnHover(takeImg, "#2df900", "#262523","black","white")
changeOnHover(trainImg, "#2df900", "#262523","black","white")

changeOnHoverClear(None,None,clearButton,"#ea2a2a","#ff8d84","black","black")
changeOnHoverClear(None,None,clearButton2,"#ea2a2a","#ff8d84","black","black")

changeOnHover(trackImg, "#2df900", "#262523","black","white")
changeOnHoverClear(None,None,quitWindow, "#ea2a2a","#ff8d84","black","white")
changeOnHover(Att, "#2df900", "#262523","black","white")

##################### END ######################################

window.configure(menu=menubar)
window.attributes('-fullscreen', True)
window.mainloop()

####################################################################################################
