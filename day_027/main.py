from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    if type(miles) != "str":
        km = int(miles * 1.6)
        label3.config(text=km)



window = Tk()
window.title("Miles to Kilometers")
window.config(padx=10, pady=10)


# Miles Input
miles_input = Entry(text=0)
miles_input.config(width=10)
miles_input.grid(column=1, row=0)


# Labels

label1 = Label(text="Miles")
label1.grid(column=2,row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = Label(text=0)
label3.grid(column=1, row=1)

label4 = Label(text="Km")
label4.grid(column=2, row=1)

# Button

calculate_btn = Button(text="Calculate", command=miles_to_km)
calculate_btn.grid(column=1, row=2)

window.mainloop()