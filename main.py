import pygame
import random
import sys
pygame.init()
display = pygame.display.set_mode((900, 900))
pygame.display.set_caption('NO ESCAPE')
clock = pygame.time.Clock()
fps = 120
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
x, y, x_c, y_c = 0, 0, 0, 0

class Player():
    pass
class Rocket():
    pass
class Laser():
    pass
while True:
    display.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x_c > -5:
                    x_c -= 1
            elif event.key == pygame.K_RIGHT:
                if x_c < 5:
                    x_c += 1
            elif event.key == pygame.K_UP:
                if y_c > -5:
                    y_c -= 1
            elif event.key == pygame.K_DOWN:
                if y_c < 5:
                    y_c += 1
    if 880 > x > 0:
        x += x_c
    if 880 > y > 0:
        y += y_c
    pygame.draw.rect(display, PINK, (x, y, 20, 20))
    pygame.display.update()
    clock.tick(fps)
