# ==============================
# Student Management System
# ==============================

def add_student():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    branch = input("Enter Branch: ")

    with open("students.txt", "a") as file:
        file.write(f"{name},{roll},{branch}\n")

    print("\nStudent Added Successfully!\n")


def view_students():
    try:
        with open("students.txt", "r") as file:
            records = file.readlines()

            if len(records) == 0:
                print("\nNo Student Records Found!\n")
                return

            print("\n===== Student Records =====")

            for record in records:
                name, roll, branch = record.strip().split(",")

                print(f"Name   : {name}")
                print(f"Roll No: {roll}")
                print(f"Branch : {branch}")
                print("--------------------------")

    except FileNotFoundError:
        print("\nNo student file found!\n")


def search_student():
    search_roll = input("Enter Roll Number to Search: ")

    try:
        with open("students.txt", "r") as file:
            found = False

            for record in file:
                name, roll, branch = record.strip().split(",")

                if roll == search_roll:
                    print("\n===== Student Found =====")
                    print(f"Name   : {name}")
                    print(f"Roll No: {roll}")
                    print(f"Branch : {branch}")
                    print("--------------------------")

                    found = True
                    break

            if not found:
                print("\nStudent Not Found!\n")

    except FileNotFoundError:
        print("\nNo student file found!\n")


def delete_student():
    delete_roll = input("Enter Roll Number to Delete: ")

    try:
        with open("students.txt", "r") as file:
            records = file.readlines()

        found = False

        with open("students.txt", "w") as file:
            for record in records:
                name, roll, branch = record.strip().split(",")

                if roll != delete_roll:
                    file.write(record)
                else:
                    found = True

        if found:
            print("\nStudent Deleted Successfully!\n")
        else:
            print("\nStudent Not Found!\n")

    except FileNotFoundError:
        print("\nNo student file found!\n")


# ==============================
# Main Program
# ==============================

while True:

    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("\nProgram Closed.")
        break

    else:
        print("\nInvalid Choice! Try Again.\n")