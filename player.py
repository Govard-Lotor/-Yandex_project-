import pygame
from pygame.math import Vector2
pygame.init()

fps = 60
clock = pygame.time.Clock()

counter = 0

gun_shoot_sound = pygame.mixer.Sound('sounds/оружие/пистолет_выстрел.mp3')
gun_shoot_animation = [pygame.image.load(f'анимация/стрельба/sprite_shoot{i}.png') for i in range(6)]


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.orig = self.image

    def update(self, w_h):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] and self.rect.x + self.speed < w_h[0] - self.rect.w:
            self.rect.x += self.speed

        if keys[pygame.K_a] and self.rect.x - self.speed > 0:
            self.rect.x -= self.speed

        if keys[pygame.K_w] and self.rect.y - self.speed > 0:
            self.rect.y -= self.speed

        if keys[pygame.K_s] and self.rect.y + self.speed < w_h[-1] - self.rect.h:
            self.rect.y += self.speed

    def rotate(self):
        x, y, w, h = self.rect
        direction = pygame.mouse.get_pos() - Vector2(x + w // 2, y + h // 2)
        radius, angel = direction.as_polar()
        self.image = pygame.transform.rotate(self.orig, - angel + 90)
        self.rect = self.image.get_rect(center=self.rect.center)

    def shoot_gun(self, frame):
        self.image = pygame.image.load(frame).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
