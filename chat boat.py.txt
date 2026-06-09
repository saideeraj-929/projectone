import urllib.request
import json
from datetime import datetime

print("==Smart Chat Bot==")
print("Type 'bye' to exit\n")

def get_weather(city):
    api_key = "f14f02dff3e4d9bcca7b8c9187bd0b20"  # your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            print("DEBUG: Raw API response:", data)  # <-- shows exactly what API returned
            
            if data.get("cod") == 200:
                main = data["main"]
                temperature = main["temp"]
                weather_desc = data["weather"][0]["description"]
                return f"Temperature: {temperature}°C\nCondition: {weather_desc}"
            else:
                return f"Error: {data.get('message', 'Unable to fetch weather')}"
    except Exception as e:
        return f"Error fetching weather: {e}"

while True:
    user = input("You: ").lower()
    
    if "hello" in user or "hi" in user:
        print("Bot: Hello, nice to meet you!")
        
    elif "your name" in user:
        print("Bot: My name is Python Chat Bot 🤖")

    elif "time" in user:
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time:", current_time)

    elif "date" in user:
        today = datetime.today().strftime("%Y-%m-%d")
        print("Bot: Today's date:", today)

    elif "2+2" in user:
        print("Bot: 2 + 2 = 4")
    
    elif "5*5" in user:
        print("Bot: 5 * 5 = 25")

    elif "about python" in user:
        print("Bot: Python is one of the best programming languages, easy to learn.")

    elif "about c" in user:
        print("Bot: C is a basic programming language and also very powerful.")

    elif "how are you" in user:
        print("Bot: I am good, thanks for asking ☺")

    elif "help" in user:
        print("Bot: I can help you with C, Python, date, time, maths, and weather.")

    elif "weather" in user:
        city = input("Bot: Please enter city name (e.g., tirupati,in): ")
        print("Bot:", get_weather(city))

    elif "bye" in user:
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't know the answer.")
