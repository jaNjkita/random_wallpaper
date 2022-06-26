import pygame
from parsing import *


pygame.init()

# Объявляем необходимые переменные
W = 1000
H = 600
pos_x = 10
pos_y = 10
pos_but_x = 575
pos_but_y = 350
FPS = 30
clock = pygame.time.Clock()
j = 1


# Объявляем поверхности

sc = pygame.display.set_mode((W, H)) # Размеры клиентской области
sc.fill((0, 191, 255))
pygame.display.set_caption("Рандомные обои") # Название приложения
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



def event_mouse1(): # Отвечает за выбор темы для обоев
    global j
    for i in range(len(lst_rect)):
        if lst_rect[i].collidepoint(pygame.mouse.get_pos()):
            lst_div[i].fill((238, 238, 209))
            sc.blit(lst_div[i], lst_rect[i])
            number = interface(i)
            soup = change(number, web_menu)
            href = get_href_to_image(soup)
            src = get_image(href, lst_src)
            save_img(src)
            make_wallpapper()
            pygame.display.update()
            j = len(lst_src)



def event_mouse2(): # Отвечает за нажатие на кнопки
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
