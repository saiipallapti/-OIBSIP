import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        weather_desc = data['weather'][0]['description']

        print(f"\nWeather in {city.capitalize()}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_desc.capitalize()}")
    elif response.status_code == 404:
        print(f"\nError: City '{city}' not found. Please check the spelling.")
    else:
        print(f"\nError: Failed to retrieve weather data (Code: {response.status_code}).")

def main():
    print("=== Weather App ===")
    city = input("Enter city name: ").strip()
    api_key = "1884859e7b5c321df7d77f7b99ac298b"  # Your actual API key

    if city:
        get_weather(city, api_key)
    else:
        print("City name cannot be empty.")

if __name__ == "__main__":
    main()
