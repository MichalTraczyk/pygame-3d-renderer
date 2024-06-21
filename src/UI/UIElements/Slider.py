from pygame import Vector2, Rect, draw
import pygame
from src.UI.UIElements.UIElement import UIElement



class Slider(UIElement):
    def __init__(self, size, position, min=0.0, max=1.0):
        super().__init__(size, position)
        self.is_pressed = False
        self.current_value = (min + max) / 2
        self.outline = 2
        self.outrect = Rect(position, size)
        self.min = min
        self.max = max
        p = (position[0] + self.outline, position[1] + self.outline)
        s = (size[0] - self.outline * 2, size[1] - self.outline * 2)
        self.inrect = Rect(p, s)

    def update(self, deltaTime):
        super().update(deltaTime)
        if self.is_pressed:
            mouse_pos = pygame.mouse.get_pos()
            mouse_pos = self.get_normalized_mouse_position(mouse_pos)
            self.current_value = mouse_pos.x

    def draw(self, screen, camera):
        current_fill = (self.current_value - self.min) / self.max
        self.inrect.size = (current_fill*(self.size[0] - self.outline * 2),self.size[1] - self.outline * 2)
        draw.rect(screen, (180, 180, 180), self.outrect)
        draw.rect(screen, (210, 210, 210), self.inrect)

    def on_pointer_down(self):
        self.is_pressed = True

    def on_pointer_up(self):
        self.is_pressed = False

    def on_unhover(self):
        self.is_pressed = False

    def get_normalized_mouse_position(self, pos):
        v = Vector2(pos)
        v.x -= self.position[0]
        v.y -= self.position[1]
        return Vector2(v.x / self.size[0], v.y / self.size[1])