from pygame import Vector2

from src.UI.Button import Button
from src.UI.UIElement import UIElement


class ExpandableList(UIElement):
    def __init__(self, size, position):
        super().__init__(size, position)
        self.expandButton = Button(self.position, (20, 20), "")
        self.expandButton.add_listener(self.expand_button_click)
        self.expanded = True
        self.elements = []
        self.indent = 10

    def add_element(self, element):
        self.elements.append(element)
        self.update_positions()
    def remove_element(self, element):
        self.elements.remove(element)
        self.update_positions()
    def update_positions(self):
        curr_pos = Vector2(self.position[0]+self.indent, self.position[1]+5)
        for element in self.elements:
            element.set_position(curr_pos)
            curr_pos.y += element.size[1] + self.indent
    def update(self, deltaTime):
        for element in self.elements:
            element.hidden = not self.expanded

    def expand_button_click(self):
        self.expanded = not self.expanded

    def expand(self):
        self.expanded = True

    def collapse(self):
        self.expanded = False
