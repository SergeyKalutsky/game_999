import pygame as pg


WIDTH, HEIGHT = 600, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 100, 100)
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


class Board:
    def __init__(self):
        self.board = {}
        self._fill_board()

    def _fill_board(self):
        for x in range(8):
            for y in range(8):
                self.board[(x, y)] = False

    def draw(self):
        for x in range(8):
            for y in range(8):
                color = pick_color(x, y)
                pg.draw.rect(screen, color, pg.Rect(20+x*70, 20+y*70, 70, 70))


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
    posX, posY = pg.mouse.get_pos()
    posX = posX // 70
    posY = posY // 70
    pg.draw.rect(screen, YELLOW, (20+posX * 70, 20+posY * 70, 70, 70), 3)


checker = Checker(3, 4)
board = Board()
board.board[(3, 4)] = True
while True:
    screen.fill(BLACK)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            if board.board[(x//70, y//70)]:
                if checker.highlite:
                    checker.highlite = False
                else:
                    checker.highlite = True
    board.draw()
    checker.draw()
    checker.update()
    podsvet()
    pg.display.update()
    clock.tick(FPS)
