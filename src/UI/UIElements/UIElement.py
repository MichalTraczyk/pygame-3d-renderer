import pygame.mouse
from pygame import Vector2

from src.Systems.Drawable import Drawable
from src.Systems.Updatable import Updatable


class UIElement(Updatable, Drawable):
    def __init__(self, size, position):
        super().__init__()
        self.size = size
        self.position = position
        self.was_pressed = False
        self.was_in_bounds = False

    def update(self, deltaTime):
        pos = pygame.mouse.get_pos()
        mouse_in_bounds = self.contains(pos)
        is_pressed = pygame.mouse.get_pressed()[0]
        if mouse_in_bounds:
            if not self.was_in_bounds:
                self.on_hover()
            if is_pressed and not self.was_pressed:
                self.on_pointer_down()
            elif not is_pressed and self.was_pressed:
                self.on_pointer_up()
        elif self.was_in_bounds:
            self.on_unhover()

        self.was_in_bounds = mouse_in_bounds
        self.was_pressed = is_pressed

    def on_pointer_down(self):
        pass

    def on_hover(self):
        pass

    def on_unhover(self):
        pass

    def on_pointer_up(self):
        pass

    def draw(self, screen, camera):
        pygame.mouse.get_pos()

    def contains(self, position):
        return self.position[0] < position[0] < self.size[0] + self.position[0] and self.position[1] < position[1] < self.size[1] + self.position[1]
