from tkinter import *
from tkinter import messagebox


def output():
    messagebox.showinfo("", "Hello World")


def click():
    top = Tk()
    top.geometry("100x100")
    my_button = Button(top, text="ClickMe", command=output)  # using function object to call function 'output'
    my_button.place(x=35, y=50)
    top.mainloop()


click()
