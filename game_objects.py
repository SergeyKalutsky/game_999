import pygame as pg
from constants import BLACK, RED, GREY, WHITE


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

    def draw(self, screen):
        pg.draw.circle(screen, self.color, (55+self.x*70, 55+self.y*70), 30)


class Board:
    def __init__(self):
        self.board = {}
        self._fill_board()

    def _fill_board(self):
        for x in range(8):
            for y in range(8):
                if x == 3 and y == 4:
                    self.board[(x, y)] = Checker(x, y)
                else:
                    self.board[(x, y)] = None

    def pick_color(self, i, j):
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

    def draw(self, screen):
        for x in range(8):
            for y in range(8):
                color = self.pick_color(x, y)
                pg.draw.rect(screen, color, pg.Rect(20+x*70, 20+y*70, 70, 70))
                if self.board[(x, y)] is not None:
                    self.board[(x, y)].draw(screen)

    def highlite_checker(self, x, y):
        pass
