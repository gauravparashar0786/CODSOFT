import tkinter as tk
from tkinter import messagebox
import random
import string

# ---------------- WINDOW ---------------- #
root = tk.Tk()
root.title("Password Generator")
root.geometry("450x500")
root.resizable(False, False)

# ---------------- VARIABLES ---------------- #
password_var = tk.StringVar()

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

# ---------------- FUNCTIONS ---------------- #
def generate_password():
    characters = ""

    if uppercase_var.get():
        characters += string.ascii_uppercase

    if lowercase_var.get():
        characters += string.ascii_lowercase

    if numbers_var.get():
        characters += string.digits

    if symbols_var.get():
        characters += "!@#$%^&*()_-+=<>?/"

    if characters == "":
        messagebox.showwarning(
            "Warning",
            "Please select at least one character type."
        )
        return

    try:
        length = int(length_entry.get())

        if length <= 0:
            raise ValueError

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter a valid password length."
        )
        return

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    password_var.set(password)


def copy_password():
    password = password_var.get()

    if password == "":
        messagebox.showwarning(
            "Warning",
            "Generate a password first."
        )
        return

    root.clipboard_clear()
    root.clipboard_append(password)

    messagebox.showinfo(
        "Copied",
        "Password copied to clipboard."
    )


def clear_fields():
    length_entry.delete(0, tk.END)
    password_var.set("")

    uppercase_var.set(True)
    lowercase_var.set(True)
    numbers_var.set(True)
    symbols_var.set(True)

# ---------------- TITLE ---------------- #
title = tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 18, "bold")
)

title.pack(pady=15)

# ---------------- LENGTH ---------------- #
tk.Label(
    root,
    text="Password Length",
    font=("Arial", 11)
).pack()

length_entry = tk.Entry(
    root,
    width=20,
    font=("Arial", 12)
)

length_entry.pack(pady=8)

# ---------------- CHECKBOXES ---------------- #
tk.Checkbutton(
    root,
    text="Uppercase Letters",
    variable=uppercase_var
).pack(anchor="w", padx=90)

tk.Checkbutton(
    root,
    text="Lowercase Letters",
    variable=lowercase_var
).pack(anchor="w", padx=90)

tk.Checkbutton(
    root,
    text="Numbers",
    variable=numbers_var
).pack(anchor="w", padx=90)

tk.Checkbutton(
    root,
    text="Symbols",
    variable=symbols_var
).pack(anchor="w", padx=90)
# ---------------- PASSWORD DISPLAY ---------------- #
tk.Label(
    root,
    text="Generated Password",
    font=("Arial", 11)
).pack(pady=(15, 5))

password_entry = tk.Entry(
    root,
    textvariable=password_var,
    width=35,
    font=("Arial", 12),
    justify="center"
)

password_entry.pack(pady=5)

# ---------------- BUTTONS ---------------- #
generate_btn = tk.Button(
    root,
    text="Generate Password",
    width=22,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold"),
    command=generate_password
)

generate_btn.pack(pady=10)

copy_btn = tk.Button(
    root,
    text="Copy Password",
    width=22,
    bg="#2196F3",
    fg="white",
    font=("Arial", 11, "bold"),
    command=copy_password
)

copy_btn.pack(pady=5)

clear_btn = tk.Button(
    root,
    text="Clear",
    width=22,
    bg="#F44336",
    fg="white",
    font=("Arial", 11, "bold"),
    command=clear_fields
)

clear_btn.pack(pady=5)

# ---------------- FOOTER ---------------- #
footer = tk.Label(
    root,
    text="Developed using Python & Tkinter",
    font=("Arial", 9),
    fg="gray"
)

footer.pack(side="bottom", pady=10)

# ---------------- MAIN LOOP ---------------- #
root.mainloop()