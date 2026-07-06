import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List")
root.geometry("450x500")
root.resizable(False, False)

tasks = []


def add_task():
    task = task_entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task.")
        return

    tasks.append(task)
    listbox.insert(tk.END, "☐ " + task)
    task_entry.delete(0, tk.END)


def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        tasks.pop(index)
    except:
        messagebox.showwarning("Warning", "Select a task first.")


def mark_completed():
    try:
        index = listbox.curselection()[0]
        text = listbox.get(index)

        if text.startswith("☐"):
            text = text.replace("☐", "✔", 1)
            listbox.delete(index)
            listbox.insert(index, text)
    except:
        messagebox.showwarning("Warning", "Select a task first.")


def clear_all():
    if messagebox.askyesno("Confirm", "Clear all tasks?"):
        listbox.delete(0, tk.END)
        tasks.clear()


title = tk.Label(
    root,
    text="To-Do List",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

task_entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 12)
)
task_entry.pack(pady=5)

add_btn = tk.Button(
    root,
    text="Add Task",
    width=20,
    bg="#4CAF50",
    fg="white",
    command=add_task
)
add_btn.pack(pady=5)

frame = tk.Frame(root)
frame.pack()

scrollbar = tk.Scrollbar(frame)

listbox = tk.Listbox(
    frame,
    width=45,
    height=12,
    font=("Arial", 11),
    yscrollcommand=scrollbar.set
)

scrollbar.config(command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.pack()

complete_btn = tk.Button(
    root,
    text="Mark Completed",
    width=20,
    bg="#2196F3",
    fg="white",
    command=mark_completed
)
complete_btn.pack(pady=5)

delete_btn = tk.Button(
    root,
    text="Delete Task",
    width=20,
    bg="#FF9800",
    fg="white",
    command=delete_task
)
delete_btn.pack(pady=5)

clear_btn = tk.Button(
    root,
    text="Clear All",
    width=20,
    bg="#F44336",
    fg="white",
    command=clear_all
)
clear_btn.pack(pady=5)

footer = tk.Label(
    root,
    text="Developed using Python & Tkinter",
    fg="gray",
    font=("Arial", 9)
)
footer.pack(side="bottom", pady=10)

root.mainloop()