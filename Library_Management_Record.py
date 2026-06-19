import tkinter as tk
from tkinter import messagebox

window=tk.Tk()
window.title("Library Management System")
window.geometry("500x500")
window.config(bg="#EAF4FF")
FILE_NAME ="books.txt"

tk.Label(window,text="Book Name",bg="#EAF4FF",font=("Arial",10,"bold")).pack(pady=5)
book_entry =tk.Entry(window,width=35)
book_entry.pack(pady=5)
book_listbox=tk.Listbox(window,width=40,height=12,font=("Arial",10))
book_listbox.pack(pady=20)
def save_books():
    
        with open("books.txt","w")as file:
            for i in range(book_listbox.size()):
                book = book_listbox.get(i)
                file.write(book+"\n")
        messagebox.showinfo(
        "Saved",
        "Books saved successfully"
    )
def add_book():
    book =book_entry.get()
    if book=="":
        messagebox.showwarning("Warning","Entre a book name")
    else:
        book_listbox.insert(tk.END,f"Available-{book}")
        book_entry.delete(0,tk.END)
        save_books()
        
def load_books():
    try:
        with open(FILE_NAME, "r") as file:

            for line in file:
                book_listbox.insert(
                    tk.END,
                    line.strip()
                )

    except FileNotFoundError:
        pass
def issue_book():
    selected = book_listbox.curselection()

    if selected:
        index = selected[0]

        book = book_listbox.get(index)

        if "Available" in book:
            book_listbox.delete(index)

            new_book = book.replace(
                "Available",
                "Issued"
            )

            book_listbox.insert(
                index,
                new_book
            )
            save_books()
            
def return_book():
    selected = book_listbox.curselection()
    if selected:
        index = selected[0]
        book=book_listbox.get(index)
        if "Issued" in book:
            book_listbox.delete(index)
            new_book=book.replace("Issued","Available")
            book_listbox.insert(index,new_book)
            save_books()
return_button = tk.Button(
    window,
    text="Return Book",
    command=return_book,
    bg="#2196F3",
    fg="white",
    width=20
)

return_button.pack(pady=5)
issue_button = tk.Button(
    window,
    text="Issue Book",
    command=issue_book,
    bg="#F44336",
    fg="white",
    width=20
)

issue_button.pack(pady=5)
save_button = tk.Button(
    window,
    text="Save Books",
    command=save_books,
    bg="#FF9800",
    fg="white",
    width=20
)

save_button.pack(pady=5)
add_button=tk.Button(window,text="Add Book",command=add_book,bg="#4CAF50",fg="white",width=20)
add_button.pack(pady=5)
load_books()
window.mainloop()
