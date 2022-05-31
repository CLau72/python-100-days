from cgitb import text
from ctypes import alignment
from tkinter import *
import random

# ---------------------------- CONSTANTS --------------------------------#
WHITE = "#FFFFFF"
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    with open(file="data.txt", mode="a") as f:
        website = website_input.get()
        user = user_input.get()
        password = pass_input.get()
        data = f"{website} | {user} | {password}\n"
        f.writelines(data)
    
    website_input.delete(0,"end")
    pass_input.delete(0,"end")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("MyPass")
window.config(padx=50,pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


# LABELS
website_label = Label(text="Website:", bg=WHITE)
website_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:", bg=WHITE)
user_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg=WHITE)
password_label.grid(column=0, row=3)

# INPUT FIELDS
website_input = Entry()
website_input.config(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

user_input = Entry()
user_input.config(width=35)
user_input.insert(0, "carselau@gmail.com")
user_input.grid(column=1, row=2, columnspan=2)

pass_input = Entry()
pass_input.config(width=18)
pass_input.grid(column=1, row=3)

# BUTTONS
gen_pass_button = Button(text="Generate Password", command=generate_pass, width=14)
gen_pass_button.grid(column=2, row=3)

add_pass_button = Button(text="Add", command=save_pass, width=33)
add_pass_button.grid(column=1, row=4, columnspan=2)

window.mainloop()