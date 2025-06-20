import requests
import os
from dotenv import load_dotenv


def save_photo(filepath, url):
    response = requests.get(url)
    response.raise_for_status()
    with open(filepath, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    response = requests.get(url)
    response.raise_for_status()
    for num, url in enumerate(response.json()['links']['flickr']['original']):
        filename = f'images/spacex_{num}.jpg'
        save_photo(filename, url)


def get_nasa_apod(apikey):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'count': 50,
        'api_key': apikey,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    apod_pictures = response.json()
    for apod_picture in apod_pictures:
        apod_url = apod_picture['url']
        filename = os.path.basename(apod_url)
        filepath = os.path.join('images/', filename)
        save_photo(filepath, apod_url)


def get_epic_photo(apikey, count):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': apikey
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    epic_photos = response.json()[:count]
    for photo in epic_photos:
        image_name = photo['image']
        date = photo['date'].split()[0].replace('-', '/')
        url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image_name}.png?api_key={apikey}'
        save_photo(f'images/{image_name}.png', url)


def main():
    load_dotenv('secret_data.env')
    apikey = os.getenv('NASA_API')
    os.makedirs('images', exist_ok=True)
    fetch_spacex_last_launch()
    get_nasa_apod(apikey)
    get_epic_photo(apikey, count=5)


if __name__ == '__main__':
    main()
