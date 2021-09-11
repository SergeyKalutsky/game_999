import pygame
from constants import BLUE, GREEN, BLACK, WIDTH, HEIGHT

class Button():
    def __init__(
            self, x, y, w, h, name,
            font_color=(169, 169, 169),
            normal_color=BLUE,
            highlight_color = GREEN,
            active_color=BLACK,
            size=24,
            font='Arial',
            padding=5
    ):
        self.state = 'normal'
        self.normal_color = normal_color
        self.highlight_color = highlight_color
        self.active_color = active_color
        self.name = name
        self.font = pygame.font.SysFont(font, size, True)
        self.text = self.font.render(name, True, font_color)
        self.image = pygame.Surface([w,h])
        self.image.fill(normal_color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.padding = padding

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, (self.rect.x + self.padding, self.rect.y + self.padding))


    def update(self):
        if self.state == 'normal':
            self.image.fill(self.normal_color)
        elif self.state == 'highlight':
            self.image.fill(self.highlight_color)
        elif self.state == 'active':
            self.image.fill(self.active_color)


    def handle_mouse_action(self, event=None):
        pos_x, pos_y = pygame.mouse.get_pos()
        check_pos = self.rect.left <= pos_x <= self.rect.right and self.rect.top <= pos_y <= self.rect.bottom
        if event == pygame.MOUSEMOTION:
            if check_pos:  self.state = 'highlight'
            else: self.state = 'normal'
        elif event == pygame.MOUSEBUTTONDOWN:
            if check_pos: self.state = 'active'
            else: self.state = 'normal'
        elif event == pygame.MOUSEBUTTONUP:
            if check_pos:  self.state = 'highlight'
            else: self.state = 'normal'


class MainMenu():
    def __init__(self, w, h):
        self.labels = [
            'START',
            'PICK COLOR THEME',
            'QUIT'
        ]
        self.x = (WIDTH - w) // 2
        self.y = (HEIGHT - h) // 2
        self.buttons = []
        button_height = int(h / (len(self.labels) + 1))
        current_y = self.y
        for label in self.labels:
            new_button = Button(self.x, current_y, w, button_height, label)
            current_y += button_height + 2
            self.buttons.append(new_button)

    def update(self):
        for button in self.buttons:
            button.update()

    def handle_mouse_event(self, event):
        for button in self.buttons:
            button.handle_mouse_action(event)
            if button.state == 'active':
                return button

    def draw(self, screen):
        for button in self.buttons:
            button.draw(screen)

