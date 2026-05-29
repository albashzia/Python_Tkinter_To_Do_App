from tkinter import *
from tkinter.font import BOLD

window = Tk()

window.title("To Do App")
window.geometry("350x500")

title_label = Label(window,
                    text="To-Do App",
                    font=("Ink Free",20,BOLD),
                    fg="black",
                    bg="white"
)
title_label.place(x=105,y=10)

window.mainloop()