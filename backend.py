import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')


def get_data(place, forecast_days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    total_values = 8 * forecast_days
    filtered_data = filtered_data[:total_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, type="Sky"))
