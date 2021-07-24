from _typeshed import ReadableBuffer
import pygame as pg


WIDTH, HEIGHT = 600, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0 )
GREY = (127, 127, 127)
FPS = 30

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
pg.display.set_caption('ШАШКИ!')


class Checker:
    def __init__(self, x, y, color=BLACK):
        self.x = x
        self.y = y
        self.default_color = color
        self.color = color
        self.highlite = False
    
    def update(self):
        if self.highlite:
            self.color = RED
        else:
            self.color = self.default_color

    def draw(self):
        pg.draw.circle(screen, self.color, (55+self.x*70, 55+self.y*70), 30)


def pick_color(i, j):
    if i % 2 == 0:
        if j % 2 == 0:
            return WHITE
        else:
            return GREY
    else:
        if j % 2 == 0:
            return GREY
        else:
            return WHITE


def podsvet():
    global posX, posY
    pos = pg.mouse.get_pos()
    posX = pos[0]
    posY = pos[1]
    posX = posX // 70
    posY = posY // 70
    pg.draw.rect(screen, YELLOW, (20+posX * 70, 20+posY * 70, 70, 70), 5)


checker = Checker(3, 4)
while True:
    screen.fill(BLACK)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    for i in range(8):
        for j in range(8):
            color = pick_color(i, j)
            pg.draw.rect(screen, color, pg.Rect(20+i*70, 20+j*70, 70, 70))

    checker.draw()
    podsvet()
    pg.display.update()
    clock.tick(FPS)
