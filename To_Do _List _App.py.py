import tkinter as tk
from tkinter import messagebox

FILE_NAME = "tasks.txt"

# ---------- WINDOW ----------
window = tk.Tk()
window.title("Pro To-Do App")
window.geometry("420x500")
window.config(bg="#1e1e1e")

# ---------- FUNCTIONS ----------
def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task")

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Select a task")

def clear_all():
    listbox.delete(0, tk.END)
    save_tasks()

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass

# ---------- TITLE ----------
title = tk.Label(
    window,
    text="MY TO-DO LIST",
    font=("Arial", 18, "bold"),
    bg="#1e1e1e",
    fg="white"
)
title.pack(pady=10)

# ---------- ENTRY ----------
entry = tk.Entry(
    window,
    font=("Arial", 12),
    width=30,
    bg="#2b2b2b",
    fg="white",
    insertbackground="white"
)
entry.pack(pady=10)

# ---------- BUTTON FRAME ----------
button_frame = tk.Frame(window, bg="#1e1e1e")
button_frame.pack(pady=5)

# Add Button
tk.Button(
    button_frame,
    text="Add",
    width=10,
    bg="#4CAF50",
    fg="white",
    command=add_task
).grid(row=0, column=0, padx=5)

# Delete Button
tk.Button(
    button_frame,
    text="Delete",
    width=10,
    bg="#f44336",
    fg="white",
    command=delete_task
).grid(row=0, column=1, padx=5)

# Clear Button
tk.Button(
    button_frame,
    text="Clear All",
    width=10,
    bg="#ff9800",
    fg="white",
    command=clear_all
).grid(row=0, column=2, padx=5)

# ---------- LISTBOX ----------
listbox_frame = tk.Frame(window)
listbox_frame.pack(pady=10)

scrollbar = tk.Scrollbar(listbox_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(
    listbox_frame,
    width=45,
    height=15,
    font=("Arial", 11),
    bg="#2b2b2b",
    fg="white",
    selectbackground="#4CAF50",
    yscrollcommand=scrollbar.set
)
listbox.pack()

scrollbar.config(command=listbox.yview)

# ---------- LOAD TASKS ----------
load_tasks()

# ---------- RUN ----------
window.mainloop()
