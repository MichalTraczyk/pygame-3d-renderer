import pygame
import pygame_gui
from pygame import *

from src.Systems.Drawable import Drawable
from src.Systems.Updatable import Updatable
from src.UI.Button import Button
from src.UI.ExpandableList import ExpandableList
from src.UI.ExpandableListElement import ExpandableListElement
from src.UI.Slider import Slider


class SettingsScreen(Drawable, Updatable):
    Instance = None

    def __init__(self, size: Vector2, position: Vector2):
        super().__init__()
        self.size = size
        self.position = position
        self.padding = 10
        self.elementWidth = self.size.x - self.padding*2
        self.elementHeight = 40
        self.button = Button((self.elementWidth,self.elementHeight), (self.position.x+self.padding,self.position.y+100+self.padding), "Import")
        self.slider = Slider((self.elementWidth,self.elementHeight), (self.position.x+self.padding,self.position.y+self.padding), 0,1)
        self.Rect = pygame.Rect(self.position, self.size)
        self.exList = ExpandableList((self.elementWidth,300), (self.position.x+self.padding,self.position.y+self.padding))
        el = ExpandableListElement((self.elementWidth,self.elementHeight),(0,0),"dupa1")
        el1 = ExpandableListElement((self.elementWidth,self.elementHeight),(0,0),"dupa2")
        el2 = ExpandableListElement((self.elementWidth,self.elementHeight),(0,0),"dupa3")
        self.exList.add_element(el)
        self.exList.add_element(el1)
        self.exList.add_element(el2)