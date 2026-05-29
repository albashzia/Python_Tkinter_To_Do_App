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

text_field = Text(window,
            bg="white",
            font=('Ink Free',12,BOLD),
            height=1,
            width=25,
            )
text_field.place(x=15,y=100)

add_button = Button(window,
                    text="Add",
                    font=("Ink Free",12,BOLD),
                    fg="white",
                    bg="light green",
                    height=1,
                    width=6,
                    activeforeground="white",
                    activebackground="light green")
add_button.place(x=275,y=95)

window.mainloop()