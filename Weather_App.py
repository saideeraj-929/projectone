import tkinter as tk
import requests

# ---------------- WINDOW ----------------

window = tk.Tk()
window.title("Weather App")
window.geometry("400x350")
window.config(bg="#EAF4FF")

# ---------------- FUNCTIONS ----------------

def get_weather():
    city = city_entry.get()

    if city == "":
        result_label.config(
            text="Please enter a city name"
        )
        return

    try:
        url = f"https://wttr.in/{city}?format=3"

        response = requests.get(url)

        result_label.config(
            text=response.text
        )

    except:
        result_label.config(
            text="Unable to get weather data"
        )

def clear_data():
    city_entry.delete(0, tk.END)

    result_label.config(
        text="Weather Information"
    )

# ---------------- WIDGETS ----------------

title_label = tk.Label(
    window,
    text="🌦️ Weather App",
    bg="#EAF4FF",
    font=("Arial", 16, "bold")
)
title_label.pack(pady=10)

tk.Label(
    window,
    text="Enter City",
    bg="#EAF4FF",
    font=("Arial", 12, "bold")
).pack(pady=5)

city_entry = tk.Entry(
    window,
    width=30,
    font=("Arial", 11)
)
city_entry.pack()

get_button = tk.Button(
    window,
    text="Get Weather",
    command=get_weather,
    bg="#2196F3",
    fg="white",
    width=20
)
get_button.pack(pady=10)

clear_button = tk.Button(
    window,
    text="Clear",
    command=clear_data,
    bg="#F44336",
    fg="white",
    width=20
)
clear_button.pack(pady=5)

result_label = tk.Label(
    window,
    text="Weather Information",
    bg="#EAF4FF",
    fg="#0D47A1",
    font=("Arial", 12, "bold"),
    wraplength=300
)
result_label.pack(pady=20)

window.mainloop()
