from tkinter import *
import pyscreenrec
from PIL import Image,ImageTk
import cv2
import numpy as np
import pyautogui
import datetime
import time
import asyncio

root = Tk()
root.geometry("400x600")
root.title("Oleg Recorder")
root.config(background="#fff")
root.resizable(False,False)

rec = pyscreenrec.ScreenRecorder()



def start_rec():
    file = Filename.get()
    rec.start_recording(str(file+".mp4"), 5)
def stop_rec():
    rec.stop_recording()
def pause_rec():
    rec.pause_recording()
def resume_rec():
    rec.resume_recording()
#icon
image_icon = PhotoImage(file="icon.png")

#heading
lbl = Label(root,text="Oleg Recorder",background="#fff",font="arial 15 bold")
lbl.pack(pady=20)

img=Image.open("recording.png")
resized_img = img.resize((350, 255), Image.LANCZOS)
new_img=ImageTk.PhotoImage(resized_img)

Label(root,image=new_img,bd=0).pack(pady=30)

#entry
Filename=StringVar()
entry=Entry(root,textvariable=Filename,width=18,font="arial 15")
entry.place(x=110, y=435)
Filename.set("recording15")


#buttnos
start=Button(root,text="Start",font="arial 22",bd=0,command=start_rec)
start.place(x=155,y=380)

#pause button
img2=Image.open("pause.png")
resized_img2 = img2.resize((50, 50), Image.LANCZOS)
new_img2=ImageTk.PhotoImage(resized_img2)

pause=Button(root,image=new_img2,bd=0,bg="#fff",command=pause_rec)
pause.place(x=170,y=490)

#resume button
img3=Image.open("play.png")
resized_img3 = img3.resize((50, 50), Image.LANCZOS)
new_img3=ImageTk.PhotoImage(resized_img3)

resume=Button(root,image=new_img3,bd=0,bg="#fff",command=resume_rec)
resume.place(x=70,y=490)

#stop button
img4=Image.open("stop.png")
resized_img4 = img4.resize((50, 50), Image.LANCZOS)
new_img4=ImageTk.PhotoImage(resized_img4)


stop=Button(root,image=new_img4,bd=0,bg="#fff",command=stop_rec)
stop.place(x=270,y=490)
