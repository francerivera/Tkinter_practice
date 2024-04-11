from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tkinter Exam")
root.geometry("500x400")
root.resizable(False, False)


def greeting():
    messagebox.showinfo(message=f"Hello, {entry.get()}")

def font_size():
    if selected.get() == 1:
        entry.config(font=("Arial", 8, "normal"))
    elif selected.get() == 2:
        entry.config(font=("Arial", 10, "normal"))
    elif selected.get() == 3:
        entry.config(font=("Arial", 12, "normal"))

label = Label(root, text="Enter your name")
label.grid(row=0, column=0)

entry = Entry(root)
entry.grid(row=0, column=1)

button = Button(root, text="Generate Greeting", command=greeting)
button.grid(row=1, column=1)

frame = Frame(root)
frame.grid(row=3, column=1)

selected = IntVar()
op1 = Radiobutton(frame, text="Small", value=1, variable=selected, command=font_size)
op1.pack(anchor=W)

op2 = Radiobutton(frame, text="Medium", value=2, variable=selected, command=font_size)
op2.pack(anchor=W)

op3 = Radiobutton(frame, text="Large", value=3, variable=selected, command=font_size)
op3.pack(anchor=W)


root.mainloop()
