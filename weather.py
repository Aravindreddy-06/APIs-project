import requests

# Replace with your actual API key from OpenWeatherMap
API_KEY = '9bbf42dc5eae32ba85355f3a2e3c5fef'

def fetch_weather_data(location):
    # URL for fetching weather data
    url = f'http://api.openweathermap.org/data/2.5/weather'
    # Parameters for the request
    params = {
        'q': location,  # Location input by user
        'appid': API_KEY,  # Your API key
        'units': 'metric'  # Temperature in Celsius
    }
    # Send GET request to the API
    response = requests.get(url, params=params)
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data (status code: {response.status_code})")
        return None

def display_weather_data(weather_data):
    if weather_data:
        main = weather_data['main']
        weather = weather_data['weather'][0]
        wind = weather_data['wind']
        
        print(f"Location: {weather_data['name']}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Weather: {weather['description'].capitalize()}")
        print(f"Humidity: {main['humidity']}%")
        print(f"Wind Speed: {wind['speed']} m/s")
    else:
        print("No data to display.")

def main():
    location = input("Enter city name or coordinates (lat,lon): ")
    weather_data = fetch_weather_data(location)
    display_weather_data(weather_data)

if __name__ == "__main__":
    main()
