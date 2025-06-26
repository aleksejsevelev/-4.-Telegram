import telegram
import os
from dotenv import load_dotenv


def main():
    load_dotenv('secret_data.env')
    token = os.getenv('TELEGRAM_TOKEN')
    bot = telegram.Bot(token=token)
    chat_id = '@kakashke12345678'
    bot.send_message(chat_id=chat_id, text='я насрал')


if __name__ == '__main__':
    main()
