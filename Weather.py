from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

def c_f(c):
    f = (c * 1.8) + 32.0
    return round(f)

while True:
    i = input("What to search for : ")
    url = 'https://www.google.com/search?q=weather+' + i
    web = requests.get(url, headers=headers)
    webpage = BeautifulSoup(web.content, 'html.parser')
    website = webpage.find(class_='eqAnXb')
    temp = website.find(class_='vk_bk TylWce SGNhVe')
    celsius = int(temp.find(class_='wob_t').text)
    faren = c_f(celsius)
    val = website.find(class_='wtsRwe')
    precipitation = val.find(id='wob_pp').text
    humidity = val.find(id='wob_hm').text
    wind = val.find(id='wob_ws').text
    weather = website.find(class_='VQF4g')
    date = weather.find(id='wob_dts').text
    w = weather.find(id='wob_dc').text
    print('Weather :', w)
    print("Temp : " + str(celsius) + "°C / " + str(faren) + "°F")
    print("Precipitation :", precipitation)
    print("Humidity :", humidity)
    print("Wind speed :", wind)
    print('Day and Time :', date)
    print('-----------------------------------------')

