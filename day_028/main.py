
from tkinter import *
import math

from numpy import short

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    title.config(text="Timer")
    checks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_stop():
    global reps
    reps += 1

    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps == 8:
        countdown(long_break_secs)
        title.config(text="Break", fg=RED, bg=YELLOW)
    elif reps % 2 == 0:
        countdown(short_break_secs)
        title.config(text="Rest", fg=PINK, bg=YELLOW)
    else:
        countdown(work_secs)
        title.config(text="Work", fg=GREEN, bg=YELLOW)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global reps
    global timer

    minutes = math.floor(count / 60)
    seconds = count % 60

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds:02d}")
    if count > 0:
       timer = window.after(1000, countdown, count - 1)
    else:
        start_stop()
        check_count = "✔" * math.floor(reps / 2)
        checks.config(text=check_count)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=95, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row = 1)

# Labels
title = Label(text="Timer", font= (FONT_NAME,40,"bold"),fg=GREEN, bg=YELLOW)
title.grid(column=1,row=0)

checks = Label(font=(FONT_NAME,20,"bold"), fg=GREEN, bg=YELLOW)
checks.grid(column=1, row=4)

# Buttons
start_stop_btn = Button(text="Start", command=start_stop)
start_stop_btn.grid(column=0, row=2)

# Buttons
reset_btn = Button(text="Reset", command=reset_timer)
reset_btn.grid(column=3, row=2)


window.mainloop()