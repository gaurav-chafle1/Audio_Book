from distutils.cmd import Command
import tkinter as tk
from tkinter import *
from typing import MutableMapping, MutableSet
from gtts import gTTS
from tkinter import ttk
from tkinter.ttk import Combobox
import pyttsx3
import os
from tkinter import filedialog
from playsound import playsound 


 
#tkinter window


app = Tk()
 
app.geometry("900x580")
 
app.title("Text to speech converter")
  
heading = Label(text="*  *  *  *  *  *  *  *     AUDIO BOOK     *  *  *  *  *  *  *  *",bg="wheat",fg="red",font=('algerian 20 bold'),width="500",height="3")
 
heading.pack()

app.config(bg="black")

engine = pyttsx3.init()

#speak button code

def speaknow():
    text = text_area.get(1.0,END)
    gender = gender_Combobox.get()
    speed = speed_Combobox.get()
    voices = engine.getProperty("voices")

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if (text):
        if (speed =='High'):
            engine.setProperty('rate',250)
            setvoice()
        elif (speed == 'Normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()


#SAVE the code button            

def download():
    text = text_area.get(1.0,END)
    gender = gender_Combobox.get()
    speed = speed_Combobox.get()
    voices = engine.getProperty("voices")

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()

    if (text):
        if (speed =='High'):
            engine.setProperty('rate',250)
            setvoice()
        elif (speed == 'Normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()

def openfile():
    text = text_area.get(1.0,END)
    gender = gender_Combobox.get()
    speed = speed_Combobox.get()
    voices = engine.getProperty("voices")

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.open_to_file(text,'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.open_to_file(text,'text.mp3')
            engine.runAndWait()

    if (text):
        if (speed =='High'):
            engine.setProperty('rate',250)
            setvoice()
        elif (speed == 'Normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()


#Label frame 

address_field = LabelFrame(app,text="Text to speech converter",bg="gray",font=('arial',11),fg='black',bd=5)
 
address_field.pack(fill="both",expand="yes",padx=15,pady=15)

button2 = Button(app,text="PLAY",command=speaknow,width="10",bg="#38f20a")
 
button2.place(x=200,y=480)

button4 = Button(app,text="Exit",command=app.destroy,width="10",bg="red")
 
button4.place(x=780,y=520)
n = StringVar()
lang=ttk.Combobox(app,width=10,font='arial 14',textvariable=n,values=['English','Hindi','Marathi','Punjabi','Tamil','Telugu','Urdu','Nepali','Gujarati','Sindhi','Oriya','Kashmiri','Kannada','Manipuri','Bangla'])
lang.place(x=640,y=308)
lang.set('English')

#TEXT BOX

text_area=Text(app,font='Robote 14',bg='white',relief=GROOVE,wrap=WORD)
text_area.place(x=30,y=130,width=500,height=280)

Label(app,text='VOICE',font='arial 15 bold',bg='#305065',fg='white').place(x=580,y=160)
Label(app,text='SPEED',font='arial 15 bold',bg='#305065',fg='white').place(x=760,y=160)
Label(app,text='LANGUAGE',font='arial 15 bold',bg='#305065',fg='white').place(x=650,y=270)

#voices

gender_Combobox=Combobox(app,values=['Male','Female'],font='arial 14',state='r',width=10)
gender_Combobox.place(x=550,y=200)
gender_Combobox.set("Male")

#speed

speed_Combobox=Combobox(app,values=['Normal','High','Low'],font='arial 14',state='r',width=10)
speed_Combobox.place(x=730,y=200)
speed_Combobox.set("Normal")

#save

save = Button(app,text="SAVE",command=download,width="10",bg="orange",)
save.place(x=330,y=480)

#OpenFile

openfile = Button(app,text="OPEN FILE",command=openfile,width="12",bg="aqua",)
 
openfile.place(x=70,y=480)

 #  Previous  Button

previous = Button(app,text='<< Previous',command=MutableMapping ,width='10',bg='olive')
previous.place(x=580,y=380)



# Next Button


Next = Button(app,text='Next >>',command=MutableMapping ,width='10',bg='olive')
Next.place(x=770,y=380)

mainloop()








































































































































