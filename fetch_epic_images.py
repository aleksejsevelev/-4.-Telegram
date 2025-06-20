import os
import argparse
import requests
from global_functions import get_nasa_apikey, save_photo


def main():
    apikey = get_nasa_apikey()
    os.makedirs('images', exist_ok=True)
    parser = argparse.ArgumentParser()
    parser.add_argument('count')
    args = parser.parse_args()
    count = int(args.count)
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


if __name__ == '__main__':
    main()
