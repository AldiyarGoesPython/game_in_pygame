import pygame
import random
pygame.init()
display = pygame.display.set_mode((600, 600))
pygame.display.set_caption('NO ESCAPE')
clock = pygame.time.Clock()
fps = 120
class Player():
    pass
class Rocket():
    pass
class Laser():
    pass
while True:
    pygame.display.flip()
    clock.tick(fps)
    