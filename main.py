import pygame as pg


WIDTH, HEIGHT = 600, 600
WHITE = (255, 255, 255)
GREY = (50, 50, 50)
FPS = 30

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
pg.display.set_caption('ШАШКИ!')

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    pg.draw.rect(screen, WHITE, pg.Rect(30, 30, 60, 60))
    pg.display.update()
    clock.tick(FPS)
        