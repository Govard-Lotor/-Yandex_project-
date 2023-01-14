import pygame
pygame.init()
fps = 60
FPS = 0
clock = pygame.time.Clock()

black = (0, 0, 0)
green = (53, 161, 31)


class Main_menu:
    def __init__(self, screen):
        self.screen = screen
        self.on_menu_marker = 1

    def on_menu(self):
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        self.field = pygame.Surface((self.width, self.height))
        self.field.fill(black)

        button_one = [self.width // 4, self.height // 15, 100, 100]
        button_two = [self.width // 4, self.height // 15, 100, 600]

        x1, y1 = button_one[2], button_one[3]
        w1, h1 = button_one[0], button_one[1]

        x2, y2 = button_two[2], button_two[3] + 200
        w2, h2 = button_two[0], button_two[1]

        font = pygame.font.Font(None, 30)

        for event in pygame.event.get():
            while self.on_menu_marker:
                    text1 = font.render('Приступить к операции', True, green)
                    text2 = font.render('завершить работу', True, green)

                    self.field.blit(text1, (x1 + 10, y1 + 15))
                    self.field.blit(text2, (x2 + 10, y2 + 15))

                    pygame.draw.rect(self.field, green, (x1, y1, w1, h1), 6)
                    pygame.draw.rect(self.field, green, (x2, y2, w2, h2), 6)

                    self.screen.blit(self.field, (0, 0))

                    pygame.display.flip()
                    clock.tick(fps)

                    if event.type == pygame.KEYDOWN:
                        self.on_menu_marker = 0
                        exit()




