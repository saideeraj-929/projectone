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
    birth_year = year_entry.get().strip()

    if birth_year.isdigit():
        birth_year = int(birth_year)
        current_year = datetime.now().year

        if birth_year > current_year or birth_year < 1900:
            messagebox.showwarning("Warning", "Enter a valid year!")
            return

        age = current_year - birth_year

        if age < 13:
            category = "Child"
        elif age < 20:
            category = "Teen"
        elif age < 60:
            category = "Adult"
        else:
            category = "Senior"

        result_label.config(text=f"Age: {age}\nCategory: {category}")

    else:
        messagebox.showwarning("Warning", "Please enter numbers only")

calculate_button = tk.Button(
    window,
    text="Calculate Age",
    command=calculate_age,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 10, "bold")
)

calculate_button.pack(pady=10)

result_label = tk.Label(window, text="Your Age:")
result_label.pack(pady=20)

window.mainloop()
