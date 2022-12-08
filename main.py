import pygame
import random
import sys

pygame.init()
display = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('NO ESCAPE')
pygame.display.set_icon(pygame.image.load('recruit-dance.gif'))
clock = pygame.time.Clock()
fps = 120
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
x, y = 450, 450
font = pygame.font.SysFont('Arial', 20)


class Bullet:
    def __init__(self):
        self.x = random.randint(0, 1200)
        self.end = random.randint(0, 1200)
        self.y = random.choice([0, 800])
        self.change_y = (800 - 2 * self.y) / 200
        self.change_x = (self.end - self.x) / 200


class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

        objects.append(self)

    def process(self):

        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

                else:
                    self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        display.blit(self.buttonSurface, self.buttonRect)


objects = []
check = False
over = False
set_check = False
mus_theme = '08cb5660-76e7-11ed-bc0a-eb032856cba0.wav'


def game():
    pygame.mixer.music.load(mus_theme)
    pygame.mixer.music.play(-1)
    global over, collide
    over = False
    global check
    check = False
    objects.clear()
    rect = pygame.Rect(0, 0, 20, 20)
    rect.center = display.get_rect().center
    base_vel = 2
    enemy_vel = 1
    enemy_count = 4
    vel_x = base_vel
    vel_y = base_vel
    max_vel = 5
    change = 0.03
    start_ticks = pygame.time.get_ticks()
    bullets = []
    killers = []
    for i in range(enemy_count):
        shoot = Bullet()
        bullets.append(shoot)
        killers.append(pygame.Rect(bullets[i].x, bullets[i].y, 30, 30))

    while True:
        display.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        if seconds > 12:
            base_vel += 0.5
            max_vel += 1
            change += 0.01
            enemy_vel += 0.1
            enemy_count += 1
            shoot = Bullet()
            bullets.append(shoot)
            killers.append(pygame.Rect(bullets[enemy_count - 1].x, bullets[enemy_count - 1].y, 30, 30))
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
        for i in range(enemy_count):
            killers[i].x += bullets[i].change_x * enemy_vel
            killers[i].y += bullets[i].change_y * enemy_vel
            pygame.draw.circle(display, RED, killers[i].center, 10)
        pygame.draw.circle(display, PINK, rect.center, 10, 2)
        pygame.display.update()
        clock.tick(fps)
        for i in killers:
            collide = rect.colliderect(i)
            if collide:
                break
        for i in range(enemy_count):
            if not 0 < killers[i].y < 800:
                shoot = Bullet()
                bullets[i] = shoot
                killers[i] = pygame.Rect(bullets[i].x, bullets[i].y, 30, 30)
        if collide:
            pygame.mixer.music.stop()
            over = True
            break
    start_button = Button(500, 50, 200, 100, 'Start the game', game, True)
    go_back_button = Button(500, 300, 200, 100, 'Back to menu', go_back, True)


def draw_text(text, size, color, x, y):
    txt_font = 'Slaytanic.ttf'
    txt_font = pygame.font.Font(txt_font, size)
    text_surface = txt_font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    display.blit(text_surface, text_rect)


def color_change(color, dir):
    for i in range(3):
        color[i] += col_spd * dir[i]
        if color[i] >= 255 or color[i] <= 0:
            dir[i] *= -1


def about():
    objects.clear()
    go_back_button = Button(500, 300, 200, 100, 'Back to menu', go_back, True)
    global check
    check = True


def setting():
    objects.clear()
    global set_check
    set_check = True
    go_back_button = Button(500, 500, 200, 100, 'Back to menu', go_back, True)
    music1 = Button(800, 300, 200, 100, "deadwood", opt1, True)
    music2 = Button(500, 300, 200, 100, 'rumble', opt2, True)
    music3 = Button(200, 300, 200, 100, 'boss', opt3, True)


def opt1():
    global mus_theme
    mus_theme = '08cb5660-76e7-11ed-bc0a-eb032856cba0.wav'


def opt2():
    global mus_theme
    mus_theme = 'a9b13060-76ea-11ed-b064-95ee47d4ceba.wav'


def opt3():
    global mus_theme
    mus_theme = '2bcb9db0-76eb-11ed-bbf7-8bea163bb517.wav'


def go_back():
    global check
    check = False
    global over
    over = False
    global set_check
    set_check = False
    objects.clear()
    settings = Button(500, 350, 200, 100, 'settings', setting, True)
    creator_button = Button(500, 200, 200, 100, 'About creator', about, True)
    start_button = Button(500, 50, 200, 100, 'Start the game', game, True)
    exitter = Button(500, 700, 200, 100, 'Exit', exit_button, True)


def exit_button():
    pygame.quit()
    sys.exit()


col_spd = 1
col_dir = [1, 1, 1]
def_col = [0, 128, 25]
creator_button = Button(500, 200, 200, 100, 'About creator', about, True)
start_button = Button(500, 50, 200, 100, 'Start the game', game, True)
exitter = Button(500, 700, 200, 100, 'Exit', exit_button, True)
settings = Button(500, 350, 200, 100, 'settings', setting, True)
while True:
    display.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for object in objects:
        object.process()
    if check:
        draw_text('Author - N I S student, Amanov Aldiyar', 40, def_col, 600, 200)
        color_change(def_col, col_dir)
    if over:
        draw_text('GAME OVER, YOU DIED', 40, RED, 600, 225)
    if set_check:
        draw_text('CHOOSE SONG', 40, YELLOW, 600, 150)
    pygame.display.update()
    clock.tick(fps)
