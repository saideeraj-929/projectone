import tkinter as tk

from tkinter import messagebox

window=tk.Tk()
window.title("Expense Tracker")
window.geometry("400x500")
window.config(bg="#EAF4FF")
FILE_NAME = "expenses.txt"

total = 0

tk.Label(
    window,
    text="Expense Name",
    bg="#EAF4FF",
    font=("Arial", 10, "bold")
).pack(pady=5)

expense_entry=tk.Entry(window,width=30)

expense_entry.pack()
 
tk.Label(
    window,
    text="Amount",
    bg="#EAF4FF",
    font=("Arial", 10, "bold")
).pack(pady=5)
amount_entry=tk.Entry(window,width=30)
amount_entry.pack()

def save_expenses():
    expenses = listbox.get(0, tk.END)
    with open(FILE_NAME,"w")as file:
        for expense in expenses:
            file.write(expense+"\n")


def load_expenses():
    global total
    
    try:
        with open(FILE_NAME,"r")as file:
            for line in file:
                item =line.strip()
                
                listbox.insert(tk.END,item)
                amount = float(item.split("$")[1])
                total += amount

        total_label.config(text=f"Total: ${total}")

    except FileNotFoundError:
        pass
def add_expense():
    global total

    expense = expense_entry.get()
    amount = amount_entry.get()

    if expense == "" or amount == "":
        messagebox.showwarning(
            "Warning",
            "Please fill all fields"
        )

    else:
        try:
            amount_value = float(amount)

            item = f"{expense} - ${amount}"

            listbox.insert(tk.END, item)

            total += amount_value

            total_label.config(
                text=f"Total: ${total}"
            )
            save_expenses()
            expense_entry.delete(0, tk.END)
            amount_entry.delete(0, tk.END)

        except ValueError:
            messagebox.showwarning(
                "Warning",
                "Amount must be a number"
            )
def delete_expense():
    global total

    selected = listbox.curselection()

    if selected:
        item = listbox.get(selected[0])

        amount = float(item.split("$")[1])

        total -= amount

        total_label.config(text=f"Total: ${total}")

        listbox.delete(selected[0])
        save_expenses()
    else:
        messagebox.showwarning(
            "Warning",
            "Please select an expense"
        )
def clear_expenses():
    global total
    
    listbox.delete(0,tk.END)
    
    total =0
    
    total_label.config(text="Total: $0")
    save_expenses()

delete_button = tk.Button(
    window,
    text="Delete Expense",
    command=delete_expense,
    bg="#F44336",
    fg="white",
    font=("Arial", 10, "bold"),
    width=15
)
delete_button.pack(pady=5)
clear_button = tk.Button(
    window,
    text="Clear All",
    command=clear_expenses,
    bg="#FF9800",
    fg="white",
    font=("Arial", 10, "bold"),
    width=15
)
clear_button.pack(pady=5)

add_button = tk.Button(
    window,
    text="Add Expense",
    command=add_expense,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 10, "bold"),
    width=15
)    
add_button.pack(pady=5,padx=5)

total_label = tk.Label(
    window,
    text="Total: $0",
    font=("Arial", 14, "bold"),
    bg="#EAF4FF",
    fg="#0D47A1"
)
total_label.pack(pady=10)

listbox=tk.Listbox(window,width=40,height=12,font=("Arial",10),bg="white",fg="black")
listbox.pack(pady=15)
load_expenses()
window.mainloop()
