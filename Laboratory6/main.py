#Імпортуємо бібліотеку requests

import requests

r = requests.get("https://tsn.ua/")

#Імпортуємо BS

from bs4 import BeautifulSoup

#Рахуємо к-сть зображень на сайті

def get_img_cnt(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content)
    return len(soup.find_all('img'))

#Рахуємо к-сть посилань

def get_href_cnt(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content)

    return len(soup.find_all('a'))


#Рахуємо к-сть html тегів

def get_html_tegs_cnt(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content)

    return len(soup.find_all('html'))


print ("Кількість HTML тегів на сайті: " +str(get_html_tegs_cnt('http://www.tsn.ua/')))

print ("Кількість посилань на сайті: " +str(get_href_cnt('http://www.tsn.ua/')))

print ("Кількість зображень на сайті: " +str(get_img_cnt('http://www.tsn.ua/')))








