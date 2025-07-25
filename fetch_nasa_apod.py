import requests
import os
import argparse
import global_functions


def main():
    apikey = global_functions.get_nasa_apikey()
    os.makedirs('images', exist_ok=True)
    url = 'https://api.nasa.gov/planetary/apod'
    parser = argparse.ArgumentParser(description='Скачивает фотографии с сервиса NASA APOD')
    parser.add_argument('count', type=int, help='Позволяет выбрать количество скачиваемых фотографий')
    args = parser.parse_args()
    count = args.count
    params = {
        'count': count,
        'api_key': apikey,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    apod_pictures = response.json()
    params = {}
    for apod_picture in apod_pictures:
        apod_url = apod_picture['url']
        filename = os.path.basename(apod_url)
        filepath = os.path.join('images/', filename)
        global_functions.save_photo(filepath, apod_url, params)


if __name__ == '__main__':
    main()
