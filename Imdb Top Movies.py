from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

while True:
    try:
        url = 'https://www.imdb.com/chart/moviemeter'
        web = requests.get(url, headers=headers)
        webpage = BeautifulSoup(web.content, 'html.parser')
        title = webpage.find(class_='seen-collection')
        movie = title.find(class_='lister-list')
        movies = movie.find_all(class_='titleColumn')
        for i in movies[:5]:
            j = i.find('a')
            text = j.text
            print(text)
        print('-------------------------------------------------')
        break
    except:
        continue
