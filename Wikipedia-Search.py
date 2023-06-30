from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

while True:
    i = input("What to search for : ")
    url = 'https://en.wikipedia.org/wiki/'+i
    web = requests.get(url, headers=headers)
    webpage = BeautifulSoup(web.content, 'html.parser')
    stuff = webpage.find(class_='mw-page-container').find(class_='mw-content-container')
    data = stuff.find_all('p')
    for i in data:
        if len(i.get_text()) > 10:
            print(i.get_text())
            break
    print('-----------------------------------------')