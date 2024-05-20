import requests
from bs4 import BeautifulSoup

users: list[dict] = [
    {'name': 'Jakub', 'surname': 'Orłowski', 'posts': 13},
    {'name': 'Janek', 'surname': 'Mielec', 'posts': 20},
    {'name': 'Maciej', 'surname': 'Przybytek', 'posts': 45},
    {'name': 'Bartosz', 'surname': 'Pietrasik', 'posts': 60},
    {'name': 'Tymoteusz', 'surname': 'Miszczak', 'posts': 21},
    {'name': 'Mateusz', 'surname': 'Matysiak', 'posts': 33},
    {'name': 'Paweł', 'surname': 'Paszkowski', 'posts': 9},
]

miasto=input("Podaj nazwę miejscowości ")
def get_coords(miasto:str) ->list:
    adres_url=f"https://pl.wikipedia.org/wiki/{miasto}"
    respounce = requests.get(adres_url)
    respounce_html=BeautifulSoup(respounce.text,'html.parser')
    # print(respounce_html)
    latitude=float(respounce_html.select(".latitude")[1].text.replace(",","."))
    longitude=float(respounce_html.select(".longitude")[1].text.replace(",","."))
    print([latitude,longitude])
    return latitude,longitude
get_coords(miasto)
