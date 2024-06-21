from pygame import *

from src.UI.Label import Label
from src.UI.UIElement import UIElement


class Button(UIElement):

    def __init__(self, size, position, text:str):
        super().__init__(size, position)
        self.text = text
        self.on_click = []
        self.color = Color(210,210,210)
        self.hover_color = Color(180,180,180)
        self.click_color = Color(240,240,240)
        self.current_color = self.color
        self.label = Label(self.size,self.position,self.text,(255,255,255))
        self.rect = Rect(self.position, self.size)

    def add_listener(self, listener):
        self.on_click.append(listener)
    def remove_listener(self, listener):
        self.on_click.remove(listener)

    def draw(self, screen, camera):
        if self.hidden:
            return
        draw.rect(screen, self.current_color, self.rect)

    def on_pointer_up(self):
        self.current_color = self.hover_color
        for listener in self.on_click:
            listener()

    def on_hover(self):
        self.current_color = self.hover_color

    def on_unhover(self):
        self.current_color = self.color

    def on_pointer_down(self):
        self.current_color = self.click_color

