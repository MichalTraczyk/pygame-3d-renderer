from pygame import Vector2, Vector3

from src.UI.Editors.LightEditor import LightEditor
from src.UI.Editors.TransformEditor import TransformEditor
from src.UI.UIElements.Label import Label
from src.UI.UIElements.Slider import Slider


class DirectionalLightEditor(LightEditor):
    def __init__(self,position,target_light):
        super().__init__(position,target_light)
        ui_pos = Vector2(position[0],position[1] + super().get_height())
        t_pos = target_light.get_position()
        self.direction_label = Label((20, 20), (ui_pos.x, ui_pos.y), "dir: ")
        ui_pos.y += 20
        xLabel = Label((20, 20), (ui_pos.x, ui_pos.y), "x")
        min = -1
        max = 1
        ui_pos.x += 20
        self.xSlider = Slider((self.default_slider_size, 20), (ui_pos.x, ui_pos.y), min=min, max=max)
        self.xSlider.current_value = t_pos.x
        ui_pos.x -= 20
        ui_pos.y += 25

        yLabel = Label((20, 20), (ui_pos.x, ui_pos.y), "y")
        ui_pos.x += 20
        self.ySlider = Slider((self.default_slider_size, 20), (ui_pos.x, ui_pos.y), min=min, max=max)
        self.ySlider.current_value = t_pos.y
        ui_pos.x -= 20
        ui_pos.y += 25

        zLabel = Label((20, 20), (ui_pos.x, ui_pos.y), "z")
        ui_pos.x += 20
        self.zSlider = Slider((self.default_slider_size, 20), (ui_pos.x, ui_pos.y), min=min, max=max)
        self.zSlider.current_value = t_pos.z
        ui_pos.x -= 20
        ui_pos.y += 25
        self.xSlider.add_value_changed_listener(self.__refresh_direction)
        self.ySlider.add_value_changed_listener(self.__refresh_direction)
        self.zSlider.add_value_changed_listener(self.__refresh_direction)


        self.to_kill.append(xLabel)
        self.to_kill.append(self.xSlider)
        self.to_kill.append(yLabel)
        self.to_kill.append(self.ySlider)
        self.to_kill.append(zLabel)
        self.to_kill.append(self.zSlider)
        self.to_kill.append(self.direction_label)
        self._update(0)
        self.__refresh_direction(0)

    def __refresh_direction(self, val):
        xf = self.xSlider.current_value
        yf = self.ySlider.current_value
        zf = self.zSlider.current_value
        x = "{:.2f}".format(xf)
        y = "{:.2f}".format(yf)
        z = "{:.2f}".format(zf)
        self.direction_label.change_text(f"dir: ({x}, {y}, {z})")
        self.target.direction = Vector3(xf,yf,zf)

    def _update(self, deltaTime):
        dir = self.target.direction
        self.xSlider.current_value = dir.x
        self.ySlider.current_value = dir.y
        self.zSlider.current_value = dir.z

    def get_height(self):
        return 240

