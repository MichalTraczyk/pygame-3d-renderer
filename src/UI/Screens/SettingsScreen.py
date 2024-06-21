import pygame
from pygame import *

from src.Systems.Drawable import Drawable
from src.Systems.Updatable import Updatable
from src.UI.UIElements.Slider import Slider


class SettingsScreen(Drawable, Updatable):
    Instance = None

    def __init__(self, size: Vector2, position: Vector2):
        super().__init__()
        self.size = size
        self.position = position
        self.padding = 10
        self.elementWidth = self.size.x - self.padding*2
        self.elementHeight = 40
        self.slider = Slider((self.elementWidth,self.elementHeight), (self.position.x+self.padding,self.position.y+self.padding), 0,1)
        self.Rect = pygame.Rect(self.position, self.size)