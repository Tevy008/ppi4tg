import requests
import os


def address_and_path(link,path,params=None):
    response = requests.get(link,params)
    response.raise_for_status()
    if not os.path.exists("images"):
        os.mkdir("images")  
    with open(path, 'wb') as file:
        file.write(response.content)