def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "❌ Cannot divide by zero"

while True:
    print("\n--- Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "5":
        print("Exiting calculator... Goodbye 👋")
        break

    if choice in ["1", "2", "3", "4"]:
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid input, please enter numbers only")
            continue

        if choice == "1":
            print("Result:", add(x, y))
        elif choice == "2":
            print("Result:", sub(x, y))
        elif choice == "3":
            print("Result:", mul(x, y))
        elif choice == "4":
            print("Result:", div(x, y))
    else:
        print("Invalid choice, try again.")
