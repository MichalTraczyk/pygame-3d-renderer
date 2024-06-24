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

    def _update(self, deltaTime):
        pos = pygame.mouse.get_pos()
        mouse_in_bounds = self.__contains(pos)
        is_pressed = pygame.mouse.get_pressed()[0]
        if mouse_in_bounds:
            if not self.was_in_bounds:
                self._on_hover()
            if is_pressed and not self.was_pressed:
                self._on_pointer_down()
            elif not is_pressed and self.was_pressed:
                self._on_pointer_up()
        elif self.was_in_bounds:
            self._on_unhover()

        self.was_in_bounds = mouse_in_bounds
        self.was_pressed = is_pressed

    def _on_pointer_down(self):
        """
        Event function called when the pointer starts a click on this object
        """
        pass

    def _on_hover(self):
        """
        Event function called when the pointer starts to hover this object
        """
        pass

    def _on_unhover(self):
        """
        Event function called when the pointer unhovers this object
        """
        pass

    def _on_pointer_up(self):
        """
        Event function called when the pointer stops a click on this object
        """
        pass

    def set_position(self, pos):
        """
        Sets the position of the element
        @param pos: New position of the element
        """
        self.position = pos

    def _draw(self, screen, camera):
        pygame.mouse.get_pos()

    def __contains(self, position):
        return self.position[0] < position[0] < self.size[0] + self.position[0] and self.position[1] < position[1] < \
            self.size[1] + self.position[1]
