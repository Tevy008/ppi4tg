import telegram 
import random
from os import listdir
from time import sleep
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    token_tg = os.environ['TOKEN_TG']
    chat_id = os.environ['CHAT_ID']
    bot = telegram.Bot(token=token_tg)
    time = 14400
    while True:
        folder = "images"
        files = listdir(folder)
        random.shuffle(files)
        for file in files:
            filepath = f"{folder}/{file}"
            with open(filepath,"rb") as f:
                bot.send_document(chat_id=chat_id, document=f)
            sleep(time)


if __name__ == '__main__':
    main()
