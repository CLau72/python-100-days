from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
word = {}
wordbank = None
wordbank_dict =[]


def reset_wordbank():
    global wordbank, wordbank_dict
    wordbank = pandas.read_csv("./data/french_words.csv")
    wordbank.to_csv("./data/words_to_learn.csv",index=False)
    wordbank_dict = wordbank.to_dict(orient="record")

def new_card():
    global word, flip_timer
    window.after_cancel(flip_timer)
    try:
        word = random.choice(wordbank_dict)
    except IndexError:
        list_reset = messagebox.askyesno(title="Wordlist Empty", message="Wordlist exhausted. You're so smart!\n Reset wordlist?")
        if list_reset:
            reset_wordbank()
            list_reset.destroy()
            new_card()
        else:
            window.destroy()
    else:    
        flashcard.itemconfig(language_text, text="French", fill="black")
        flashcard.itemconfig(word_text, text=word["French"], fill="black")
        flashcard.itemconfig(flashcard_color, image=white_card)
        flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global word
    flashcard.itemconfig(language_text, text="English", fill="white")
    flashcard.itemconfig(word_text, text=word["English"], fill="white")
    flashcard.itemconfig(flashcard_color, image=green_card)

def known_word():
    wordbank_dict.remove(word)
    wordbank = pandas.DataFrame(wordbank_dict)
    wordbank.to_csv("./data/words_to_learn.csv",index=False)
    new_card()

def unknown_word():
    new_card()

# Read in wordbank
try:
    wordbank = pandas.read_csv("./data/words_to_learn.csv")
except:
    reset_wordbank()
else:
    wordbank_dict = wordbank.to_dict(orient="records")

# ----------- UI Setup ---------- #

# Window Setup
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Setup flashcard
flashcard = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
white_card = PhotoImage(file="./images/card_front.png")
green_card = PhotoImage(file="./images/card_back.png")
flashcard_color = flashcard.create_image(403, 263, image=white_card)
language_text = flashcard.create_text(400, 150, text="Flashcards", font=LANGUAGE_FONT)
word_text = flashcard.create_text(400, 263, text="Click a button\nto begin", font=WORD_FONT)
flashcard.grid(column=0, row=0, columnspan=2)

# Buttons
correct_img = PhotoImage(file="./images/right.png")
correct_button = Button(image=correct_img, highlightthickness=0, command=known_word)
correct_button.grid(column=0, row=1)

incorrect_img = PhotoImage(file="./images/wrong.png")
incorrect_button = Button(image=incorrect_img, highlightthickness=0, command=unknown_word)
incorrect_button.grid(column=1, row=1)


new_card()

window.mainloop()