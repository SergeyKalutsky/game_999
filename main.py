import pygame as pg


WIDTH, HEIGHT = 800, 800
FPS = 30

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
pg.display.set_caption('ШАШКИ!')

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    clock.tick(FPS)
        