import tkinter as tk

window = tk.Tk()
window.title("Greetings App")
window.geometry("300x300")
window.config(bg="black")

def greet():
    name = entry.get()

    if name == "":
        result_label.config(text="Please enter your name!", fg="red")
    else:
        result_label.config(text=f"Hello, {name}!", fg="green")

def clear():
    entry.delete(0, tk.END)
    result_label.config(text="")

def exit_app():
    window.destroy()

entry = tk.Entry(window)
entry.pack(pady=10)

greet_button = tk.Button(window, text="Greet", command=greet)
greet_button.pack(pady=5)

clear_button = tk.Button(window, text="Clear", command=clear)
clear_button.pack(pady=5)

exit_button = tk.Button(window, text="Exit", command=exit_app)
exit_button.pack(pady=5)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()
