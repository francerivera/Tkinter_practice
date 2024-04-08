from tkinter import *
from tkinter import filedialog, simpledialog, messagebox, scrolledtext

root = Tk()
root.title("mid_LA3-RIVERA")
root.geometry("400x400")
root.resizable(False,False)

def open():
    fd = filedialog.askopenfile(mode='r')
    if fd:
        content = fd.read()
        fd.close()
        lines = content.split("\n")
        listbox.delete(0, END)
        for line in lines:
            listbox.insert(END, line)

def save():
    fd = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if fd:
        content = "\n".join(listbox.get(0, END))
        fd.write(content)
        fd.close()
        messagebox.showinfo("Save", "List saved successfully!")


def add():
    content = simpledialog.askstring(" ", "Enter item:")
    if content:
        listbox.insert(END, content)

def delete():
    selected_indices = listbox.curselection()
    for index in selected_indices[::1]:
        listbox.delete(index)

def edit_item():
    selected_indices = listbox.curselection()
    for index in selected_indices:
        current_content = listbox.get(index)
        edited_content = simpledialog.askstring("Edit Item", f"Edit New Item {index}:", initialvalue=current_content)
        if edited_content:
            listbox.delete(index)
            listbox.insert(index, edited_content)

def help_about():
    messagebox.showinfo("About My List Application", "Features:\n\n"
                        "File menu: \n"
                        " • Open - Open existing text files. \n"
                        " • Save - Save your text as a new file.\n\n"
                        "Edit menu: \n"
                        " • Add - Add new items on the list.\n"
                        " • Delete - Delete items from the list.\n"
                        " • Edit - Modify existing items on the list\n\n"
                        "Help menu: \n"
                        " • About - Display information about this application.\n\n"
                        "This is an interactive list application using Tkinter in Python.\n\n"
                        "Made by: France Raphael R. Rivera")


menubar = Menu(root)

file = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file)
file.add_command(label="Open...", command=open)
file.add_command(label="Save", command=save)

edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Add", command=add)
edit.add_command(label="Delete", command=delete)
edit.add_command(label="Edit", command=edit_item)

help = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help)
help.add_command(label="About", command=help_about)

root.config(menu=menubar)


frame = Frame(root, width=400, height=400, bg="#79d083")
frame.pack(fill=X, expand=True)

label = Label(frame, text="List Application", font=("Arial", 16, "bold"), bg="#79d083")
label.pack(pady=10)


frame2 = Frame(frame, width=400, height=400, bg="#79d083")
frame2.pack()


scrollbar = Scrollbar(frame2)
scrollbar.pack(side=RIGHT, fill=Y, pady=30)

listbox = Listbox(frame2, width=40, height=30, yscrollcommand=scrollbar.set)
listbox.pack(pady=30)


root.mainloop()

