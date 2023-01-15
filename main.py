import pygame
from player import Player
from loading_screen import Loading
from main_menu import Menu
pygame.init()


main_window = pygame.display.set_mode((1920, 1080))

fps = 60
clock = pygame.time.Clock()
FPS = 0


white = 255, 255, 255
red = 255, 0, 0

loading = Loading()
load_marker = 0     # 0-загрузка  1-текст  2-старт 3-stop

menu = Menu(main_window)
menu_marker = 0     # 1-отобразить меню  2-ожидать действий

keys = pygame.key.get_pressed()


while True:
    if load_marker == 0:
        load_marker = loading.one_step(main_window)

    if load_marker == 1:
        load_marker = loading.second_step(main_window)

    if load_marker == 3:
        for event in pygame.event.get():
            if pygame.key.get_pressed()[pygame.K_f]:
                menu_marker = 1

    if menu_marker:
        menu.on_menu()




    pygame.display.flip()
    clock.tick(fps)


#event.type == pygame.QUIT