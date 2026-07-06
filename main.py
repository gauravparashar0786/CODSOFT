import tkinter as tk
from tkinter import messagebox


def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed!")
                return
            result = num1 / num2
        else:
            messagebox.showwarning("Warning", "Please select an operation.")
            return

        result_label.config(text=f"Result : {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")


def clear_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    operation_var.set("+")
    result_label.config(text="Result : ")


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x450")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Simple Calculator",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

tk.Label(root, text="First Number", font=("Arial", 11)).pack()

entry1 = tk.Entry(root, width=25, font=("Arial", 12))
entry1.pack(pady=5)

tk.Label(root, text="Second Number", font=("Arial", 11)).pack()

entry2 = tk.Entry(root, width=25, font=("Arial", 12))
entry2.pack(pady=5)

operation_var = tk.StringVar()
operation_var.set("+")

operations = ["+", "-", "*", "/"]

tk.Label(root, text="Select Operation", font=("Arial", 11)).pack(pady=5)

operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.config(width=15)
operation_menu.pack()

calculate_btn = tk.Button(
    root,
    text="Calculate",
    width=18,
    command=calculate,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold")
)
calculate_btn.pack(pady=10)

clear_btn = tk.Button(
    root,
    text="Clear",
    width=18,
    command=clear_fields,
    bg="#f44336",
    fg="white",
    font=("Arial", 11, "bold")
)
clear_btn.pack()

result_label = tk.Label(
    root,
    text="Result : ",
    font=("Arial", 14, "bold")
)
result_label.pack(pady=20)

root.mainloop()