from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tkinter Exam")
root.geometry("500x400")
root.resizable(False, False)

def greeting():
    messagebox.showinfo(message=f"Hello, {entry.get()}")

def change_font():
    if c1.get() == 1:
        entry.config(font=("Arial", 4, "normal"))
    elif c1.get() == 2:
        entry.config(font=("Arial", 8, "normal"))
    elif c1.get() == 3:
        entry.config(font=("Arial", 12, "normal"))

def add_items():
    listbox.insert(END, entry.get())


def about_info():
    messagebox.showinfo("About My Program", "Features:\n\n"
                        "You can personalize your greeting.\n"
                        "You can customize the size of the font.\n"
                        "You can add items on the list.\n\n"
                        "Made by: France Rivera")




label = Label(root, text="Enter your name")
label.grid(row=0, column=0)

entry = Entry(root)
entry.grid(row=0, column=1)

button = Button(root, text="Generate Greeting", command=greeting)
button.grid(row=1, column=1)

frame = Frame(root)
frame.grid(row=3, column=1)

c1 = IntVar()
op1 = Radiobutton(frame, text="Small", variable=c1, value=1, command=change_font)
op1.pack(anchor=W)
op2 = Radiobutton(frame, text="Medium", variable=c1, value=2, command=change_font)
op2.pack(anchor=W)
op3 = Radiobutton(frame, text="Large", variable=c1, value=3, command=change_font)
op3.pack(anchor=W)


scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, expand=True, fill=Y)

listbox = Listbox(frame, yscrollcommand=scrollbar.set, width=20, height=10)
listbox.pack()
listbox.insert(END, "Emilio Aguinaldo")
listbox.insert(END, "Ferdinand Marcos")
listbox.insert(END, "Rodrigo Duterte")
listbox.insert(END, "Gloria Arroyo")
listbox.insert(END, "Emilio Aguinaldo")

menubar = Menu(root)

new = Menu(menubar, tearoff=0)
menubar.add_command(label="New", command=add_items)


about = Menu(menubar, tearoff=0)
menubar.add_command(label="About", command=about_info)


root.config(menu=menubar)


root.mainloop()
