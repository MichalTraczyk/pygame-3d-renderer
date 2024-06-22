from pygame import Vector2

from src.UI.Editors.Editor import Editor
from src.UI.UIElements.Label import Label
from src.UI.UIElements.Slider import Slider


class LightEditor(Editor):
    def __init__(self, position, target_light):
        super().__init__(position, target_light)
        start = Vector2(position)
        start.y += 10
        self.label = Label((20, 20), (start.x, start.y), "i", color=(255, 255, 255))
        start.x += 20
        self.intensity_slider = Slider((self.default_slider_size, 20), (start.x, start.y))
        self.intensity_slider.current_value = target_light.intensity
        self.to_kill.append(self.intensity_slider)
        self.to_kill.append(self.label)
    def intensity_changed(self, val):
        self.target.intensity = val

    def get_height(self):
        return 40