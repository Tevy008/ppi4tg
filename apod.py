import requests
import os
import argparse
from urllib.parse import urlparse,unquote
from downloads import address_and_path
from dotenv import load_dotenv


def get_extension_link(link):
    link_unquote = unquote(link)
    link_parse = urlparse(link_unquote)
    path,full_name = os.path.split(link_parse.path)
    file_extension = os.path.splitext(full_name)
    file_name,extension = file_extension
    return extension,file_name


def get_image_apport():
    token = os.environ['TOKEN']
    url_token = "https://api.nasa.gov/planetary/apod"
    count = 30
    params = {"api_key":token,"count":count}
    response=requests.get(url_token,params=params)
    response.raise_for_status()
    for image_apod in response.json():
        if image_apod.get("hdurl"):
            apod_link_image=image_apod["hdurl"]
        else:
            apod_link_image=image_apod["url"]
        print(apod_link_image)
        extension,file_name=get_extension_link(apod_link_image)
        file_path = f"images/{file_name}{extension}"
        address_and_path(apod_link_image,file_path)


def main():
    load_dotenv()
    get_image_apport()


if __name__ == '__main__':    
    main()