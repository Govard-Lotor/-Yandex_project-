import pygame
from player import Player
from loading_screen import Loading
from main_menu import Main_menu
pygame.init()

def nothing():
    pass

main_window = pygame.display.set_mode((1920, 1080))

fps = 60
clock = pygame.time.Clock()
FPS = 0


white = 255, 255, 255
red = 255, 0, 0

loading = Loading()
load_marker = 0     # 0 - нужно отобразить стартовый экран, 1 - до игры, 2 - во время игры

menu = Main_menu(main_window)
menu_marker = 0

keys = pygame.key.get_pressed()


while True:
    FPS += 1

    for event in pygame.event.get():

        if pygame.key.get_pressed()[pygame.K_f]:
            exit()


    pygame.display.flip()
    clock.tick(fps)
    if FPS == 60:
        FPS = 0

#event.type == pygame.QUIT