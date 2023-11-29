import requests
from urllib.parse import urlparse,unquote
from downloads import download_images
from pathlib import Path
import argparse


def fetch_spacex_last_launch(launch_id):
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}}" 
    response=requests.get(url)
    response.raise_for_status()
    links_image = response.json()["links"]["flickr"]["original"]
    for number,link in enumerate(links_image):
        download_images(link, f"images/{number}.jpg")


def main():
    parser = argparse.ArgumentParser(description='Программа для скачивания фотографий космического телеграма')
    parser.add_argument('--id', dest="launch_id",default="5eb87d42ffd86e000604b384" help='укажите id нужного запуска spacex.py')
    args = parser.parse_args()
    Path("images").mkdir(parents=True, exist_ok=True)
    fetch_spacex_last_launch(args.lauch_id)
    


if __name__ == '__main__':
    main()
