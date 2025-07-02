import telegram
import os
import argparse
import random
import time
from dotenv import load_dotenv


def main():
    load_dotenv('secret_data.env')
    token = os.getenv('TELEGRAM_TOKEN')
    bot = telegram.Bot(token=token)
    chat_id = '@kakashke12345678'
    parser = argparse.ArgumentParser()
    parser.add_argument('--delay', default=4, type=int)
    args = parser.parse_args()
    delay = args.delay
    while True:
        for i in os.walk('images'):
            images_list = i[2]
        random.shuffle(images_list)
        for image in images_list:
            bot.send_document(chat_id=chat_id, document=open(f'images/{image}', 'rb'))
            time.sleep(delay*3600)


if __name__ == '__main__':
    main()
