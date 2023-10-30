import requests
from urllib.parse import urlparse,unquote
from downloads import address_and_path


def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384" 
    response=requests.get(url)
    response.raise_for_status()
    links_image = response.json()["links"]["flickr"]["original"]
    for number,link in enumerate(links_image):
        address_and_path(link, f"images/{number}.jpg")


def main():
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()