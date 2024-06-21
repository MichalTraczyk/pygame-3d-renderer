from pygame import Rect, Color

from src.Systems.Drawer import Drawer
from src.Systems.Updater import Updater
from src.UI.UIElements.Button import Button


class ExpandableListElement(Button):
    def __init__(self, size, position, text: str):
        super().__init__(size, position, text, label_color=(255, 255, 255), color=Color(0, 0, 0))
        self.selected = False
        self.select_color = Color(30, 30, 30)
        self.add_listener(self.select)
        self.target = None

    def set_position(self, new_position):
        self.position = new_position
        self.rect = Rect(self.position, self.size)
        self.label.set_position(new_position)

    def select(self, _ = None):
        self.selected = True

    def unselect(self):
        self.selected = False

    def draw(self, screen, camera):
        prev_color = self.current_color
        if self.selected and self.current_color == self.color:
            self.current_color = self.select_color
        super().draw(screen, camera)
        self.current_color = prev_color

    def on_pointer_up(self):
        self.current_color = self.hover_color
        for listener in self.on_click:
            listener(self)
