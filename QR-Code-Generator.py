from tkinter import *
import pyqrcode
from PIL import ImageTk,Image
root=Tk()
canvas=Canvas(root,width=400,height=600)
canvas.pack()
label=Label(root,text="QR CODE Generator",fg="blue",font=("Arial",30))
canvas.create_window(200,50,window=label)

root.mainloop()
