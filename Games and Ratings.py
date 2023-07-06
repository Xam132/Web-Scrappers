import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

url = 'https://www.imdb.com/search/title/?title_type=video_game&genres=action&explore=genres&ref_=adv_prv'

file = open('./Output/Games.csv','w',encoding='utf8')
write = csv.writer(file)
write.writerow(['name','year','genres','rating'])

def scrape(url,a):
    web = requests.get(url,headers=headers)
    website = BeautifulSoup(web.content,'html.parser').find('body').find(id='wrapper').find(id='main')
    all_link = website.find(class_='desc').find_all('a')
    full_list = website.find_all(class_='lister-item mode-advanced')
    for item in full_list:
        name = item.find(class_='lister-item-content').find('a').text.strip()
        try: year = item.find(class_='lister-item-content').find(class_='lister-item-year text-muted unbold').text.strip()
        except: year = None
        try: genre = item.find(class_='lister-item-content').find(class_='genre').text.strip()
        except: genre = None
        try: rating = item.find(class_='lister-item-content').find(class_='ratings-bar').find('strong').text.strip()
        except: rating = None
        row = [name,year,genre,rating]
        write.writerow(row)
    try:
        nxt_link = all_link[a]['href']
        new_url = urljoin(url,nxt_link)
        print(new_url)
        scrape(new_url,1)
    except:
        return

scrape(url,0)

file.close()

print("Done...")
print('-------------------------------------------------------------')
