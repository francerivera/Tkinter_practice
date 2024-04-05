from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry("400x300")
root.title("Tkinter Exam")
root.resizable(False, False)


def click():
    messagebox.showinfo(message="Button Clicked!")

def submit():
    messagebox.showinfo(message=f"Hello, {entry.get()}")

def change_color(event):
    selected_indices = listbox.curselection()
    if selected_indices:
        selected_colors = listbox.get(selected_indices[0])
        root.configure(bg=selected_colors)

def text_color():
    if c1.get() == 1:
        entry.config(fg="red")
    else:
        entry.config(fg="black")

def change_font():
    if c2.get() == 1:
        entry.config(font=("Arial", 8, "bold"))
    else:
        entry.config(font=("Arial", 8, "normal"))

def state():
    if c3.get() == 1:
        entry.config(state=DISABLED)
    else:
        entry.config(state=NORMAL)

def exit_button():
    root.quit()



label = Label(text="Welcome to Tkinter Exam")
label.pack(anchor=N)

button = Button(text="Click Me", command=click)
button.pack()

entry = Entry(root)
entry.pack()

button1 = Button(text="Submit", command=submit)
button1.pack()


listbox = Listbox(root, width=10, height=5)
listbox.insert(END, "Red")
listbox.insert(END, "Blue")
listbox.insert(END, "Green")
listbox.insert(END, "Purple")
listbox.insert(END, "Orange")
listbox.pack()

listbox.bind("<<ListboxSelect>>", change_color)

c1 = IntVar()
op1 = Checkbutton(text="Option 1", variable=c1, command=text_color)
op1.pack()

c2 = IntVar()
op2 = Checkbutton(text="Option 2", variable=c2, command=change_font)
op2.pack()

c3 = IntVar()
op3 = Checkbutton(text="Option 3", variable=c3, command=state)
op3.pack()


button2 = Button(root, text="Exit", command=exit_button)
button2.pack(anchor=S)


root.mainloop()
