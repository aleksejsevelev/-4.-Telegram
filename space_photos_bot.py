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
    chat_id = os.getenv('TG_CHAT_ID')
    parser = argparse.ArgumentParser(description='Запускает Telegram-бота публикующего фотографии космоса в канал')
    parser.add_argument('--delay', default=4, type=int, help='Добавляет кастомное значение задержки между публикацией фотографий(по умолчанию - 4 часа)')
    args = parser.parse_args()
    delay = args.delay
    images = os.listdir('images/')
    while True:
        random.shuffle(images)
        for image in images:
            with open(f'images/{image}', 'rb') as picture:
                bot.send_document(chat_id=chat_id, document=picture)
            time.sleep(delay*3600)


if __name__ == '__main__':
    main()
