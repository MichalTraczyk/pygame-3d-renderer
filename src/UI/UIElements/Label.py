from pygame import Color, font

from src.Systems.Drawable import Drawable


class Label(Drawable):
    def __init__(self, size, position, text, color=(255, 255, 255), font_size= 15):
        super().__init__()
        self.color = Color(color)
        self.position = position
        self.size = size
        self.font = font.SysFont("Arial", font_size)
        self.color = color
        self.change_text(text)


    def draw(self, screen, camera):
        screen.blit(self.textSurface, self.position)
    def change_text(self, text):
        self.text = text
        self.textSurface = self.font.render(self.text, True, self.color)
    def set_position(self, pos):
        self.position = pos
