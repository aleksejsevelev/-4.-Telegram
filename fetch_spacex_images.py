import requests
import os
import argparse
from global_functions import save_photo


def main():
    os.makedirs('images', exist_ok=True)
    id = ''
    parser = argparse.ArgumentParser()
    parser.add_argument('id')
    args = parser.parse_args()
    id = args.id
    if id == '':
        id = 'latest'
    url = f'https://api.spacexdata.com/v5/launches/{id}'
    response = requests.get(url)
    response.raise_for_status()
    for num, url in enumerate(response.json()['links']['flickr']['original']):
        filename = f'images/spacex_{num}.jpg'
        save_photo(filename, url)


if __name__ == '__main__':
    main()
