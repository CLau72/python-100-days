from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


def button_click():
    text = input.get()
    my_label["text"] = text


#Label
my_label = Label(text="I am a label", font=("Times New Roman",24,"bold"))
my_label.grid(column=0, row=0)

# Buttons
button1 = Button(text="Click Me!", command=button_click)
button1.grid(column=1,row=1)

button2 = Button(text="I am also a button")
button2.grid(column=2, row=0)


# Entry
input = Entry()
input.grid(column=3, row=3)



window.mainloop()