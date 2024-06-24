from pygame import Vector2, Vector3

from src.Math.Transform import Transform
from src.UI.Editors.Editor import Editor
from src.UI.UIElements.Label import Label
from src.UI.UIElements.Slider import Slider


class TransformEditor(Editor):
    def __init__(self, position, target: Transform):
        super().__init__(position, target)
        min_position = -5
        max_position = 5
        ui_pos = Vector2(position)
        ui_pos.y += 12
        t_pos = target.get_position()
        xLabel = Label((20, 20), (ui_pos.x, ui_pos.y), "x")
        ui_pos.x += 20
        self.xSlider = Slider((self.default_slider_size, 20), (ui_pos.x, ui_pos.y), min=min_position, max=max_position)
        self.xSlider.current_value = t_pos.x
        ui_pos.x -= 20
        ui_pos.y += 25

        yLabel = Label((20, 20), (ui_pos.x, ui_pos.y), "y")
        ui_pos.x += 20
        self.ySlider = Slider((self.default_slider_size, 20), (ui_pos.x, ui_pos.y), min=min_position, max=max_position)
        self.ySlider.current_value = t_pos.y
        ui_pos.x -= 20
        ui_pos.y += 25

        zLabel = Label((20, 20), (ui_pos.x, ui_pos.y), "z")
        ui_pos.x += 20
        self.zSlider = Slider((self.default_slider_size, 20), (ui_pos.x, ui_pos.y), min=min_position, max=max_position)
        self.zSlider.current_value = t_pos.z
        ui_pos.x -= 20
        ui_pos.y += 25

        rotLabel = Label((20, 20), (ui_pos.x, ui_pos.y), "r")
        ui_pos.x += 20
        self.rotSlider = Slider((self.default_slider_size, 20), (ui_pos.x, ui_pos.y), min=0, max=360)
        self.rotSlider.current_value = target.get_rotation()

        self.xSlider.add_value_changed_listener(self.__slider_changed)
        self.ySlider.add_value_changed_listener(self.__slider_changed)
        self.zSlider.add_value_changed_listener(self.__slider_changed)
        self.rotSlider.add_value_changed_listener(self.__slider_changed)

        self.to_kill.append(xLabel)
        self.to_kill.append(self.xSlider)
        self.to_kill.append(yLabel)
        self.to_kill.append(self.ySlider)
        self.to_kill.append(zLabel)
        self.to_kill.append(self.zSlider)
        self.to_kill.append(rotLabel)
        self.to_kill.append(self.rotSlider)

    def __slider_changed(self, v):
        self.target.set_position(Vector3(
            self.xSlider.current_value,
            self.ySlider.current_value,
            self.zSlider.current_value
        ))
        self.target.set_local_rotation(self.rotSlider.current_value)

    def _update(self, deltaTime):
        p = self.target.get_position()
        self.xSlider.current_value = p.x
        self.ySlider.current_value = p.y
        self.zSlider.current_value = p.z
        self.rotSlider.current_value = self.target.get_rotation()

    def get_height(self):
        return 130

    def kill(self):
        for i in self.to_kill:
            i.kill()
        self.to_kill.clear()
        super().kill()
