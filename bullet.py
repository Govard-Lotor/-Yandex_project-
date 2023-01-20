import pygame
from player import Player
pygame.init()

fps = 60
clock = pygame.time.Clock()


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        self.speed = 10
        self.k = 0
        self.x1 = 0
        self.y1 = 0

    def set_coor(self, coor, rect):
        self.x1, self.y1 = coor[0], coor[1]
        self.x, self.y = rect

    def shoot(self, screen):
        v_x = self.x1 - self.x
        v_y = self.y1 - self.y
        x2 = int(0.1 * v_x * self.k) + self.x
        y2 = int(0.1 * v_y * self.k) + self.y
        pygame.draw.rect(screen, (255, 255, 0), (x2, y2, 8, 8))
        self.k += 5

        clock.tick(60)
        pygame.display.update()

        if self.k == 100:
            self.k = 0
            return 0
        else:
            return 1
