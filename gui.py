from tkinter import *
from tkinter import ttk
import time
import os

root=Tk(className='Ultimate cyka blyat fire хуй fucking GUI')
frames = [PhotoImage(file='ann.gif',format = 'gif -index %i' %(i)) for i in range(100)]
def cyka1(event):
    print("Cyka Blyat key is pressed congrats for being a CYKA")
def cyka2(event):
    print("Your keyboard have been blyaten successfully! idinakhuy!")
def pressed(event):
    style=ttk.Style()
    style.theme_use('winnative')
def pressed2(event):
    style=ttk.Style()
    style.theme_use('classic')
def SetResolution1(event):
    root.geometry("1024x768")
def SetResolution2(event):
    root.geometry("1080x1024")
def SetResolution3(event):
    root.geometry("800x600")
def SetGif(event):
    photo = PhotoImage(file = r"pic.png")
    label = Label(image = photo)
    label.pack()
def update(ind):
    frame = frames[ind]
    ind += 1
    label.configure(image=frame)
    root.after(100, update, ind)
    label = Label(root)
    label.pack()
root.geometry("1024x768")
root.bind('<Control-f>',cyka1)
root.bind('<Return>',cyka2)
entry1=ttk.Entry(root,width=60)
entry1.pack()
button1=ttk.Button(root,text='Go winnative!')
button1.pack()
button1.bind('<ButtonPress>',pressed)
button2=ttk.Button(root,text='Go classic!')
button2.pack()
button2.bind('<ButtonPress>',pressed2)
resolution1=ttk.Button(root,text='1024x768')
resolution1.pack()
resolution1.bind('<ButtonPress>',SetResolution1)
resolution2=ttk.Button(root,text='1080x1024')
resolution2.pack()
resolution2.bind('<ButtonPress>',SetResolution2)
resolution3=ttk.Button(root,text='800x600')
resolution3.pack()
resolution3.bind('<ButtonPress>',SetResolution3)
giff=ttk.Button(root,text="Load Gif")
giff.pack()
giff.bind('<ButtonPress>', SetGif)
root.mainloop()