import pygame
from pygame.math import Vector2
pygame.init()

fps = 60
clock = pygame.time.Clock()

counter = 0

steps_1_sound = pygame.mixer.Sound('sounds/player/steps_1.mp3')
steps_2_sound = pygame.mixer.Sound('sounds/player/steps_2.mp3')


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('textures/player.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.orig = self.image

        self.hp = 100

        self.steps = 0
        self.fr = 1
        self.rf = 0

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

    def coord(self):
        return self.rect.center

    def reload(self, frame):
        if frame % 6 == 0:
            self.image = pygame.image.load(f'animation/gun_reload/sprite_0{self.fr}.png')
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.orig = self.image
            self.fr += 1
            if self.fr == 9:
                self.fr = 1
                self.image = pygame.image.load('textures/player.png')
                self.image = pygame.transform.scale(self.image, (100, 100))
                self.orig = self.image
                return 1
            else:
                return 0

    def shoot(self, frame):
        if frame % 10 == 0:
            self.image = pygame.image.load(f'animation/shooting/sprite_shoot{self.rf}.png')
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.orig = self.image
            self.rf += 1
            if self.rf == 5:
                self.rf = 0
                self.image = pygame.image.load('textures/player.png')
                self.image = pygame.transform.scale(self.image, (100, 100))
                self.orig = self.image
