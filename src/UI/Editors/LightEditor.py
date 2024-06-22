from pygame import Vector2, Color

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
        self.intensity_slider.add_value_changed_listener(self.intensity_changed)
        start.y += 35
        start.x -= 20
        rLabel = Label((20, 20), (start.x, start.y), "r")
        start.x += 20
        self.rSlider = Slider((self.default_slider_size, 20), (start.x, start.y), min=0, max=255)
        self.rSlider.current_value = target_light.color[0]
        start.x -= 20
        start.y += 25

        gLabel = Label((20, 20), (start.x, start.y), "g")
        start.x += 20
        self.gSlider = Slider((self.default_slider_size, 20), (start.x, start.y), min=0, max=255)
        self.gSlider.current_value = target_light.color[1]
        start.x -= 20
        start.y += 25

        bLabel = Label((20, 20), (start.x, start.y), "b")
        start.x += 20
        self.bSlider = Slider((self.default_slider_size, 20), (start.x, start.y), min=0, max=255)
        self.bSlider.current_value = target_light.color[2]

        self.rSlider.add_value_changed_listener(self.color_changed)
        self.gSlider.add_value_changed_listener(self.color_changed)
        self.bSlider.add_value_changed_listener(self.color_changed)

        self.to_kill.append(rLabel)
        self.to_kill.append(gLabel)
        self.to_kill.append(bLabel)

        self.to_kill.append(self.rSlider)
        self.to_kill.append(self.gSlider)
        self.to_kill.append(self.bSlider)

        self.to_kill.append(self.intensity_slider)
        self.to_kill.append(self.label)

    def color_changed(self,v):
        self.target.color = Color(
            (int)(self.rSlider.current_value),
            (int)(self.gSlider.current_value),
            (int)(self.bSlider.current_value)
        )

    def intensity_changed(self, val):
        self.target.intensity = val
    def get_height(self):
        return 130