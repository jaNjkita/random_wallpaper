import pygame
from parsing import *


pygame.init()

# Объявляем необходимые переменные
W = 1000
H = 600
pos_x = 10
pos_y = 70
pos_but_x = 575
pos_but_y = 350
FPS = 30
clock = pygame.time.Clock()
j = 1


# Дизайн
colors_1 = {
    'bg_color': (0,191,255),
    'hover': (175,238,238),
    'click': (224,255,255),
    'button_color': (0,0,2),
    'font_button_color': (255,255,255),
    'font_color': (0,0,0),
    'font_menu_color': (255,215,0)
    }


# Объявляем поверхности

sc = pygame.display.set_mode((W, H)) # Размеры клиентской области
font_menu = pygame.font.SysFont('arial', 35)
font_menu.set_italic(1)
font_menu.set_bold(1)
font_menu = font_menu.render('RandomWallpaper', 1, colors_1['font_menu_color'])
rect_menu = font_menu.get_rect(topleft =(20,20))
sc.fill(colors_1['bg_color'])
pygame.display.set_caption("Рандомные обои") # Название приложения
menu = inside_text(web_menu) # Присваиваевем переменной список тем для обоев
f = pygame.font.SysFont('arial', 18)
b1 = pygame.font.SysFont('arial', 18)
b2 = pygame.font.SysFont('arial', 18)
b1 = b1.render('Предыдущая', 1, colors_1['font_button_color'])
b2 = b2.render('Следующая', 1, colors_1['font_button_color'])
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
            lst_div[rect].fill(colors_1['hover'])
            lst_div[rect].blit(lst_surf[rect], (0,0))
            sc.blit(lst_div[rect], lst_rect[rect])
            pygame.display.update()



def event_mouse1(): # Отвечает за выбор темы для обоев
    global j
    for i in range(len(lst_rect)):
        if lst_rect[i].collidepoint(pygame.mouse.get_pos()):
            lst_div[i].fill(colors_1['click'])
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
            lst_button[i].fill(colors_1['click'])
            lst_button[i].fill(colors_1['button_color'])
            sc.blit(lst_button[i], lst_button_rect[i])
            pygame.display.update()
            if i == 0:
                l = len(lst_src)
                if l - j - 1 >= 0:
                    j = j + 1
                else:
                    j = 1
                if l != 0:
                    save_img(lst_src[l - j - 1])
                make_wallpapper()
                
            if i == 1:
                l = len(lst_src)
                if l - j < l:
                    j = j - 1
                else:
                    j = 1
            if l != 0:
                save_img(lst_src[l - j - 1])
            make_wallpapper()


def fill_surf():
    sc.blit(font_menu, rect_menu)
    for i in range(len(menu)):
        lst_div[i].fill(colors_1['bg_color'])
        lst_div[i].blit(lst_surf[i], (0,0))
        sc.blit(lst_div[i], lst_rect[i])
    for i in range(len(lst_button)):
        lst_button[i].fill(colors_1['button_color'])
        lst_button[i].blit(lst_b[i], (7,5))
        sc.blit(lst_button[i], lst_button_rect[i])


def visual_wallpaper():
    img = pygame.image.load(r'C:\обои\image.jpg')
    img = pygame.transform.scale(img, (450,250))
    sc.blit(img, (500, 70))



for i in range(len(menu)):
    theme = menu[i]
    div = pygame.Surface((200,23))
    rect = div.get_rect(topleft = (pos_x, pos_y))
    div.fill((255,0,0))
    
    pos_y = pos_y + 27
    if i == 16:
        pos_x = pos_x + 225
        pos_y = 70
    lst_div.append(div)
    lst_rect.append(rect)

    surf_text = f.render(f'{theme}', 1, colors_1['font_color'])
    lst_surf.append(surf_text)
    div.blit(surf_text, (0,0))
    sc.blit(div, rect)


for i in range(len(lst_button)):
        lst_button[i].blit(lst_b[i], (7,5))
        rect = lst_button[i].get_rect(topleft = (pos_but_x, pos_but_y))
        lst_button_rect.append(rect)
        sc.blit(lst_button[i], rect)
        pos_but_x = pos_but_x + 175
