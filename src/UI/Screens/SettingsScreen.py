import pygame
from pygame import *

from src.Light.LightSourcesTypes import *
from src.Math.Transform import Transform
from src.Systems.Drawable import Drawable
from src.Systems.Updatable import Updatable
from src.UI.Editors.DirectionalLightEditor import DirectionalLightEditor
from src.UI.Editors.LightEditor import LightEditor
from src.UI.Editors.TransformEditor import TransformEditor
from src.UI.UIElements.Slider import Slider


class SettingsScreen(Drawable, Updatable):
    Instance = None

    def __init__(self, size: Vector2, position: Vector2):
        super().__init__()
        self.size = size
        self.position = position
        self.padding = 10
        self.elementWidth = self.size.x - self.padding * 2
        self.elementHeight = 40
        self.Rect = pygame.Rect(self.position, self.size)
        self.editors = []

    def open_editors_for(self, object_to_edit):
        """
        Opens UI editors for the given object basing on its components
        @param object_to_edit: Object to be edited
        """
        for e in self.editors:
            e.kill()
        self.editors.clear()
        curr = Vector2(self.position)
        curr.y += 30
        if isinstance(object_to_edit, Transform):
            e = TransformEditor((curr.x, curr.y), object_to_edit)
            self.editors.append(e)
            curr.y += e.get_height()

        if isinstance(object_to_edit, SkyboxLight) or isinstance(object_to_edit, PointLight):
            e = LightEditor((curr.x, curr.y), object_to_edit)
            self.editors.append(e)
            curr.y += e.get_height()
        elif isinstance(object_to_edit, DirectionalLight):
            e = DirectionalLightEditor((curr.x, curr.y), object_to_edit)
            self.editors.append(e)
            curr.y += e.get_height()
