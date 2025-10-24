from openweather import OpenWeatherClient
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_KEY")
if not API_KEY:
    raise SystemExit("Set OpenWeatherAPI key in .env")

c = OpenWeatherClient(api_key=API_KEY)

cw = c.get_current_weather(city='Pune', as_model=True)
print(f"{cw.name}: {cw.main.temp} °C, {cw.weather[0].description}")

fc = c.get_forecast(city="Pune")
print(fc["city"]["name"], "points:", len(fc["list"]))