import tkinter as tk

window = tk.Tk()
window.title("BMI Calculator Pro")
window.geometry("400x500")
window.config(bg="lightblue")

# Title
tk.Label(window, text="BMI Calculator", bg="lightblue",
         font=("Arial", 16, "bold")).pack(pady=10)

# Inputs
tk.Label(window, text="Weight (kg)", bg="lightblue").pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

tk.Label(window, text="Height (m)", bg="lightblue").pack()
height_entry = tk.Entry(window)
height_entry.pack()

# Result label
result_label = tk.Label(window, text="Your BMI:", bg="lightblue", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# History label (separate area)
history_label = tk.Label(window, text="", bg="lightblue", justify="left")
history_label.pack(pady=10)

# ---------------- FUNCTIONS ----------------

def save_bmi(bmi, category):
    with open("bmi_history.txt", "a") as file:
        file.write(f"BMI: {bmi:.2f} | Status: {category}\n")


def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if height <= 0:
            result_label.config(text="Height must be greater than 0!")
            return

        bmi = weight / (height * height)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal Weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"Your BMI: {bmi:.2f}\n{category}")

        save_bmi(bmi, category)

    except:
        result_label.config(text="Please enter valid numbers!")


def clear_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="Your BMI:")


def show_history():
    try:
        with open("bmi_history.txt", "r") as file:
            data = file.read()
        history_label.config(text=data)
    except:
        history_label.config(text="No history found")


def clear_history():
    open("bmi_history.txt", "w").close()
    history_label.config(text="History cleared!")

# ---------------- BUTTONS ----------------

tk.Button(window, text="Calculate BMI", command=calculate_bmi).pack(pady=5)

tk.Button(window, text="Clear Inputs", command=clear_fields).pack(pady=5)

tk.Button(window, text="Show History", command=show_history).pack(pady=5)

tk.Button(window, text="Clear History", command=clear_history).pack(pady=5)

# Run app
window.mainloop()
