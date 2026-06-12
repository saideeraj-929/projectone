# Simple Login System in Python

def register():
    username = input("Enter new username: ")
    password = input("Enter new password: ")
    with open("users.txt", "a") as f:
        f.write(f"{username},{password}\n")
    print("✅ Registration successful!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    found = False

    try:
        with open("users.txt", "r") as f:
            for line in f:
                stored_user, stored_pass = line.strip().split(",")
                if stored_user == username:
                    found = True
                    if stored_pass == password:
                        print("✅ Login successful!")
                    else:
                        print("❌ Wrong password!")
                    break
        if not found:
            print("❌ Username not found!")
    except FileNotFoundError:
        print("⚠️ No users registered yet. Please register first.")

# --- Menu System ---
while True:
    print("\n--- Login System Menu ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Exiting program... Goodbye 👋")
        break
    else:
        print("Invalid choice. Please try again.")
