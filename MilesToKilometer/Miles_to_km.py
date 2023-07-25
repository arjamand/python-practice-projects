# 2023-01-16 22:34:24

from tkinter import *

window = Tk()
window.minsize(width=350, height=150)
window.title("Miles To Kilometer")
window.config(padx=15, pady=35)


def Calculate():
    label_4["text"] = round((int(input.get())) * 1.6)
    label_4.grid()


label_1 = Label(text="                                    ")
label_1.grid(row=0, column=0)

input = Entry()
input.grid(row=0, column=1)

label_2 = Label(text="   is equal to", font=("Arial", 11))
label_2.grid(row=1, column=0)

label_3 = Label(text="   miles", font=("Arial", 11))
label_3.grid(row=0, column=2)

label_4 = Label(text="      ", font=("Arial", 11))
label_4.grid(row=1, column=1)

label_5 = Label(text="  km", font=("Arial", 11))
label_5.grid(row=1, column=2)

button_1 = Button(text="Calculate", command=Calculate)
button_1.grid(row=2, column=1)


mainloop()
