import pygame
import random


class Enemies(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('animation/enemies/sprite_00.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.orig = self.image
        x, y, w, h, = self.image.get_rect()
        self.rect.x = random.choice([0, 1920])
        self.rect.y = random.choice([0, 1080])
        self.screen = screen

    def go_to_player(self, player):
        x = player.rect.x - self.rect.x
        y = player.rect.y - self.rect.y
        dist = (x ** 2 + y ** 2) ** 0.5
        speed_x = random.choice([2, 2, 2, 2, -2, -2, 2, 2])
        speed_y = random.choice([2, 2, 2, 2, -2, -2, 2, 2])
        if dist > 10:
            self.rect.x += speed_x
            self.rect.y += speed_y
