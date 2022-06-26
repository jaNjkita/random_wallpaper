import os

from GUI_logic import *


try:
    os.mkdir(r'C:\обои')
except FileExistsError:
    pass
        




################################################################       Графический интерфейс       ####################################################################


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
