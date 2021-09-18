import pygame as pg
from constants import WIDTH, HEIGHT, BLACK, WHITE, YELLOW, FPS
from game_objects import Board, colors, themes, drawText
from game_menu import MainMenu
import video

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
pg.display.set_caption('ШАШКИ!')


def podsvet():
    posX, posY = pg.mouse.get_pos()
    posX = (posX - 20) // 70
    posY = (posY - 20) // 70
    if (0 <= posX < 8) and (0 <= posY < 8):
        pg.draw.rect(screen, YELLOW, (20 + posX * 70, 20 + posY * 70, 70, 70), 3)


wallpaper = pg.image.load("wallpaper.jpg")
menu = MainMenu(300, 200)
game_on = False
board = Board("Standart")
theme=0
video.run_vid()
run = True
while run:
    screen.fill(BLACK)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = not run

        if not game_on:
            btn = menu.handle_mouse_event(event.type)
            if btn:
                if btn.name == 'START':
                    game_on = True
                if btn.name == 'QUIT':
                    run = not run
                if btn.name == 'PICK COLOR THEME':
                    theme=(theme+1)%len(colors)
                    board.theme_change(themes[theme])
                    pg.display.set_caption('ШАШКИ! ('+themes[theme]+')')
        else:
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                x, y = (x - 20) // 70, (y - 20) // 70
                if (-1 < x < 8) and (-1 < x < 8):
                    if event.button == 1:
                        if board.board[(x, y)]:
                            board.remove_highlite()
                            checker = board.board[(x, y)]
                            if not checker.highlite:
                                checker.highlite = True
                            else:
                                checker.highlite = False
                        else:
                            board.update(x, y)

    menu.update()
    if game_on:
        board.draw(screen)
        podsvet()
        drawText(board.turn, pg.font.SysFont("Arial", 14), screen, 0, 0, WHITE)
    else:
        screen.blit(wallpaper, (0, 0))
        menu.draw(screen)
    pg.display.update()
    clock.tick(FPS)
pg.quit()
