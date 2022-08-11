from tkinter import *
text = "1. очистить res" \
       "2. *" \
       "3. /"


def add(inp_1: Entry, inp_2: Entry, res: Entry):
    try:
        print(f"{inp_1.get()} - {inp_2.get()} = {int(inp_1.get()) + int(inp_2.get())}")
        res.delete(0, END)
        res.insert(0, string=str(int(inp_1.get()) + int(inp_2.get())))
    except ValueError:
        print("Неверные значения!")


def minus(inp_1: Entry, inp_2: Entry, res: Entry):
    try:
        print(f"{inp_1.get()} - {inp_2.get()} = {int(inp_1.get()) - int(inp_2.get())}")
        res.delete(0, END)
        res.insert(0, string=str(int(inp_1.get()) - int(inp_2.get())))
    except ValueError:
        print("Неверные значения!")


window = Tk()
input_2 = Entry()
input_2.grid(column=1)
input_1 = Entry()
input_1.grid(column=0, row=0)
res = Entry(takefocus=True)
res.grid(column=2, row=0)
# title = Label(window, text="Нажми кнопку")
# title.grid(column=2, row=0)
but_1 = Button(window, text="+", width=15, height=7, bg="blue", fg="black", command=lambda: add(input_1, input_2, res))
but_1.grid(column=0, row=1)
but_2 = Button(window, text="-", width=15, height=7, bg="blue", fg="black", command=lambda: minus(input_1, input_2, res))
but_2.grid(column=1, row=1)
but_3 = Button(window, text="exit", width=15, height=7, bg="blue", fg="black", command=lambda: window.destroy())
but_3.grid(column=2, row=1)

window.mainloop()
