import telegram
import os
from dotenv import load_dotenv


def main():
    load_dotenv('secret_data.env')
    token = os.getenv('TELEGRAM_TOKEN')
    bot = telegram.Bot(token=token)
    chat_id = '@kakashke12345678'
    bot.send_document(chat_id=chat_id, document=open('test_image.jpg', 'rb'))


if __name__ == '__main__':
    main()
