from pygame import Color, Vector2, font

from src.Systems.Drawable import Drawable
from src.UI.UIElement import UIElement


class Label(Drawable):
    def __init__(self, size, position, text, color = (255,255,255)):
        super().__init__()
        self.text = text
        self.color = Color(color)
        self.position = position
        self.size = size
        self.font = font.SysFont("Arial", 36)
        self.textSurface = self.font.render(self.text, True, color)

    def draw(self, screen, camera):
        screen.blit(self.textSurface, self.position)
