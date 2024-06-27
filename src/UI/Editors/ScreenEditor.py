from pygame import Color, Vector2
from src.UI.UIElements.Label import Label
from src.UI.UIElements.Slider import Slider
from src.UI.Editors.Editor import Editor
from src.Camera import Camera

class ScreenEditor(Editor):
    def __init__(self, position):
        super().__init__(position, None)
        start = Vector2(position)
        start.y += 10

        fovLabel = Label((40, 20), (start.x, start.y), "FOV")
        start.x += 40

        self.fovSlider = Slider((self.default_slider_size, 20), (start.x, start.y), 30, 120)
        self.fovSlider.current_value = Camera.main_camera.fov

        self.fovSlider.add_value_changed_listener(self.__fov_changed)
    def __fov_changed(self, value : float):
        Camera.main_camera.set_fov(value)

    def get_height(self):
        return 50