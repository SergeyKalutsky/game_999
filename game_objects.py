import json
import pygame as pg

with open('colors.json', 'r') as f:
    colors = json.load(f)

colors = colors['Jungle Awakens']


class Checker:
    def __init__(self, x, y, color=colors['BLACK']):
        self.x = x
        self.y = y
        self.last_x = x
        self.last_y = y
        self.color = color
        self.highlite = False

    def draw(self, screen):
        pg.draw.circle(screen, self.color, (55+self.x*70, 55+self.y*70), 30)
        if self.highlite:
            pg.draw.circle(screen, colors['CHOOSE'],
                           (55+self.x*70, 55+self.y*70), 30)


class Board:
    white_coords = [(1, 0), (3, 0), (5, 0), (7, 0),
                    (0, 1), (2, 1), (4, 1), (6, 1),
                    (1, 2), (3, 2), (5, 2), (7, 2)]
    black_coords = [(0, 5), (0, 7), (1, 6),
                    (2, 5), (2, 7), (3, 6), (4, 5),
                    (4, 7), (5, 6), (6, 5), (6, 7), (7, 6)]

    def __init__(self):
        self.last_moved_cheker = None
        self.board = {}
        self._fill_board()

    def _fill_board(self):
        for x in range(8):
            for y in range(8):
                if (x, y) in self.black_coords:
                    self.board[(x, y)] = Checker(x, y)
                elif (x, y) in self.white_coords:
                    self.board[(x, y)] = Checker(x, y, colors['WHITE'])
                else:
                    self.board[(x, y)] = None

    def pick_color(self, i, j):
        if i % 2 == 0:
            if j % 2 == 0:
                return colors['WHITE']
            else:
                return colors['GREY']
        else:
            if j % 2 == 0:
                return colors['GREY']
            else:
                return colors['WHITE']

    def draw(self, screen):
        for x in range(8):
            for y in range(8):
                color = self.pick_color(x, y)
                pg.draw.rect(screen, color, pg.Rect(20+x*70, 20+y*70, 70, 70))
                if self.board[(x, y)] is not None:
                    self.board[(x, y)].draw(screen)

    def update(self, x, y):
        self.move_checker(x, y)
        self.remove_highlite()

    def move_checker(self, x, y):
        for key in self.board.keys():
            checker = self.board[key]
            if isinstance(checker, Checker):
                if checker.highlite:
                    if self.pick_color(x, y) == colors['GREY']:
                        checker.x, checker.y = x, y
                        self.board[(x, y)] = checker
                        self.board[key] = None
                        self.last_moved_cheker = checker
                        break

    def remove_highlite(self):
        for x in range(8):
            for y in range(8):
                if self.board[(x, y)] is not None:
                    self.board[(x, y)].highlite = False
