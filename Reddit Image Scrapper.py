from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import os,time

scroll_pause_time = 1

sub = input("Enter subreddit : ")
i = 1
url = 'https://www.reddit.com/r/' + sub + '/top/?t=month'
web = webdriver.Chrome()
web.get(url)
screen_height = web.execute_script("return window.screen.height;")
scroll_height = max(web.execute_script("return document.body.scrollHeight;"),screen_height*250)
j = 0
prev_height = 0
while True:
    # if scroll-height doesnt change even after 60 sec then we have reached end of scroll so break out of loop
    if i-j >= 60:
        l = web.execute_script("return document.body.scrollHeight;")
        if l == prev_height:
            break
        j = i
        prev_height = l

    # scroll one screen height each time
    web.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    if screen_height * i >= scroll_height:
        break

webpage = BeautifulSoup(web.page_source,'html.parser')

all = webpage.find('body').find_all('img')
l = 0
path = '.\\Reddit\\img\\' + sub
if not os.path.exists(path):
    os.mkdir(path)
for i in all:
    if i.has_attr('alt') and i['alt'] == 'Post image':
        data = requests.get(i['src']).content
        file = open(path+'\\'+str(l)+'.jpg','wb')
        file.write(data)
        file.close()
        l += 1
        print('------------------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------------------')


