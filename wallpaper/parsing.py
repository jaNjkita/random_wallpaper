import random as rd
import ctypes
import requests

from bs4 import BeautifulSoup



def clear_(lst):
    for i in range(lst.count('\n')):
        lst.remove('\n')


def inside_text(lst):
    '''
    Данная функция принимает список тегов и возвращает его содержимое
    inside_text(list) -> list,
    element of list is text which is inside tag
    '''
    return list(map(lambda tag: tag.text, lst))



def get_href(lst):
    '''
    Данная функция принимает список тегов a и возвращает ссылки,
    которые находятся внутри тегов
    '''
    return list(map(lambda tag: tag['href'], lst))



def interface(i):
    return i + 1


def change(number, web_menu):
    '''Данная функция принимает номер темы и выбирает соответствующую ссылку
    и возвращает html-разметку страницы по данной теме'''
    hrefs = get_href(web_menu)
    href = hrefs[number-1]
    soup = BeautifulSoup(requests.get(href).text, 'lxml')
    return soup



def get_href_to_image(soup):
    lst_div = soup.find_all('div', class_ = 'wallpapers__item')
    return rd.choice(lst_div).div.a['href']


def get_image(href, lst_src):
    soup = BeautifulSoup(requests.get(href).text, 'lxml')
    src = soup.find('img', class_ = 'wallpaper__item__fon__img')['src']
    lst_src.append(src)
    return src


def save_img(src):
    with open('C:\обои\image.jpg', 'wb') as f:
        f.write(requests.get(src).content)
        f.close()


def make_wallpapper():
    path = r'C:\обои\image.jpg'
    ctypes.windll.user32.SystemParametersInfoW(20,0,path,0)



# Получение HTML документа главной страницы
url = 'https://www.goodfon.ru/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

web_menu = soup.find('div', class_ = 'head_menu').contents
clear_(web_menu)


lst_src = [] # список ссылок
