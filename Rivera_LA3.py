import tkinter as tk
from tkinter.messagebox import showerror
import sqlite3

root = tk.Tk()
root.title("SQLite3 Inventory Management")
root.geometry("600x200")
root.resizable(False,False)



# Connect to the SQLite database (inventory.db) or create if not exists
conn = sqlite3.connect("inventory.db")
c = conn.cursor()

# Create the products table if it doesn't exist
c.execute("""
    CREATE TABLE IF NOT EXISTS products (
        ID INTEGER PRIMARY KEY,
        Name TEXT,
        Price REAL,
        Quantity INTEGER
    )
""")
conn.commit()

# Create GUI components
frame = tk.Frame(root, bg='#ADD8E6')
frame.pack(fill="both", expand=True)



label = tk.Label(frame, text="Inventory Management", font=("Arial", 14, "bold"))
label.pack(pady=20)

button_frame = tk.Frame(frame)
button_frame.pack()

# Function to add a new product to the database
def add_product():
    add_window = tk.Toplevel(root)
    add_window.title("Add Product")
    add_window.geometry("250x200")

    # Labels and entry fields for product details
    name_label = tk.Label(add_window, text="Product Name:")
    name_label.pack()
    name_entry = tk.Entry(add_window)
    name_entry.pack()

    price_label = tk.Label(add_window, text="Product Price:")
    price_label.pack()
    price_entry = tk.Entry(add_window)
    price_entry.pack()

    quantity_label = tk.Label(add_window, text="Product Quantity:")
    quantity_label.pack()
    quantity_entry = tk.Entry(add_window)
    quantity_entry.pack()

    # Function to add the product to the database
    def add_product_to_db():
        name = name_entry.get()
        price = price_entry.get()
        quantity = quantity_entry.get()

        # Validate input and insert into database
        if not all(c.isalpha() for c in name):
            tk.messagebox.showerror("Error", "Product name should contain only letters.")
            return

        try:
            price = float(price)
            quantity = int(quantity)
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid input for price or quantity.")
            return

        c.execute("INSERT INTO products (Name, Price, Quantity) VALUES (?,?,?)", (name, price, quantity))
        conn.commit()
        add_window.destroy()

    add_button = tk.Button(add_window, text="Add", command=add_product_to_db)
    add_button.pack()

# Function to view all products
def view_products():
    view_window = tk.Toplevel(root)
    view_window.title("View Products")
    view_window.geometry("300x100")  # Set the width and height of the window

    # Retrieve and display all products from the database
    c.execute("SELECT * FROM products")
    rows = c.fetchall()

    product_list = tk.Listbox(view_window, width=80)  # Set the width of the Listbox
    product_list.pack()

    for row in rows:
        product_list.insert("end", f"ID: {row[0]}, Name: {row[1]}, Price: ₱{row[2]:.2f}, Quantity: {row[3]}")

# Function to update a product
def update_product():
    update_window = tk.Toplevel(root)
    update_window.title("Update Product")
    update_window.geometry("300x200")

    # Labels and entry fields for product details
    id_label = tk.Label(update_window, text="Product ID:")
    id_label.pack()
    id_entry = tk.Entry(update_window)
    id_entry.pack()

    name_label = tk.Label(update_window, text="New Product Name:")
    name_label.pack()
    name_entry = tk.Entry(update_window)
    name_entry.pack()

    price_label = tk.Label(update_window, text="New Product Price:")
    price_label.pack()
    price_entry = tk.Entry(update_window)
    price_entry.pack()

    quantity_label = tk.Label(update_window, text="New Product Quantity:")
    quantity_label.pack()
    quantity_entry = tk.Entry(update_window)
    quantity_entry.pack()

    # Function to update product in the database
    def update_product_in_db():
        id = id_entry.get()
        name = name_entry.get()
        price = price_entry.get()
        quantity = quantity_entry.get()

        # Validate input and update the database
        if not id:
            tk.messagebox.showerror("Error", "Product ID is required.")
            return

        try:
            id = int(id)
            price = float(price)
            quantity = int(quantity)
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid input for ID, price, or quantity.")
            return

        c.execute("SELECT * FROM products WHERE ID = ?", (id,))
        result = c.fetchone()

        if not result:
            tk.messagebox.showerror("Error", "Invalid product ID.")
            return

        # Execute SQL UPDATE command to update product information in the database
        c.execute("""
            UPDATE products SET
                Name = ?,
                Price = ?,
                Quantity = ?
            WHERE ID = ?
        """, (name, price, quantity, id))
        conn.commit()
        update_window.destroy()

    update_button = tk.Button(update_window, text="Update", command=update_product_in_db)
    update_button.pack()

# Function to remove a product
def remove_product():
    remove_window = tk.Toplevel(root)
    remove_window.title("Remove Product")
    remove_window.geometry("300x100")

    # Label and entry field for product ID
    id_label = tk.Label(remove_window, text="Product ID:")
    id_label.pack()
    id_entry = tk.Entry(remove_window)
    id_entry.pack()

    # Function to remove the product from the database
    def remove_product_from_db():
        id = id_entry.get()

        # Check if the product ID is provided
        if not id:
            tk.messagebox.showerror("Error", "Product ID is required.")
            return

        # Validate and convert the product ID to an integer
        try:
            id = int(id)
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid input for product ID.")
            return

        c.execute("DELETE FROM products WHERE ID =?", (id,))
        conn.commit()

        # Update IDs of products with higher IDs
        c.execute("SELECT ID FROM products WHERE ID >?", (id,))
        ids_to_update = c.fetchall()
        for product_id in ids_to_update:
            c.execute("UPDATE products SET ID =? WHERE ID =?", (product_id[0] - 1, product_id[0]))
        conn.commit()

        remove_window.destroy()

    remove_button = tk.Button(remove_window, text="Remove", command=remove_product_from_db)
    remove_button.pack()

# Buttons for their respective actions.
add_button = tk.Button(button_frame, text="Add Product", command=add_product, font=("Arial", 12))
add_button.pack(side="left")

view_button = tk.Button(button_frame, text="View Products", command=view_products, font=("Arial", 12))
view_button.pack(side="left")

update_button = tk.Button(button_frame, text="Update Product", command=update_product, font=("Arial", 12))
update_button.pack(side="left")

remove_button = tk.Button(button_frame, text="Remove Product", command=remove_product, font=("Arial", 12))
remove_button.pack(side="left")

exit_button = tk.Button(button_frame, text="Exit", command=root.destroy, font=("Arial", 12))
exit_button.pack(side="left")

root.mainloop()