import pygame as pg
from constants import WIDTH, HEIGHT, BLACK, WHITE, YELLOW, FPS
from game_objects import Board

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
pg.display.set_caption('ШАШКИ!')


def podsvet():
    posX, posY = pg.mouse.get_pos()
    posX = (posX - 20) // 70
    posY = (posY - 20) // 70
    if (0 <= posX < 8) and (0 <= posY < 8):
        pg.draw.rect(screen, YELLOW, (20 + posX *
                     70, 20 + posY * 70, 70, 70), 3)


l_checker = [(None, None, None), (None, None, None)]
board = Board()
run = True
while run:
    screen.fill(BLACK)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = not run

        if event.type == pg.MOUSEBUTTONDOWN:
            
            x, y = pg.mouse.get_pos()
            x, y = (x - 20) // 70, (y - 20) // 70
            if event.button == 1:
                if board.board[(x, y)]:
                    board.remove_highlite()
                    checker = board.board[(x, y)]
                    if not checker.highlite:
                        checker.highlite = True
                        # l_checker - Послденяя ходившая шашка
                        l_checker[0] = (x, y, board.board[(x, y)].color)
                    else:
                        checker.highlite = False
                                    # сейчас              шаг назад
                        l_checker = [(None, None, None), (None, None, None)]
                else:
                    board.update(x, y)
                    if board.pick_color(x, y) != WHITE:
                        l_checker[1] = l_checker[0]
                        l_checker[0] = (x, y, board.board[(x, y)].color)
                        # Съедание шашки
                        aver_checker = board.board[((l_checker[0][0]+l_checker[1][0])//2, (l_checker[0][1]+l_checker[1][1])//2)]
                        if aver_checker and ((aver_checker.x != l_checker[0][0])) and ((aver_checker.color != l_checker[0][2])):
                            board.board[
                                ((l_checker[0][0] + l_checker[1][0]) // 2, (l_checker[0][1] + l_checker[1][1]) // 2)] = None

            if event.button == 3:
                board.remove_highlite()
                board.board[(x, y)] = None
                # HOMEWORK
    board.draw(screen)
    podsvet()
    pg.display.update()
    clock.tick(FPS)
pg.quit()
