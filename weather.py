import requests

API_KEY = "533eaa9469556092768a6dca773df51f"

city = input("Enter city name: ").strip()


unit = input("Choose unit (C for Celsius / F for Fahrenheit): ").strip().upper()

if unit == "F":
    units = "imperial"
    symbol = "°F"
else:
    units = "metric"
    symbol = "°C"


url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}"

try:
    response = requests.get(url)
    data = response.json()

    if data.get("cod") == 200:
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print("\n Weather Details")
        print("----------------------")
        print(f"City: {city.capitalize()}")
        print(f"Temperature: {temperature}{symbol}")
        print(f"Feels Like: {feels_like}{symbol}")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather.capitalize()}")
        print(f"Wind Speed: {wind_speed} m/s")

    else:
        print("\n Error:", data.get("message"))

except requests.exceptions.RequestException:
    print("\n Network error. Check your internet connection.")