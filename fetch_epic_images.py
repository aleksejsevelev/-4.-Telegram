import os
import argparse
import requests
import global_functions


def main():
    apikey = global_functions.get_nasa_apikey()
    os.makedirs('images', exist_ok=True)
    parser = argparse.ArgumentParser(description='Скачивает фотографии с сервиса NASA EPIC')
    parser.add_argument('count', type=int, help='Позволяет выбрать количество скачиваемых фотографий')
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
        url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image_name}.png'
        global_functions.save_photo(f'images/{image_name}.png', url, params)


if __name__ == '__main__':
    main()
