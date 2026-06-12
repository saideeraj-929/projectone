import tkinter as tk
 
window=tk.Tk()
window.title("calculator ")
window.geometry("300x300")
window.config(bg="gray")
# Addition functiion
def add():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1+num2
    result_label.config(text ="Result ="+str(result))
    
# Subtractiion function

def subtract():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1-num2
    result_label.config(text ="Result ="+str(result)
                        )
# Multiplycation function
    
def multiply():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1*num2
    result_label.config(text ="Result ="+str(result))
    
# division function

def divide():

    num1 = int(entry1.get())
    num2 = int(entry2.get())

    if num2 == 0:
        result_label.config(text="Cannot divide by zero")

    else:
        result = num1 / num2
        result_label.config(text="Result = " + str(result))
    
    
label1 =tk.Label(window,text="First Number")
label1.pack(pady=5)
entry1 =tk.Entry(window)
entry1.pack(pady=5)

label2 = tk.Label(window,text="Second Number")
label2.pack(pady=5)
entry2 = tk.Entry(window)
entry2.pack(pady=5)

add_button = tk.Button(window,text="Add",command=add)
add_button.pack(pady=5)

subtract_button = tk.Button( window,text="Subtract",command=subtract)
subtract_button.pack(pady=5)

multiply_button = tk.Button(window,text = "multiply",command = multiply)
multiply_button.pack(pady=5)

divide_button = tk.Button(window,text = "divide",command = divide)
divide_button.pack(pady=5)

result_label = tk.Label(window,text="")
result_label.pack(pady=5)

from tkinter import messagebox
import math

# ---------------- WINDOW ----------------
window = tk.Tk()

window.title("Scientific Calculator")
window.geometry("420x650")
window.config(bg="black")

# ---------------- ENTRY ----------------
entry = tk.Entry(
    window,
    font=("Arial", 24),
    bd=10,
    relief="ridge",
    justify="right",
    bg="gray10",
    fg="cyan",
    insertbackground="white"
)

entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# ---------------- HISTORY ----------------
history = tk.Text(
    window,
    height=6,
    font=("Arial", 12),
    bg="black",
    fg="lime",
    insertbackground="white"
)

history.pack(fill="both", padx=10, pady=5)

# ---------------- FUNCTIONS ----------------
def press(num):
    entry.insert(tk.END, num)

def clear():
    entry.delete(0, tk.END)

def clear_history():
    history.delete("1.0", tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate(event=None):

    try:
        expression = entry.get()

        result = eval(expression)

        history.insert(
            tk.END,
            f"{expression} = {result}\n"
        )

        entry.delete(0, tk.END)
        entry.insert(0, result)

    except:
        messagebox.showerror(
            "Error",
            "Invalid Input"
        )

def square_root():

    try:
        number = float(entry.get())

        result = math.sqrt(number)

        history.insert(
            tk.END,
            f"√{number} = {result}\n"
        )

        entry.delete(0, tk.END)
        entry.insert(0, result)

    except:
        messagebox.showerror(
            "Error",
            "Invalid Input"
        )

def square():

    try:
        number = float(entry.get())

        result = number ** 2

        history.insert(
            tk.END,
            f"{number}² = {result}\n"
        )

        entry.delete(0, tk.END)
        entry.insert(0, result)

    except:
        messagebox.showerror(
            "Error",
            "Invalid Input"
        )

# ---------------- FRAME ----------------
frame = tk.Frame(window, bg="black")
frame.pack()

# ---------------- BUTTON STYLE ----------------
btn_style = {
    "font": ("Arial", 18),
    "width": 5,
    "height": 2,
    "activebackground": "cyan",
    "activeforeground": "black",
    "bd": 3
}

# ---------------- BUTTONS ----------------
buttons = [

    ('7', 0, 0),
    ('8', 0, 1),
    ('9', 0, 2),
    ('/', 0, 3),

    ('4', 1, 0),
    ('5', 1, 1),
    ('6', 1, 2),
    ('*', 1, 3),

    ('1', 2, 0),
    ('2', 2, 1),
    ('3', 2, 2),
    ('-', 2, 3),

    ('0', 3, 0),
    ('.', 3, 1),
    ('+', 3, 2),
    ('=', 3, 3),

    ('C', 4, 0),
    ('⌫', 4, 1),
    ('√', 4, 2),
    ('x²', 4, 3),

]

# ---------------- CREATE BUTTONS ----------------
for (text, row, col) in buttons:

    # Equal Button
    if text == "=":

        btn = tk.Button(
            frame,
            text=text,
            command=calculate,
            bg="orange",
            fg="white",
            **btn_style
        )

    # Clear Button
    elif text == "C":

        btn = tk.Button(
            frame,
            text=text,
            command=clear,
            bg="red",
            fg="white",
            **btn_style
        )

    # Backspace Button
    elif text == "⌫":

        btn = tk.Button(
            frame,
            text=text,
            command=backspace,
            bg="purple",
            fg="white",
            **btn_style
        )

    # Square Root Button
    elif text == "√":

        btn = tk.Button(
            frame,
            text=text,
            command=square_root,
            bg="green",
            fg="white",
            **btn_style
        )

    # Square Button
    elif text == "x²":

        btn = tk.Button(
            frame,
            text=text,
            command=square,
            bg="blue",
            fg="white",
            **btn_style
        )

    # Number Buttons
    else:

        btn = tk.Button(
            frame,
            text=text,
            command=lambda t=text: press(t),
            **btn_style
        )

    btn.grid(
        row=row,
        column=col,
        padx=5,
        pady=5
    )

# ---------------- CLEAR HISTORY BUTTON ----------------
history_btn = tk.Button(
    window,
    text="Clear History",
    command=clear_history,
    font=("Arial", 14),
    bg="darkred",
    fg="white"
)

history_btn.pack(fill="both", padx=10, pady=10)

# ---------------- KEYBOARD SUPPORT ----------------
window.bind("<Return>", calculate)

# ---------------- RUN ----------------
window.mainloop()
