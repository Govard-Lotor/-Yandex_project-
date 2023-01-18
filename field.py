import pygame
from player import Player

player = Player(990, 500, 5)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1920, 1080))
im = pygame.image.load('textures/background.jpg')
guide = pygame.image.load('arts/game_ruls.png')
screen.blit(im, (0, 0))


class Field:
    def __init__(self, main_screen):
        self.field = screen
        self.screen = main_screen
        self.field.blit(player.image, player.rect)
        self.pause = 1

    def draw(self):
        for event in pygame.event.get():
            pass

        if pygame.mouse.get_pressed()[2]:
            self.pause = 0

        if not self.pause:
            self.field.blit(guide, (0, 0))

        if pygame.key.get_pressed()[pygame.K_f] and self.pause == 0:
            self.pause = 1

        if self.pause:
            player.update((1920, 1080))
            player.rotate()
            self.screen.blit(im, (0, 0))
            self.field.blit(player.image, player.rect)

        self.screen.blit(self.field, (0, 0))

        pygame.display.flip()
        clock.tick(60)
