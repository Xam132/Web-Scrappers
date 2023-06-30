from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

while True:
    i = input("What to search for : ")
    url = 'https://www.google.com/search?q=random+fact'
    web = requests.get(url, headers=headers)
    webpage = BeautifulSoup(web.content, 'html.parser')
    website = webpage.find(class_='dG2XIf Wnoohf OJXvsb')
    ques = website.find(class_='sW6dbe').text.strip()
    ans = website.find(class_='EikfZ').text.strip()
    print(ques)
    print(ans)

    print('-----------------------------------------')