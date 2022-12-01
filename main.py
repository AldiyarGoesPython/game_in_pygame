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
x, y = 450, 450


class Rocket():
    pass


class Laser():
    pass


rect = pygame.Rect(0, 0, 20, 20)
rect.center = display.get_rect().center
base_vel = 1.5
vel_x = base_vel
vel_y = base_vel
max_vel = 4
change = 0.1
start_ticks = pygame.time.get_ticks()
while True:
    display.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    if seconds>30:
        base_vel +=0.5
        max_vel +=1
        change +=0.05
        start_ticks = pygame.time.get_ticks()
    keys = pygame.key.get_pressed()  # checking pressed keys
    rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel_x
    rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * vel_y
    if (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]) and vel_x < max_vel:
        vel_x += change
    else:
        if vel_x > base_vel:
            vel_x -= change
    if (keys[pygame.K_DOWN] or keys[pygame.K_UP]) and vel_y < max_vel:
        vel_y += change
    else:
        if vel_y > base_vel:
            vel_y -= change
    rect.centerx = rect.centerx % display.get_width()
    rect.centery = rect.centery % display.get_height()

    pygame.draw.rect(display, PINK, rect)
    pygame.display.update()
    clock.tick(fps)
