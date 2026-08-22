import requests

import os
API_KEY = os.environ.get("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"  # ✅ f added here
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        print(f"\n📍 {name}, {country}")
        print(f"🌡️  Temperature : {temp}°C")
        print(f"🤔 Feels Like  : {feels_like}°C")
        print(f"💧 Humidity    : {humidity}%")
        print(f"🌤️  Weather     : {description}")
    else:
        print("City not found! Please check the name.")

def main():
    while True:
        city = input("\nEnter city name (or 'quit' to exit): ")
        if city.lower() == "quit":
            print("Goodbye!")
            break
        get_weather(city)

main()