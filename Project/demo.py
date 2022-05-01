#This GUI app is Currently in Development.
from cProfile import label
from logging import root
from tkinter import *
import requests

root = Tk()
# Currency converter title
root.title("CURRENCY CONVERTER")
# Currency converter dimensions height,width
root.geometry("600x400")

e1 = Label(root, text="From Currency")
e1.pack()
e1 = Entry(root, bd =5)
e1.pack()
e1.pack()

e2 = Label(root, text="To Currency")
e2.pack()
e2 = Entry(root, bd =5)
e2.pack()
e2.pack()

e3 = Label(root, text="Amount")
e3.pack()
e3 = Entry(root, bd =5)
e3.pack()
e3.pack()


def myClick():
    myclick =label(root)
    myclick.pack()

myButton = Button(root, text = "CONVERT", width=17, command=myClick)
myButton.pack()

button_exit = Button(root, text = "EXIT PROGRAM", width=17, command=root.quit)
button_exit.pack()

root.mainloop()