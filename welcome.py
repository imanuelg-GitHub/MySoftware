from tkinter import *
from tkinter import messagebox
import os


def outputNewScreen():
    messagebox.showinfo("", "New Screen")
    osCommandString = "notepad.exe file.txt"
    os.system(osCommandString)


def welcome():
    top = Tk()
    top.geometry("100x100")
    my_button = Button(top, text="ClickMe", command=outputNewScreen)  # using function object to call function 'outputNewScreen'
    my_button.place(x=35, y=50)
    top.mainloop()


welcome()
