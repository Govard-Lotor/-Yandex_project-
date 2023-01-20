import pygame
from player import Player
from bullet import Bullet

player = Player(990, 500, 5)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1920, 1080))
im = pygame.image.load('textures/background.jpg')
guide = pygame.image.load('arts/game_ruls.png')
pause_im = pygame.image.load('arts/game_pause.png')
screen.blit(im, (0, 0))

bullet = Bullet()

shoot_sound = pygame.mixer.Sound('sounds/guns/shoot.mp3')
reload_sound = pygame.mixer.Sound('sounds/guns/reload.mp3')



class Field:
    def __init__(self, main_screen):
        self.field = screen
        self.screen = main_screen
        self.field.blit(player.image, player.rect)

        self.FPS = 0

        self.pause = 1
        self.stop = 0

        self.shoot = 0
        self.bullets = 7
        self.reload_sound = 1

    def draw(self):
        for event in pygame.event.get():
            pass

        self.FPS += 1

        if not self.pause:
            self.field.blit(pause_im, (0, 0))

        if pygame.mouse.get_pressed()[2]:
            self.pause = 0

        if pygame.key.get_pressed()[pygame.K_f] and self.pause == 0:
            self.pause = 1
        if pygame.key.get_pressed()[pygame.K_e] and self.pause == 0:
            self.stop = 1

        if pygame.mouse.get_pressed()[0] and self.pause == 1 and not self.shoot and self.bullets > 0:
            shoot_sound.play()
            player.shoot(self.FPS)
            bullet.set_coor(pygame.mouse.get_pos(), player.coord())
            self.shoot = 1

            self.bullets -= 1

        if self.shoot and self.pause == 1 and self.bullets > 0:
            self.shoot = bullet.shoot(self.field)

        if self.bullets == 0:
            if self.reload_sound:
                reload_sound.play()
                self.reload_sound = 0
            if player.reload(self.FPS):
                self.bullets = 7
                self.reload_sound = 1

        if self.pause:
            player.update((1920, 1080))
            player.rotate()
            self.screen.blit(im, (0, 0))
            self.field.blit(player.image, player.rect)

        self.screen.blit(self.field, (0, 0))

        if self.FPS == 60:
            self.FPS = 0

        pygame.display.flip()
        clock.tick(60)

    def game_stop(self):
        if self.stop:
            self.stop = 0
            return 1
        else:
            return 0
