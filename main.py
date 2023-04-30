from tkinter import *
from playsound import playsound
from PIL import Image, ImageTk
import pyglet
import time

def second(x,y,c):
    if c == True:
        f.config(state='disabled')
    elif  c == False:
        t.config(state='disabled')
    if x > 0:
        x-=1
        z = str(x)
        y['text'] = z
        root.after(1000,second,x,y,c)
        
    else :
        playsound('ses.mp3')
        if c == True:
            y['text'] = '150'
            f.config(state='normal')
            root.after_cancel(second)
        else :
            y['text'] = '100'
            t.config(state='normal')
            root.after_cancel(second)
pyglet.font.add_file('ds-digib.ttf')
flash= 'spells/Flash_HD.png'
tutustur='spells/tutuştur.png'

root = Tk()
img1 = ImageTk.PhotoImage(Image.open(flash))
img2 = ImageTk.PhotoImage(Image.open(tutustur))

root.title('Wildrift Büyü Takip Projesi v1')

f=Button(root,image=img1,command=lambda: second(150,flash_label,True))
f.grid(row=0,column=0)
t=Button(root,image=img2,command=lambda: second(100,tutusutur_label,c=False))
t.grid(row=1,column=1)

flash_label = Label(root,text='150', font=('DS-Digital',50))
flash_label.grid(row=0,column=1)
tutusutur_label=Label(root,text='100', font=('DS-Digital',50))
tutusutur_label.grid(row=1,column=0)

root.mainloop()