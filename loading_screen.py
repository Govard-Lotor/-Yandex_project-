import pygame
pygame.init()
fps = 60
FPS = 0
clock = pygame.time.Clock()

black = (0, 0, 0)
green = (53, 161, 31)

keyboard_sound = pygame.mixer.music.load('sounds/interface/keyboard.mp3')

text_one = list('[Проверка кода доступа]     ')
text_two = list('[успешно]  ')
text_tree = list('[шифрование канала]     ')
text_four = list('[запуск программы "Nemesis"]     ')
text_five = list('[программа готова]    ')
text_six = list('[нажмите "f" чтобы начать сканирование]  ')
text_dop = list('----------      ')

t1_len = len(text_one)
t2_len = len(text_two)
t3_len = len(text_tree)
t4_len = len(text_four)
t5_len = len(text_five)
t6_len = len(text_six)
td_len = len(text_dop)


class Loading:
    def __int__(self):
        pass

    def one_step(self, screen):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()

        self.marker_one = 0

        x0, y0 = self.width // 6, self.height // 4 * 3
        w, h = self.width // 6 * 4, 50
        self.field = pygame.Surface((self.width, self.height))
        self.field.fill(black)
        pygame.draw.rect(self.field, green, (x0, y0, w, h), 6)
        pygame.draw.rect(self.field, green, (x0 + 20, y0 + 10, 25, 30))

        x_x0 = x0 + 20
        y_y0 = y0 + 10
        w_w = 25
        h_h = 30

        FPS = 0

        self.marker = 0
        self.counter = 5

        while self.marker != 23:
            if FPS % self.counter == 0 and self.marker_one == 1:
                x_x0 += 10 + 24
                pygame.draw.rect(self.field, green, (x_x0, y_y0, 25, 30))
                self.marker += 1
            if FPS == 60:
                FPS = 0
                self.marker_one = 1
            if self.marker == 10:
                self.counter = 10
            if self.marker == 20:
                self.counter = 20

            FPS += 1

            pygame.display.flip()
            clock.tick(fps)

            self.screen.blit(self.field, (0, 0))

    def second_step(self, screen):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()

        font = pygame.font.Font(None, 30)
        self.field = pygame.Surface((self.width, self.height))
        self.field.fill(black)

        self.collection = []

        text_x0 = self.width // 15
        text_y0 = self.height // 20

        text_x, text_y = text_x0, text_y0

        self.text = text_one

        self.counter = 0
        self.len = len(self.text) + 1
        FPS = 0

        pygame.mixer.music.play(-1)
        while self.len != 0:

            if FPS % 5 == 0:
                self.field.fill(black)
                stroka = f'{"".join(self.text[0:self.counter])}'
                text = font.render(stroka, True, green)
                self.counter += 1
                self.len -= 1
                self.field.blit(text, (text_x, text_y))
                screen.blit(self.field, (0, 0))

            if FPS == 60:
                FPS = 0
            FPS += 1

            if self.len == 0:
                self.collection.append(stroka)

            if self.len - 5 == 0:
                pygame.mixer.music.stop()

            pygame.display.flip()
            clock.tick(fps)

        text_y += 60

        self.text = text_dop

        self.counter = 0
        self.len = len(self.text) + 1
        FPS = 0

        while self.len != 0:
            self.field.fill(black)
            text_y_dop = text_y0
            for i in self.collection:
                text = font.render(i, True, green)
                self.field.blit(text, (text_x0, text_y_dop))
                text_y_dop += 60

            if FPS % 5 == 0:
                stroka = f'{"".join(self.text[0:self.counter])}'
                text = font.render(stroka, True, green)
                self.counter += 1
                self.len -= 1
                self.field.blit(text, (text_x, text_y))
                screen.blit(self.field, (0, 0))
            if FPS == 60:
                FPS = 0

            if self.len == 0:
                self.collection.append(stroka)

            FPS += 1
            pygame.display.flip()
            clock.tick(fps)

        text_y += 60

        self.text = text_two

        self.counter = 0
        self.len = len(self.text) + 1
        FPS = 0

        pygame.mixer.music.play(-1)
        while self.len != 0:
            self.field.fill(black)
            text_y_dop = text_y0
            for i in self.collection:
                text = font.render(i, True, green)
                self.field.blit(text, (text_x0, text_y_dop))
                text_y_dop += 60

            if FPS % 5 == 0:
                stroka = f'{"".join(self.text[0:self.counter])}'
                text = font.render(stroka, True, green)
                self.counter += 1
                self.len -= 1
                self.field.blit(text, (text_x, text_y))
                screen.blit(self.field, (0, 0))
            if FPS == 60:
                FPS = 0

            if self.len == 0:
                self.collection.append(stroka)

            if self.len - 5 == 0:
                pygame.mixer.music.stop()

            FPS += 1
            pygame.display.flip()
            clock.tick(fps)

        text_y += 60

        self.text = text_tree

        self.counter = 0
        self.len = len(self.text) + 1
        FPS = 0

        pygame.mixer.music.play(-1)
        while self.len != 0:
            self.field.fill(black)
            text_y_dop = text_y0
            for i in self.collection:
                text = font.render(i, True, green)
                self.field.blit(text, (text_x0, text_y_dop))
                text_y_dop += 60

            if FPS % 5 == 0:
                stroka = f'{"".join(self.text[0:self.counter])}'
                text = font.render(stroka, True, green)
                self.counter += 1
                self.len -= 1
                self.field.blit(text, (text_x, text_y))
                screen.blit(self.field, (0, 0))
            if FPS == 60:
                FPS = 0

            if self.len == 0:
                self.collection.append(stroka)

            if self.len - 5 == 0:
                pygame.mixer.music.stop()

            FPS += 1
            pygame.display.flip()
            clock.tick(fps)

        text_y += 60

        self.text = text_dop

        self.counter = 0
        self.len = len(self.text) + 1
        FPS = 0

        while self.len != 0:
            self.field.fill(black)
            text_y_dop = text_y0
            for i in self.collection:
                text = font.render(i, True, green)
                self.field.blit(text, (text_x0, text_y_dop))
                text_y_dop += 60

            if FPS % 5 == 0:
                stroka = f'{"".join(self.text[0:self.counter])}'
                text = font.render(stroka, True, green)
                self.counter += 1
                self.len -= 1
                self.field.blit(text, (text_x, text_y))
                screen.blit(self.field, (0, 0))
            if FPS == 60:
                FPS = 0

            if self.len == 0:
                self.collection.append(stroka)

            FPS += 1
            pygame.display.flip()
            clock.tick(fps)

        text_y += 60

        self.text = text_two

        self.counter = 0
        self.len = len(self.text) + 1
        FPS = 0

        pygame.mixer.music.play(-1)
        while self.len != 0:
            self.field.fill(black)
            text_y_dop = text_y0
            for i in self.collection:
                text = font.render(i, True, green)
                self.field.blit(text, (text_x0, text_y_dop))
                text_y_dop += 60

            if FPS % 5 == 0:
                stroka = f'{"".join(self.text[0:self.counter])}'
                text = font.render(stroka, True, green)
                self.counter += 1
                self.len -= 1
                self.field.blit(text, (text_x, text_y))
                screen.blit(self.field, (0, 0))
            if FPS == 60:
                FPS = 0

            if self.len == 0:
                self.collection.append(stroka)

            if self.len - 5 == 0:
                pygame.mixer.music.stop()

            FPS += 1
            pygame.display.flip()
            clock.tick(fps)

        text_y += 60

        self.text = text_four

        self.counter = 0
        self.len = len(self.text) + 1
        FPS = 0

        pygame.mixer.music.play(-1)
        while self.len != 0:
            self.field.fill(black)
            text_y_dop = text_y0
            for i in self.collection:
                text = font.render(i, True, green)
                self.field.blit(text, (text_x0, text_y_dop))
                text_y_dop += 60

            if FPS % 5 == 0:
                stroka = f'{"".join(self.text[0:self.counter])}'
                text = font.render(stroka, True, green)
                self.counter += 1
                self.len -= 1
                self.field.blit(text, (text_x, text_y))
                screen.blit(self.field, (0, 0))
            if FPS == 60:
                FPS = 0

            if self.len == 0:
                self.collection.append(stroka)

            if self.len - 5 == 0:
                pygame.mixer.music.stop()

            FPS += 1
            pygame.display.flip()
            clock.tick(fps)

        text_y += 60

        self.text = text_dop

        self.counter = 0
        self.len = len(self.text) + 1
        FPS = 0

        while self.len != 0:
            self.field.fill(black)
            text_y_dop = text_y0
            for i in self.collection:
                text = font.render(i, True, green)
                self.field.blit(text, (text_x0, text_y_dop))
                text_y_dop += 60

            if FPS % 5 == 0:
                stroka = f'{"".join(self.text[0:self.counter])}'
                text = font.render(stroka, True, green)
                self.counter += 1
                self.len -= 1
                self.field.blit(text, (text_x, text_y))
                screen.blit(self.field, (0, 0))
            if FPS == 60:
                FPS = 0

            if self.len == 0:
                self.collection.append(stroka)

            FPS += 1
            pygame.display.flip()
            clock.tick(fps)

        text_y += 60

        self.text = text_five

        self.counter = 0
        self.len = len(self.text) + 1
        FPS = 0

        pygame.mixer.music.play(-1)
        while self.len != 0:
            self.field.fill(black)
            text_y_dop = text_y0
            for i in self.collection:
                text = font.render(i, True, green)
                self.field.blit(text, (text_x0, text_y_dop))
                text_y_dop += 60

            if FPS % 5 == 0:
                stroka = f'{"".join(self.text[0:self.counter])}'
                text = font.render(stroka, True, green)
                self.counter += 1
                self.len -= 1
                self.field.blit(text, (text_x, text_y))
                screen.blit(self.field, (0, 0))
            if FPS == 60:
                FPS = 0

            if self.len == 0:
                self.collection.append(stroka)

            if self.len - 5 == 0:
                pygame.mixer.music.stop()

            FPS += 1
            pygame.display.flip()
            clock.tick(fps)

        text_y += 60

        self.text = text_six

        self.counter = 0
        self.len = len(self.text) + 1
        FPS = 0

        pygame.mixer.music.play(-1)
        while self.len != 0:
            self.field.fill(black)
            text_y_dop = text_y0
            for i in self.collection:
                text = font.render(i, True, green)
                self.field.blit(text, (text_x0, text_y_dop))
                text_y_dop += 60

            if FPS % 5 == 0:
                stroka = f'{"".join(self.text[0:self.counter])}'
                text = font.render(stroka, True, green)
                self.counter += 1
                self.len -= 1
                self.field.blit(text, (text_x, text_y))
                screen.blit(self.field, (0, 0))
            if FPS == 60:
                FPS = 0

            if self.len == 0:
                self.collection.append(stroka)

            if self.len - 5 == 0:
                pygame.mixer.music.stop()

            FPS += 1
            pygame.display.flip()
            clock.tick(fps)
