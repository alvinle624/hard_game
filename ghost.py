from characters.base_character import _BaseCharacter
import pygame

class Ghost(_BaseCharacter):
    def __init__(self, win, x, y, r, speed=5, direction=-1):
        super().__init__(win, x, y)
        self.r = r
        self.speed = speed
        self.direction = direction

    def draw(self):
        pygame.draw.circle(self.win, (200, 0, 0), (self.x, self.y), 15, 0)

    def update(self):
        self.y += self.direction*self.speed

        if self.y >= 780 and self.direction == 1:
            self.direction *= -1

        if self.y <= 20 and self.direction == -1:
            self.direction *= -1


