from src.UI.Editors.LightEditor import LightEditor


class PointLightEditor(LightEditor):
    def __init__(self,position,target_light):
        super().__init__(position,target_light)