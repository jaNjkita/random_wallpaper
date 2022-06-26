import os

from GUI_logic import *


try:
    os.mkdir(r'C:\обои')
except FileExistsError:
    pass
        




################################################################       Графический интерфейс       ####################################################################



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


for i in range(len(lst_button)):
        lst_button[i].blit(lst_b[i], (7,5))
        rect = lst_button[i].get_rect(topleft = (pos_but_x, pos_but_y))
        lst_button_rect.append(rect)
        sc.blit(lst_button[i], rect)
        pos_but_x = pos_but_x + 175


while True:

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

            

    pygame.display.update()
 
    clock.tick(FPS)
