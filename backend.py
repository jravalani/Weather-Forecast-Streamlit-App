import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')


def get_data(place, forecast_days, type):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    total_values = 8 * forecast_days
    filtered_data = filtered_data[:total_values]
    match type:
        case "Temperature":
            filtered_data = [temperatures['main']['temp'] / 10 for temperatures in filtered_data]
        case "Sky":
            filtered_data = [skys['weather'][0]['main'] for skys in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, type="Sky"))
