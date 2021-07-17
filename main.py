import pygame as pg


WIDTH, HEIGHT = 600, 600
WHITE = (255, 255, 255)
GREY = (127, 127, 127)
FPS = 30

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
pg.display.set_caption('ШАШКИ!')


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


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    for i in range(8):
        for j in range(8):
            color = pick_color(i, j)
            pg.draw.rect(screen, color, pg.Rect(20+i*70, 20+j*70, 70, 70))

    pg.display.update()
    clock.tick(FPS)
