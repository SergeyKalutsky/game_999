import pygame as pg

storon1 = True
WIDTH, HEIGHT = 800, 800
WHITE = (255, 255, 255)
GREY = (127, 127, 127)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
FPS = 20
poskletgar = 0
poskletvis = 0
color = WHITE


def whisot(storon):
    global poskletgar
    if storon == True:
        poskletgar += 100
    else:
        poskletgar -= 100


def podsvet():
    global posX
    global posY
    global posXglb
    global posYglb
    pos = pg.mouse.get_pos()
    posX = pos[0]
    posY = pos[1]
    posX = posX // 100
    posY = posY // 100
    pg.draw.rect(screen, YELLOW, (posX * 100, posY * 100, 100, 100), 5)


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
pg.display.set_caption('Sha H Mati')
podsvet()
posXglb = posX
posYglb = posY

while True:
    for i in pg.event.get():
        if i.type == pg.MOUSEBUTTONDOWN:
            posXglb = posX
            posYglb = posY
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    pg.draw.rect(screen, color, (poskletgar, poskletvis, 100, 100))
    whisot(storon1)
    if poskletgar > 800:
        if color == WHITE:
            color = GREY
        else:
            color = WHITE
        storon1 = False
        poskletvis += 100
    elif poskletgar < 0:
        if color == WHITE:
            color = GREY
        else:
            color = WHITE
        storon1 = True
        poskletvis += 100
    if color == WHITE:
        color = GREY
    else:
        color = WHITE
    if poskletvis > 900:
        poskletvis = 0
    podsvet()
    pg.draw.rect(screen, YELLOW, (posXglb * 100, posYglb * 100, 100, 100), 10)
    pg.display.update()
    clock.tick(FPS)
