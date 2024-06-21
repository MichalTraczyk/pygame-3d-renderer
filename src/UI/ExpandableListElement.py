from pygame import Rect

from src.UI.Button import Button


class ExpandableListElement(Button):
    def __init__(self, size, position, text: str):
        super().__init__(size, position, text)
    def set_position(self,new_position):
        self.position = new_position
        self.rect = Rect(self.position, self.size)