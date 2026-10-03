# Weather App

A beginner-level Python Weather App that fetches real-time weather information using the OpenWeather API.

## Features

- Accepts city name or ZIP code
- Fetches current weather data
- Displays temperature in celsius
- Displays temperature in Fahrenheit
- Displays humidity
- Displays weather condition
- Displays wind speed
- Handles empty location input
- Handles invalid API keys
- Handles city not found errors
- Handles network timeout errors

## Technologies Used

- Python
- Requests
- JSON
- OpenWeather API

## API Key Setup

The application uses the `OPENWEATHER_API_KEY` environment variable.

Set your API Key before running the application.

Example:

```powershell
$env:OPENWAETHER_API_KEY="YOUR_API_KEY"

## How to Run

Install the required package
pip install -r requirements.txt

# Run the application

python weather_app.py
