import re

def check_password_strength(password):
    strength = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Character checks
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*(),.?/:{}|<>" for c in password)

    if has_upper:
        strength += 1
    else:
        suggestions.append("Add uppercase letters.")
    if has_lower:
        strength += 1
    else:
        suggestions.append("Add lowercase letters.")
    if has_digit:
        strength += 1
    else:
        suggestions.append("Include numbers.")
    if has_special:
        strength += 1
    else:
        suggestions.append("Include special characters.")

    # Rating
    if strength <= 2:
        rating = "Weak"
    elif strength in (3, 4):
        rating = "Medium"
    else:
        rating = "Strong"

    return rating, suggestions


if __name__ == "__main__":
    user_password = input("Enter a password to check: ")
    rating, tips = check_password_strength(user_password)
    print("Password Strength:", rating)
    if tips:
        print("Suggestions:")
        for tip in tips:
            print("-", tip)
