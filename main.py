import pygame
from player import Player
from field import Field
from loading_screen import Loading
from main_menu import Menu
pygame.init()

im = pygame.image.load('textures/background.jpg')
guide = pygame.image.load('arts/game_ruls.png')
main_window = pygame.display.set_mode((1920, 1080))

fps = 60
clock = pygame.time.Clock()
FPS = 0


white = 255, 255, 255
red = 255, 0, 0

player = Player(990, 500, 5)

field = Field(main_window)

loading = Loading()
load_marker = 4      # 0-загрузка  1-текст  2-старт 3-stop 4-off

menu = Menu(main_window)
menu_marker = 4     # 1-отобразить меню  2-ожидать действий 3-рисовать 4-стоп

game_start = 0

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

    if menu_marker == 1:
        menu.on_menu()
        menu_marker = 2

    if 4 > menu_marker >= 2:
        if menu.check_menu() == 1.1:
            menu_marker = 3.1
        elif menu.check_menu() == 2.1:
            menu_marker = 3.2
        else:
            menu.on_menu()
            menu_marker = 2
        if menu_marker == 3.1:
            pygame.draw.rect(main_window, (53, 161, 31), (-6, 100 - 10, 2000, 72 + 20), 3)
        if menu_marker == 3.2:
            pygame.draw.rect(main_window, (53, 161, 31), (-6, 800 - 10, 2000, 72 + 20), 3)

        if pygame.mouse.get_pressed()[0]:
            if menu.exit():
                exit()

        if pygame.mouse.get_pressed()[0]:
            if menu.start():
                load_marker = 5
                menu_marker = 4

    if load_marker == 5:
        load_marker = loading.third_step(main_window)

    if load_marker == 4 and menu_marker == 4:
        main_window.blit(guide, (0, 0))
        for event in pygame.event.get():
            if pygame.key.get_pressed()[pygame.K_f]:
                game_start = 1
                load_marker = 6
                menu_marker = 6

    if game_start:
        field.draw()
        if pygame.key.get_pressed()[pygame.K_e]:
            if field.game_stop():
                game_start = 0
                load_marker, menu_marker, game_start = 3, 2, 0


    pygame.display.flip()
    clock.tick(fps)


#event.type == pygame.QUIT