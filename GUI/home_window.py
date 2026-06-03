from tkinter import *
from tkinter.font import BOLD

from Code import to_do_app_code

def add_to_list():
    text = text_field.get(0,END)
    list.add_task(text)

window = Tk()

window.title("To Do App")
window.geometry("350x500")

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar)
menu_bar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Save")
file_menu.add_command(label="Load")
file_menu.add_command(label="Exit")

help_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Help",menu=help_menu)
help_menu.add_command(label="User Guide")


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
                    activebackground="light green",
                    command=add_to_list)
add_button.place(x=275,y=95)

list_box = Listbox(window,
                  bg='#F7FFDE',
                  font=('Constantia',14),
                  height=14,
                  width = 28,
                  selectmode=MULTIPLE
)
list_box.place(x = 15, y = 140)

list = to_do_app_code.list

for i in range(len(list)):
    list_box.insert(i,list[i])
window.mainloop()