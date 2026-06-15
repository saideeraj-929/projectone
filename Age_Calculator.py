import tkinter as tk
from datetime import datetime
from tkinter import messagebox
window = tk.Tk()
window.title("Age Calculator")
window.geometry("350x300")
window.config(bg="#EAF4FF")

tk.Label(window, text="Birth Year").pack(pady=5)

year_entry = tk.Entry(window)
year_entry.pack()
def calculate_age():
    # Get the input from the Entry box
    birth_year = year_entry.get()
    if birth_year.isdigit():
        current_year = datetime.now().year
        age = current_year - int(birth_year)
        if age < 13:
            category = "Child"
        elif age < 20:
            category = "Teen"
        elif age < 60:
            category = "Adult"
        else:
            category = "Senior"

        result_label.config(
        text=f"Age: {age}\nCategory: {category}"
)
    else:
        messagebox.showwarning(
    "Warning",
    "Please enter a valid year"
)
calculate_button = tk.Button(
    window,
    text="Calculate Age",
    command=calculate_age,
    bg="#4CAF50",
    fg="white",
    activebackground="#2E7D32",
    activeforeground="white",
    font=("Arial", 10, "bold")
)

calculate_button.pack()
result_label = tk.Label(window, text="Your Age:")
result_label.pack(pady=20)

window.mainloop()
