import datetime as dt
import os
import requests
from colorama import Fore, Style

API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    with open("api_key") as f:
        API_KEY = f.read().strip()

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather():
    city = input("Write your city: ")
    return city

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = round(celsius * (9/5) + 32, 2)
    return celsius, fahrenheit

CITY = get_weather()

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

try:
    response = requests.get(url).json()
    if response.get("cod") != 200:
        print("City not found. Try again.")
        exit()
except requests.exceptions.RequestException as e:
    print("Error while connecting to API:", e)
    exit()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.fromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.fromtimestamp(response['sys']['sunset'] + response['timezone'])

print(Fore.GREEN + "="*40 + Style.RESET_ALL)
print(Fore.RED + f"Weather report for: "+Fore.GREEN+f"{CITY}" + Style.RESET_ALL)
print(Fore.GREEN + "="*40 + Style.RESET_ALL)
print(Fore.RED + f"Temperature: "+ Fore.GREEN +f"{temp_celsius:.2f}°C "+Fore.RED+"or "+Fore.GREEN+f"{temp_fahrenheit}°F"+ Style.RESET_ALL)
print(Fore.RED +f"Feels like: "+Fore.GREEN+f"{feels_like_celsius:.2f}°C "+Fore.RED+"or "+Fore.GREEN+f"{feels_like_fahrenheit}°F"+Style.RESET_ALL)
print(Fore.RED + f"Humidity: "+Fore.GREEN+f"{humidity}%"+Style.RESET_ALL)
print(Fore.RED+ f"Wind speed: "+Fore.GREEN+f"{wind_speed}m/s"+Style.RESET_ALL)
print(Fore.RED+ f"Condition: "+Fore.GREEN+f"{description.capitalize()}"+Style.RESET_ALL)
print(Fore.RED+ f"Sunrise: "+Fore.GREEN+f"{sunrise_time} "+Fore.RED+ "local time "+Style.RESET_ALL)
print(Fore.RED+ f"Sunset: "+Fore.GREEN+f"{sunset_time} "+Fore.RED+ "local time "+Style.RESET_ALL)
print(Fore.GREEN+"="*40 + Style.RESET_ALL)



