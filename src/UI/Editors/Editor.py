import pygame.draw
from pygame import Rect

from src.Systems.Drawable import Drawable
from src.Systems.Updatable import Updatable


class Editor(Updatable, Drawable):
    def __init__(self, position, target):
        super().__init__()
        self.target = target
        self.position = position
        self.rect = Rect((position[0] - 4,position[1] - 4), (150, self.get_height()))
        self.to_kill = []
        self.default_slider_size = 105

    def get_height(self):
        return 70

    def draw(self, screen, camera):
        pygame.draw.rect(screen, (210, 210, 210), self.rect, 2)

    def kill(self):
        for i in self.to_kill:
            i.kill()
        super().kill()
