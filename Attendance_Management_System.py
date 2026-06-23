import tkinter as tk

window = tk.Tk()
window.title("Attendance Management System")
window.geometry("500x500")
window.config(bg="#EAF4FF")
FILE_NAME ="attendance.txt"
title = tk.Label(
    window,
    text="Attendance Management System",
    font=("Arial", 16, "bold"),
    bg="#EAF4FF"
)
title.pack(pady=10)

tk.Label(
    window,
    text="Student Name",
    font=("Arial", 11, "bold"),
    bg="#EAF4FF"
).pack()

student_entry = tk.Entry(
    window,
    width=30
)
student_entry.pack(pady=5)

attendance_listbox = tk.Listbox(
    window,
    width=40,
    height=12
)
attendance_listbox.pack(pady=20)

def mark_present():
    student = student_entry.get()
    if student!="":
        attendance_listbox.insert(tk.END,f"{student}- present")
        
   
        student_entry.delete(0,tk.END)
def mark_absent():
    student = student_entry.get()

    if student != "":
        attendance_listbox.insert(
            tk.END,
            f"{student} - Absent"
        )

        student_entry.delete(
            0,
            tk.END
        )
def save_attendance():
    with open("attendance.txt", "w") as file:

        for i in range(attendance_listbox.size()):

            record = attendance_listbox.get(i)

            file.write(record + "\n")
def load_attendance():
    try:
        with open(FILE_NAME, "r") as file:

            for line in file:
                attendance_listbox.insert(
                    tk.END,
                    line.strip()
                )

    except FileNotFoundError:
        pass
def clear_attendance():
    attendance_listbox.delete(0, tk.END)
clear_button = tk.Button(
    window,
    text="Clear All",
    command=clear_attendance,
    bg="#FF9800",
    fg="white",
    width=20
)

clear_button.pack(pady=5)
absent_button = tk.Button(
    window,
    text="Mark Absent",
    command=mark_absent,
    bg="#F44336",
    fg="white",
    width=20
)

absent_button.pack(pady=5)
present_button = tk.Button(
    window,
    text="Mark Present",
    command=mark_present,
    bg="#4CAF50",
    fg="white",
    width=20
)

present_button.pack(pady=5)
save_button = tk.Button(
    window,
    text="Save Attendance",
    command=save_attendance,
    bg="#2196F3",
    fg="white",
    width=20
)

save_button.pack(pady=5)
load_attendance()
window.mainloop()
