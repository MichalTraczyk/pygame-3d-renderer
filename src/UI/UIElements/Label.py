from pygame import Color, font

from src.Systems.Drawable import Drawable
from src.UI.UIElements.UIElement import UIElement


class Label(UIElement):
    def __init__(self, size, position, text, color=(255, 255, 255), font_size= 15):
        super().__init__(size,position)
        self.color = Color(color)
        self.position = position
        self.size = size
        self.font = font.SysFont("Arial", font_size)
        self.color = color
        self.change_text(text)


    def _draw(self, screen, camera):
        screen.blit(self.textSurface, self.position)
    def change_text(self, text):
        """
        Changes the text of the element
        @param text: New text
        """
        self.text = text
        self.textSurface = self.font.render(self.text, True, self.color)
