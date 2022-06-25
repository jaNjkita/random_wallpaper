import requests
import random as rd
import os
import pygame
import ctypes
from bs4 import BeautifulSoup



try:
    os.mkdir(r'C:\обои')
except FileExistsError:
    pass


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


def change(number):
    '''Данная функция принимает номер темы и выбирает соответствующую ссылку
    и возвращает html-разметку страницы по данной теме'''
    hrefs = get_href(web_menu)
    href = hrefs[number-1]
    soup = BeautifulSoup(requests.get(href).text, 'lxml')
    return soup



def get_href_to_image(soup):
    lst_div = soup.find_all('div', class_ = 'wallpapers__item')
    return rd.choice(lst_div).div.a['href']


def get_image(href):
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


lst_src = []

########################################################################################################################################################################

pygame.init()

# Объявляем необходимые переменные
W = 1000
H = 600
pos_x = 10
pos_y = 10
pos_but_x = 575
pos_but_y = 350
FPS = 60
clock = pygame.time.Clock()
move = False
j = 1
k = 1


# Объявляем поверхности
sc = pygame.display.set_mode((W, H)) # Размеры клиентской области
sc.fill((0, 191, 255))
pygame.display.set_caption("Рандомные обои") # Название приложения
#pygame.display.set_icon(pygame.image.load("icon.jpg"))
menu = inside_text(web_menu) # Присваиваевем переменной список тем для обоев
f = pygame.font.SysFont('arial', 18)
b1 = pygame.font.SysFont('arial', 18)
b2 = pygame.font.SysFont('arial', 18)
b1 = b1.render('Предыдущая', 1, (255,255,255))
b2 = b2.render('Следующая', 1, (255,255,255))
but1 = pygame.Surface((125, 30))
but2 = pygame.Surface((125, 30))



# Объявояем списки поверхностей
lst_pos_menu = []
lst_div = []
lst_rect = []
lst_surf = []
lst_b = [b1, b2]
lst_button = [but1, but2]
lst_button_rect = []



for i in range(len(lst_button)):
        lst_button[i].blit(lst_b[i], (7,5))
        rect = lst_button[i].get_rect(topleft = (pos_but_x, pos_but_y))
        lst_button_rect.append(rect)
        sc.blit(lst_button[i], rect)
        pos_but_x = pos_but_x + 175
        
print(lst_button_rect)

def check():
    for rect in range(len(lst_rect)):
        if lst_rect[rect].collidepoint(pygame.mouse.get_pos()):
            lst_div[rect].fill((176, 226, 255))
            lst_div[rect].blit(lst_surf[rect], (0,0))
            sc.blit(lst_div[rect], lst_rect[rect])
            pygame.display.update()


def delete_src():
    for i in range(len(lst_src) - 1):
        if lst_src[i] in lst_src:
            lst_src.remove(lst_src[i])



def event_mouse1():
    global j
    for i in range(len(lst_rect)):
        if lst_rect[i].collidepoint(pygame.mouse.get_pos()):
            lst_div[i].fill((238, 238, 209))
            sc.blit(lst_div[i], lst_rect[i])
            number = interface(i)
            soup = change(number)
            href = get_href_to_image(soup)
            src = get_image(href)
            save_img(src)
            make_wallpapper()
            pygame.display.update()
            j = len(lst_src)



def event_mouse2():
    global j
    for i in range(len(lst_button)):
        if lst_button_rect[i].collidepoint(pygame.mouse.get_pos()):
            lst_button[i].fill((238, 238, 209))
            sc.blit(lst_button[i], lst_button_rect[i])
            pygame.display.update()
            if i == 0:
                l = len(lst_src)
                if l - j - 1 >= 0:
                    j = j + 1
                else:
                    j = 1
                save_img(lst_src[l - j - 1])
                make_wallpapper()
                print('да')
                
            if i == 1:
                l = len(lst_src)
                if l - j < l:
                    j = j - 1
                else:
                    j = 1
                save_img(lst_src[l - j - 1])
                make_wallpapper()
                print('да')



def fill_surf():
    for i in range(len(menu)):
        lst_div[i].fill((0, 191, 255))
        lst_div[i].blit(lst_surf[i], (0,0))
        sc.blit(lst_div[i], lst_rect[i])
    for i in range(len(lst_button)):
        lst_button[i].fill((0,0,0))
        lst_button[i].blit(lst_b[i], (7,5))
        sc.blit(lst_button[i], lst_button_rect[i])


def move_up():
    global move
    global i
    if move == False:
        i = 0
    lst_div[i].fill((224, 238, 224))
    sc.blit(lst_div[i], lst_rect[i])
    i = i + 1
    move = True


def visual_wallpaper():
    img = pygame.image.load(r'C:\обои\image.jpg')
    img = pygame.transform.scale(img, (450,250))
    sc.blit(img, (500, 50))


for i in range(len(menu)):
    theme = menu[i]
    div = pygame.Surface((200,25))
    rect = div.get_rect(topleft = (pos_x, pos_y))
    div.fill((255,0,0))
    
    pos_y = pos_y + 35
    if i == 16:
        pos_x = pos_x + 225
        pos_y = 10
    lst_div.append(div)
    lst_rect.append(rect)

    surf_text = f.render(f'{theme}', 1, (0,0,0))
    lst_surf.append(surf_text)
    div.blit(surf_text, (0,0))
    sc.blit(div, rect)


while 1:

    fill_surf()
    check()
    visual_wallpaper()

    # Обработчик событий    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_up()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                event_mouse1()
                event_mouse2()
                print(lst_src)

            
    
   

    
    pygame.display.update()
 
    clock.tick(FPS)
