from pygame import Vector2, Color

from src.UI.Editors.Editor import Editor
from src.UI.UIElements.Label import Label
from src.UI.UIElements.Slider import Slider


class MeshEditor(Editor):

    def __init__(self, position, target_mesh):
        super().__init__(position, target_mesh)
        start = Vector2(position)
        start.y += 10

        rLabel = Label((20, 20), (start.x, start.y), "r")
        start.x += 20
        self.rSlider = Slider((self.default_slider_size, 20), (start.x, start.y), min=0, max=255)
        self.rSlider.current_value = target_mesh.mesh.color[0]
        start.x -= 20
        start.y += 25

        gLabel = Label((20, 20), (start.x, start.y), "g")
        start.x += 20
        self.gSlider = Slider((self.default_slider_size, 20), (start.x, start.y), min=0, max=255)
        self.gSlider.current_value = target_mesh.mesh.color[1]
        start.x -= 20
        start.y += 25

        bLabel = Label((20, 20), (start.x, start.y), "b")
        start.x += 20
        self.bSlider = Slider((self.default_slider_size, 20), (start.x, start.y), min=0, max=255)
        self.bSlider.current_value = target_mesh.mesh.color[2]

        self.rSlider.add_value_changed_listener(self.__color_changed)
        self.gSlider.add_value_changed_listener(self.__color_changed)
        self.bSlider.add_value_changed_listener(self.__color_changed)

        self.to_kill.append(rLabel)
        self.to_kill.append(gLabel)
        self.to_kill.append(bLabel)

        self.to_kill.append(self.rSlider)
        self.to_kill.append(self.gSlider)
        self.to_kill.append(self.bSlider)

    def __color_changed(self, v):
        self.target.mesh.color = Color(
            int(self.rSlider.current_value),
            int(self.gSlider.current_value),
            int(self.bSlider.current_value)
        )

    def get_height(self):
        return 100
