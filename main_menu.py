import pygame

choice = pygame.mixer.Sound('sounds/interface/choice.mp3')

pygame.init()
fps = 60
FPS = 0
clock = pygame.time.Clock()

black = (0, 0, 0)
green = (53, 161, 31)


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.sound_marker = 1

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

        text1 = font.render('Приступить к операции', True, green)
        text2 = font.render('завершить работу', True, green)

        self.field.blit(text1, (x1 + 10, y1 + 15))
        self.field.blit(text2, (x2 + 10, y2 + 15))

        pygame.draw.rect(self.field, green, (x1, y1, w1, h1), 6)
        pygame.draw.rect(self.field, green, (x2, y2, w2, h2), 6)

        self.screen.blit(self.field, (0, 0))
        pygame.display.flip()

    def check_menu(self):
        button_one = [1920 // 4, 1080 // 15, 100, 100]
        button_two = [1920 // 4, 1800 // 15, 100, 600]

        x1, y1 = button_one[2], button_one[3]
        w1, h1 = button_one[0], button_one[1]

        x2, y2 = button_two[2], button_two[3] + 200
        w2, h2 = button_two[0], button_two[1]

        x, y = pygame.mouse.get_pos()

        if x1 < x < x1 + w1 and y1 < y < y1 + h1:
            if self.sound_marker:
                choice.play()
                self.sound_marker = 0
            return 1.1

        if x2 < x < x2 + w2 and y2 < y < y2 + h2:
            if self.sound_marker:
                choice.play()
                self.sound_marker = 0
            return 2.1
        else:
            self.sound_marker = 1

    def exit(self):
        button_two = [self.width // 4, self.height // 15, 100, 600]

        x2, y2 = button_two[2], button_two[3] + 200
        w2, h2 = button_two[0], button_two[1]

        x, y = pygame.mouse.get_pos()
        if x2 < x < x2 + w2 and y2 < y < y2 + h2:
            return 1

    def start(self):
        button_one = [self.width // 4, self.height // 15, 100, 100]

        x1, y1 = button_one[2], button_one[3]
        w1, h1 = button_one[0], button_one[1]
        x, y = pygame.mouse.get_pos()

        if x1 < x < x1 + w1 and y1 < y < y1 + h1:
            return 1

        # if marker:
        #     pygame.draw.rect(self.screen, green, (x1 - 10, y1 - 10, w1 + 20, h1 + 20), 3)
        #
        # pygame.display.flip()
        # clock.tick(fps)
