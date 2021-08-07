import pygame as pg
from constants import WIDTH, HEIGHT, BLACK, YELLOW, FPS
from game_objects import Checker, Board

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
pg.display.set_caption('ШАШКИ!')


def podsvet():
    posX, posY = pg.mouse.get_pos()
    posX = posX // 70
    posY = posY // 70
    pg.draw.rect(screen, YELLOW, (20+posX * 70, 20+posY * 70, 70, 70), 3)


board = Board()
while True:
    screen.fill(BLACK)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            if board.board[(x//70, y//70)]:
                checker = board.board[(x//70, y//70)]
                if checker.highlite:
                    checker.highlite = False
                else:
                    checker.highlite = True

    board.update()
    board.draw(screen)
    podsvet()
    pg.display.update()
    clock.tick(FPS)
