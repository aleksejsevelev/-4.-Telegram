import requests
import os
import argparse
from global_functions import save_photo


def main():
    os.makedirs('images', exist_ok=True)
    parser = argparse.ArgumentParser(description='Скачивает фотографии с нужного вам запуска ракеты SpaceX')
    parser.add_argument(
        '--id',
        default='latest',
        help='Позволяет скачать фотографии с конкретного запуска по его ID(по умолчанию скачивает фото с последнего запуска)'
        )
    args = parser.parse_args()
    url = f'https://api.spacexdata.com/v5/launches/{args.id}'
    response = requests.get(url)
    response.raise_for_status()
    params = {}
    for num, url in enumerate(response.json()['links']['flickr']['original']):
        filepath = f'images/spacex_{num}.jpg'
        save_photo(filepath, url, params)


if __name__ == '__main__':
    main()
