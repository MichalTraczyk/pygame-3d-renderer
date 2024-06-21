from src.UI.Editors.Editor import Editor
from src.UI.UIElements.Slider import Slider


class LightEditor(Editor):
    def __init__(self,position, target_light):
        super().__init__(position)
        self.intensity_slider = Slider((100,20),position)
        self.target_light = target_light

    def update(self, deltaTime):
        self.target_light.intensity = self.intensity_slider.current_value

    def draw(self, screen, camera):
        super().draw(screen, camera)
    def kill(self):
        self.intensity_slider.kill()
        super().kill()
