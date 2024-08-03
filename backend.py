import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')

def get_data(place):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    content = response.json()
    return content


if __name__ == "__main__":
    print(get_data(place="Tokyo"))
