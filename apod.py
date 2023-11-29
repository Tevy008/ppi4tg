import requests
import os
import argparse
from urllib.parse import urlparse,unquote
from downloads import download_images
from dotenv import load_dotenv
from pathlib import Path


def get_extension_link(url):
    link_unquote = unquote(url)
    link_parse = urlparse(link_unquote)
    path,full_name = os.path.split(link_parse.path)
    file_extension = os.path.splitext(full_name)
    file_name,extension = file_extension
    return extension,file_name


def get_image_apport(token):
    apod_url = "https://api.nasa.gov/planetary/apod"
    images_of_number = 30
    params = {"api_key":token,"count":number_of_images}
    response=requests.get(apod_url,params=params)
    response.raise_for_status()
    for image_apod in response.json():
        if image_apod.get("hdurl"):
            apod_link_image=image_apod["hdurl"]
        else:
            apod_link_image=image_apod["url"]
        extension,file_name=get_extension_link(apod_link_image)
        file_path = f"images/{file_name}{extension}"
        download_images(apod_link_image,file_path)


def main():
    token = os.environ['NASA_TOKEN']
    Path("images").mkdir(parents=True, exist_ok=True)
    load_dotenv()
    get_image_apport(token)


if __name__ == '__main__':
    main()
