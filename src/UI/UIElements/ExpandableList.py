from pygame import Vector2

from src.UI.UIElements.ExpandableListElement import ExpandableListElement
from src.UI.UIElements.UIElement import UIElement


class ExpandableList(UIElement):
    def __init__(self, size, position):
        super().__init__(size, position)
        self.elements = []
        self.indent = 10
        self.listeners = []

    def add_element(self, element):
        self.elements.append(element)
        self.update_positions()
        for listener in self.listeners:
            element.add_listener(listener)

    def remove_element(self, element):
        self.elements.remove(element)
        self.update_positions()
        for listener in self.listeners:
            element.remove_listener(listener)

    def update_positions(self):
        curr_pos = Vector2(self.position[0] + self.indent, self.position[1] + 5)
        for element in self.elements:
            element.set_position((curr_pos.x, curr_pos.y))
            curr_pos.y += element.size[1] + self.indent

    def set_position(self, position):
        self.position = position
        self.update_positions()

    def add_select_listener(self, listener):
        self.listeners.append(listener)
        for element in self.elements:
            element.add_listener(listener)

    @staticmethod
    def get_default_element(size, text):
        return ExpandableListElement(size, (0, 0), text)
