from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math

Window = Tk()
Window.title("Calculator")
global N


# Logik
def calc(key):
    global memory
    if key == "=":
        strNumb = "0123456789"
        if calc_entry.get()[0] in strNumb:
            memory = key
        # Без букв
        str1 = "-+0123456789.*/^"
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "Не число!")
            messagebox.showerror("Error!", "Не число!")
        # Счёт
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, " = " + str(result))
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("Error!", "See for input!")
    # Clear display
    elif key == "C":
        calc_entry.delete(0, END)
    elif key == "+/-":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
    elif key == "^":
        calc_entry.delete(0, END)
        calc_entry.insert(END, memory)
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)


# Кнопочки
bttn_list = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "+/-",
    "0", ".", "C", "^", "*", "/", "%", "="
]
r = 1
c = 0

for i in bttn_list:
    rel = ""
    cmd = lambda x=i: calc(x)
    N = i
    ttk.Button(Window, text=i, command=cmd).grid(row=r, column=c)
    c += 1
    if c >= 4:
        c = 0
        r += 1
calc_entry = Entry(Window, width=40)
calc_entry.grid(row=0, column=0, columnspan=4)

Window.mainloop()
