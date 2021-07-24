import pygame as pg

WIDTH, HEIGHT = 600,600
WHITE=(255,255,255)
GREY=(127,127,127)
FPS = 30

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

class Checker(pg.sprite.Sprite):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color=(color+1)%2

    def update(self):
        self.draw()

    def draw(self):
        pg.draw.circle(screen, (abs(255*self.color-20),abs(255*self.color-20),abs(255*self.color-20)), (55+self.x*70, 55+self.y*70), 30)

pg.init()
screen = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption('Шашки')
clock = pg.time.Clock()
checker = Checker(1,0,1)
checker2 = Checker(7, 6, 0)
e=0
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    for i in range(8):
        for j in range(8):
            e=(i*8+j)-1
            pg.draw.rect(screen, (abs(255*((e+i)%2)), abs(255*((e+i)%2)), abs(255*((e+i)%2))), pg.Rect(20+j*70, 20+i*70, 70, 70))

    checker.update()
    checker2.update()
    pg.display.update()
    clock.tick(FPS)