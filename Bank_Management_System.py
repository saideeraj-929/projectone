import tkinter as tk
from tkinter import messagebox

# ---------------- ACCOUNT CLASS ----------------

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

# ---------------- WINDOW ----------------

window = tk.Tk()
window.title("Bank Management System")
window.geometry("450x450")
window.config(bg="#EAF4FF")

account = None
FILE_NAME = "account.txt"

# ---------------- FUNCTIONS ----------------

def save_account():
    if account:
        with open(FILE_NAME, "w") as file:
            file.write(f"{account.name},{account.balance}")

def load_account():
    global account

    try:
        with open(FILE_NAME, "r") as file:
            data = file.read().split(",")

            name = data[0]
            balance = float(data[1])

            account = BankAccount(name, balance)

            result_label.config(
                text=f"{name}'s Balance: ₹{balance}"
            )

    except FileNotFoundError:
        pass

def create_account():
    global account

    name = name_entry.get()

    if name == "":
        messagebox.showwarning(
            "Warning",
            "Enter customer name"
        )
    else:
        account = BankAccount(name)

        result_label.config(
            text=f"Account created for {name}"
        )

        save_account()

def deposit_money():
    global account

    if account is None:
        messagebox.showwarning(
            "Warning",
            "Create account first"
        )
        return

    try:
        amount = float(amount_entry.get())

        account.deposit(amount)

        result_label.config(
            text=f"Deposited ₹{amount}\nBalance: ₹{account.balance}"
        )

        save_account()

    except ValueError:
        messagebox.showwarning(
            "Warning",
            "Enter valid amount"
        )

def withdraw_money():
    global account

    if account is None:
        messagebox.showwarning(
            "Warning",
            "Create account first"
        )
        return

    try:
        amount = float(amount_entry.get())

        if account.withdraw(amount):
            result_label.config(
                text=f"Withdrawn ₹{amount}\nBalance: ₹{account.balance}"
            )
            save_account()

        else:
            messagebox.showwarning(
                "Warning",
                "Insufficient Balance"
            )

    except ValueError:
        messagebox.showwarning(
            "Warning",
            "Enter valid amount"
        )

def check_balance():
    if account:
        result_label.config(
            text=f"{account.name}'s Balance: ₹{account.balance}"
        )
    else:
        messagebox.showwarning(
            "Warning",
            "Create account first"
        )

# ---------------- WIDGETS ----------------

tk.Label(
    window,
    text="Customer Name",
    bg="#EAF4FF",
    activebackground="#2E7D32",
    font=("Arial", 10, "bold")
).pack(pady=5)

name_entry = tk.Entry(window, width=30)
name_entry.pack()

tk.Label(
    window,
    text="Amount",
    bg="#EAF4FF",activebackground="#2E7D32",
    font=("Arial", 10, "bold")
).pack(pady=5)

amount_entry = tk.Entry(window, width=30)
amount_entry.pack()

create_button = tk.Button(
    window,
    text="Create Account",
    command=create_account,
    bg="#4CAF50",
    fg="white",activebackground="#2E7D32",
    width=20
)
create_button.pack(pady=5)

deposit_button = tk.Button(
    window,
    text="Deposit",
    command=deposit_money,
    bg="#2196F3",
    fg="white",activebackground="#2E7D32",
    width=20
)
deposit_button.pack(pady=5)

withdraw_button = tk.Button(
    window,
    text="Withdraw",
    command=withdraw_money,
    bg="#F44336",
    fg="white",activebackground="#2E7D32",
    width=20
)
withdraw_button.pack(pady=5)

balance_button = tk.Button(
    window,
    text="Check Balance",
    command=check_balance,
    bg="#FF9800",
    fg="white",activebackground="#2E7D32",
    width=20
)
balance_button.pack(pady=5)
def clear_data():
    global account

    account = None

    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

    result_label.config(text="No Account Created")

    with open(FILE_NAME, "w") as file:
        file.write("")
result_label = tk.Label(
    window,
    text="No Account Created",
    bg="#EAF4FF",
    fg="#0D47A1",activebackground="#2E7D32",
    font=("Arial", 12, "bold")
)
clear_button = tk.Button(
    window,
    text="Clear Account",
    command=clear_data,
    bg="#9E9E9E",
    fg="white",
    width=20
)

clear_button.pack(pady=5)
result_label.pack(pady=20)

load_account()

window.mainloop()
