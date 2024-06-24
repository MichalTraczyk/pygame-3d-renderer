from pygame import *

from src.UI.UIElements.Label import Label
from src.UI.UIElements.UIElement import UIElement


class Button(UIElement):

    def __init__(self, size, position, text: str, text_size=15, label_color=Color(0, 0, 0), color=Color(210, 210, 210),
                 hover_color=Color(180, 180, 180), click_color=Color(240, 240, 240)):
        super().__init__(size, position)
        self.text = text
        self.on_click = []
        self.color = color
        self.hover_color = hover_color
        self.click_color = click_color
        self.current_color = self.color
        self.label = Label(self.size, self.position, self.text, label_color, text_size)
        self.rect = Rect(self.position, self.size)

    def kill(self):
        self.label.kill()
        super().kill()

    def add_listener(self, listener):
        self.on_click.append(listener)

    def remove_listener(self, listener):
        self.on_click.remove(listener)

    def _draw(self, screen, camera):
        draw.rect(screen, self.current_color, self.rect)

    def _on_pointer_up(self):
        self.current_color = self.hover_color
        for listener in self.on_click:
            listener()

    def _on_hover(self):
        self.current_color = self.hover_color

    def _on_unhover(self):
        self.current_color = self.color

    def _on_pointer_down(self):
        self.current_color = self.click_color
