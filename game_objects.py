import pygame as pg
from constants import BLACK, RED, GREY, WHITE
import json

with open('colors.json', 'r') as f:
    colors = json.load(f)

themes = list(colors.keys())


def drawText(text, font, surface, x, y, color):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


class Checker:
    def __init__(self, x, y, color=BLACK):
        self.x = x
        self.y = y
        self.color = color
        self.highlite = False

    def draw(self, screen):
        pg.draw.circle(screen, self.color, (55+self.x*70, 55+self.y*70), 30)
        if self.highlite:
            pg.draw.circle(screen, RED, (55+self.x*70, 55+self.y*70), 30)


class Board:
    white_coords = [(1, 0), (3, 0), (5, 0), (7, 0),
                    (0, 1), (2, 1), (4, 1), (6, 1),
                    (1, 2), (3, 2), (5, 2), (7, 2)]
    black_coords = [(0, 5), (0, 7), (1, 6),
                    (2, 5), (2, 7), (3, 6), (4, 5),
                    (4, 7), (5, 6), (6, 5), (6, 7), (7, 6)]

    def __init__(self, theme):
        self.board = {}
        self.last_checker = [(None, None, None), (None, None, None)]
        self.turn = "WHITE"
        self.theme = theme
        self._fill_board()

    def _fill_board(self):
        for x in range(8):
            for y in range(8):
                if (x, y) in self.black_coords:
                    self.board[(x, y)] = Checker(
                        x, y, colors[self.theme]["BLACK"])
                elif (x, y) in self.white_coords:
                    self.board[(x, y)] = Checker(
                        x, y, colors[self.theme]["WHITE"])
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
                if color == WHITE:
                    pg.draw.rect(screen, colors[self.theme]["WHITE"], pg.Rect(
                        20 + x * 70, 20 + y * 70, 70, 70))
                elif color == GREY:
                    pg.draw.rect(screen, colors[self.theme]["GREY"], pg.Rect(
                        20 + x * 70, 20 + y * 70, 70, 70))
                else:
                    pass
                if self.board[(x, y)] is None:
                    continue
                self.board[(x, y)].draw(screen)

    def update(self, x, y):
        self.move_checker(x, y)
        self.remove_highlite()
        if self.last_checker != [(None, None, None), (None, None, None)]:
            aver_checker = self.board[((self.last_checker[0][0] + self.last_checker[1][0]) //
                                       2, (self.last_checker[0][1] + self.last_checker[1][1]) // 2)]
            if aver_checker and (aver_checker.x != self.last_checker[0][0]) and ((aver_checker.color != self.last_checker[0][2])):
                self.board[(aver_checker.x, aver_checker.y)] = None

    def move_checker(self, x, y):
        for key in self.board.keys():
            checker = self.board[key]
            if isinstance(checker, Checker):
                if checker.highlite and self.pick_color(x, y) == GREY:
                    if checker.color == colors[self.theme][self.turn]:
                        self.last_checker = [
                            (x, y, checker.color), (checker.x, checker.y, checker.color)]
                        checker.x, checker.y = x, y
                        self.board[(x, y)] = checker
                        self.board[key] = None
                        if self.turn == "WHITE":
                            self.turn = "BLACK"
                        elif self.turn == "BLACK":
                            self.turn = "WHITE"
                        break
                    else:
                        print("not ur tun, kiddo.")

    def remove_highlite(self):
        for x in range(8):
            for y in range(8):
                if self.board[(x, y)] is None:
                    continue
                self.board[(x, y)].highlite = False

    def theme_change(self, theme: str):
        for x in range(8):
            for y in range(8):
                checker = self.board[(x, y)]
                if checker and checker.color == colors[self.theme]["BLACK"]:
                    checker.color = colors[theme]["BLACK"]
                elif checker and checker.color == colors[self.theme]["WHITE"]:
                    checker.color = colors[theme]["WHITE"]
        self.theme = theme
