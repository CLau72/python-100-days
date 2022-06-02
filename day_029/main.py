
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- CONSTANTS --------------------------------#
WHITE = "#FFFFFF"
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():

    pass_input.delete(0,"end")

    nr_letters= random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    # Create empty list for characters
    password_chars = []

    # append characters into list to build up password

    password_chars += [random.choice(LETTERS) for n in range(1,nr_letters + 1)]
    password_chars += [random.choice(SYMBOLS) for n in range(1,nr_symbols + 1)]
    password_chars += [random.choice(NUMBERS) for n in range(1,nr_numbers + 1)]

    # Shuffle the password_chars list
    random.shuffle(password_chars)

    # Join chars together to make password string
    password = ''.join(password_chars)

    pass_input.insert(0,password)
    
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():

    website = website_input.get()
    user = user_input.get()
    password = pass_input.get()
    new_data = {
        website: {
            "email": user,
            "password": password,
        }
    }

    if website and user and password:

        confirmation = messagebox.askokcancel(title="Confirm?", message=f"Save {password} as password for \n {user} on {website}?" )

        if confirmation:
            try:
                with open(file="data.json", mode="r") as f:
                    data = json.load(f)
            except FileNotFoundError:
                data = {}
            finally:    
                data.update(new_data)
                with open(file="data.json", mode="w") as f:
                    json.dump(data,f, indent=4)
        
            website_input.delete(0,"end")
            pass_input.delete(0,"end")

    else:
        messagebox.showerror(title="Aw Beans", message="One or more fields requires an entry.")
# ---------------------------- SEARCH --------------------------------- #
def search():
    try:
        f = open("data.json", "r")
        search_data = json.load(f)
        website = website_input.get()
        user = search_data[website]["email"]
        password = search_data[website]["password"]
    except FileNotFoundError:
        messagebox.showerror(title="Aw Beans", message="No password data available")
    except KeyError:
        messagebox.showwarning(title="Website not found", message=f"No data for {website} available")
    else:
        messagebox.showinfo(title="Search Results", message=f"{website}\nUsername:\n{user}\nPassword:\n{password}\n\n Password copied to clipboard")
        pyperclip.copy(password)
    finally:
        f.close()

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
website_input.config(width=18)
website_input.grid(column=1, row=1)
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

search_button = Button(text="Search", command=search, width=14)
search_button.grid(column=2, row=1 )

window.mainloop()