from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry("600x400")
root.resizable(False,False)

def greeting():
    messagebox.showinfo(message=f"Hello, {entry.get()}")

def background():
    if c1.get() == 1:
        entry.config(bg="red")
    else:
        entry.config(bg="white")

def font():
    if c2.get() == 1:
        entry.config(fg="blue")
    else:
        entry.config(fg="black")

def state():
    if c3.get() == 1:
        entry.config(state=DISABLED)
    else:
        entry.config(state=NORMAL)

countries = ("Philippines", "China", "France", "Mexico", "Argentina", "Thailand", "Vietnam",
             "Canada", "Spain", "Italy", "Cambodia")

def file_exit():
    root.quit()

def help_about():
    messagebox.showinfo("About My Program", "Features:\n\n"
                        "* You can generate your own personal greeting by entering your name on the entry.\n\n"
                        "* You can customize the entry box by choosing on the three options.\n\n"
                        "* You can scroll the items on the list.\n\n"
                        "File manu - option to exit on the application.\n\n"
                        "Help menu - option to display information about this application\n\n"
                        "This is an interactive GUI program made in Python language.\n\n"
                        "Made by: France Raphael R. Rivera")




var = Variable(value=countries)

label = Label(root, text="Enter your name:")
label.grid(row=0, column=0)

entry = Entry(root)
entry.grid(row=0, column=1)

button = Button(root, text="Generate Greeting", command=greeting)
button.grid(row=1, column=1)

frame = Frame(root)
frame.grid(row=2, column=1)


c1 = IntVar()
op1 = Checkbutton(frame, text="Option 1", variable=c1, command=background)
op1.pack()

c2 = IntVar()
op2 = Checkbutton(frame, text="Option 2", variable=c2, command=font)
op2.pack()

c3 = IntVar()
op3 = Checkbutton(frame, text="Option 3", variable=c3, command=state)
op3.pack()

frame2 = Frame(root)
frame2.grid(row=5, column=1)

scrollbar = Scrollbar(frame2)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(frame2, yscrollcommand=scrollbar.set, listvariable=var)
listbox.pack()


menubar = Menu(root)

file = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file)
file.add_cascade(label="Exit", command=file_exit)

help = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help)
help.add_command(label="About", command=help_about)


root.config(menu=menubar)

root.mainloop()