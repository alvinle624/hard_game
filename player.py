from characters.base_character import _BaseCharacter
import pygame

class Player(_BaseCharacter):
    def __init__(self, win, x, y, w = 50, h = 100, move = 5):
        super().__init__(win, x, y)
        self.win = win
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.move = move

    def draw(self):
        pygame.draw.rect(self.win, (100, 0, 255), (self.x, self.y, 50, 50))

    def update(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.y > self.move:
            self.y -= self.move

        if keys[pygame.K_DOWN] and self.y < 800 - self.h - self.move:
            self.y += self.move

        if keys[pygame.K_RIGHT] and self.x < 800 - self.w - self.move:
            self.x += self.move

        if keys[pygame.K_LEFT] and self.x > self.move:
            self.x -= self.move