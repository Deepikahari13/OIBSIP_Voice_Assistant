import os
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

print("=== Weather App ===")

location = input("Enter city name or ZIP code:").strip()

if not location:
    print("Error:Location cannot be empty.")

elif not API_KEY:
    print("Error:OpenWeather API key is not set.")
    print("Please set OPENWEATHER_API_KEY and try again.")

else:
    # Support city name or ZIP code with country code
    if "," in location and location.split(",")[0].strip().isdigit():
        params = {
            "Zip":location,
            "appid":API_KEY,
            "units":"metric"
            }
    else:
        params = {
            "q":location,
            "appid":API_KEY,
            "units":"metric"
        }

    try:
        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )

        if response.status_code == 401:
            print("Error:Invalid or inactive API key.")

        elif response.status_code == 404:
            print("Error:City or ZIP code not found.")

        else:
            response.raise_for_status()

            data = response.json()

            temperature_c = data["main"]["temp"]
            temperature_f = (temperature_c*9/5)+32
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"].title()
            wind_speed = data["wind"]["speed"]

            print("\n=== Current Weather ===")
            print("Location:",data["name"])
            print(f"Temperature:{temperature_c:.1f}C")
            print(f"Temperature:{temperature_f:.1f}F")
            print(f"Humidity:{humidity}%")
            print("Condition:",condition)
            print(f"Wind Speed:{wind_speed} m/s")

    except requests.exceptions.Timeout:
        print("Error:Network request timed out.")

    except requests.exceptions.RequestException:
        print("Error:Could not retrieve weather data.")

    except (KeyError,ValueError):
        print("Error:Invalid weather data received.")

