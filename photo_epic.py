import requests
import datetime
from downloads import address_and_path
import os
from dotenv import load_dotenv


def get_photo_epic():
    token = os.environ['TOKEN']
    url = "https://api.nasa.gov/EPIC/api/natural/image"
    params = {"api_key":token,}
    response=requests.get(url,params=params)
    response.raise_for_status()
    for epic_image in response.json():
        filename = epic_image["image"]
        epic_image_date = epic_image["date"]
        epic_image_date = datetime.datetime.fromisoformat(epic_image_date).strftime('%Y/%m/%d')
        link_path = f"https://api.nasa.gov/EPIC/archive/natural/{epic_image_date}/png/{filename}.png"
        url_path = f"images/{filename}.png"
        address_and_path(link_path,url_path,params)                            


def main():
    load_dotenv()
    get_photo_epic()


if __name__ == '__main__':
    main()