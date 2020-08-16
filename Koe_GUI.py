# -*- coding: utf-8 -*-
"""
Created on Thu May 28 04:42:55 2020

@author: Salunke Sakshi
"""


from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

#the parent window created ....................
root=Tk() 


root.title("KoE")

root.wm_iconbitmap("C:/Users/harsida/Desktop/koeicon.ico")

root.resizable(0,0)




#WidthXHeight............................. 


canvas=Canvas(root,width=400,height=600)

#ImageDisplay ...........................

image=ImageTk.PhotoImage(Image.open("C:/Users/harsida/Desktop/Logo2.jpg"))

canvas.create_image(0,0,anchor=NW,image=image)


canvas.pack()

#msg_Window.........................

 

text = Label(root, text = " Hi I am Koe..", bg='white', justify='left')

text.place(relx=0.1, rely=0.75)


root.mainloop()                          

