from pygame import Vector2

from src.Systems.Drawable import Drawable
from src.Systems.Updatable import Updatable
from src.UI.Screens.HierarchyScreen import HierarchyScreen
from src.UI.Screens.SettingsScreen import SettingsScreen


class MainCanvas(Updatable, Drawable):
    def __init__(self, resolution):
        super().__init__()
        self.ui_width = 200
        self.resolution = resolution
        self.hierarchy = HierarchyScreen(Vector2(self.ui_width, self.resolution[1]), Vector2(0, 0))
        self.settings = SettingsScreen(Vector2(self.ui_width, self.resolution[1]), Vector2(self.resolution[0] - 150, 0))
