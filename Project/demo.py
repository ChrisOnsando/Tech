from cProfile import label
from cgitb import text
from logging import root
from tkinter import *
from tkinter import ttk
import requests

root = Tk()
# Currency converter title
root.title("CURRENCY CONVERTER")
# Currency converter dimensions height,width
root.geometry("600x400")

e1 = Entry(root)
e1.pack()

e2 = Entry(root)
e2.pack()

e3 = Entry(root)
e3.pack()

def myClick():
    mylabel1 =label(root)
    mylabel1.pack()

myButton = Button(root, text = "CONVERT", width=17, command=myClick)
myButton.pack()

button_quit = Button(root, text = "EXIT PROGRAM", width=17, command=root.quit)
button_quit.pack()

root.mainloop()