import pygame
pygame.init()

from characters.ghost import Ghost
from characters.player import Player

win = pygame.display.set_mode((800, 800))

pygame.display.set_caption("Game")

on = True

monster3 = Ghost(win, 500, 20, 15)
monster2 = Ghost(win, 300, 20, 15)
monster = Ghost(win, 400, 780, 15, 5, 1)
player = Player(win, 0, 0, 50, 50)

while on:
    pygame.time.delay(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False

    #board background
    win.fill((0, 0, 0))

    pygame.draw.rect(win, (255, 255, 255), (0, 0, 200, 800))
    pygame.draw.rect(win, (255, 255, 255), (600, 0, 200, 800))

    player.update()
    player.draw()

    monster.update()
    monster.draw()
    monster2.update()
    monster2.draw()
    monster3.update()
    monster3.draw()

    pygame.display.update()
    pygame.display.flip()

pygame.quit()


# if __name__ == "__main__":
#     main()