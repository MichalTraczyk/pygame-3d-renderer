import pygame
from pygame import Vector2, Rect
from Systems.Drawable import Drawable
from Systems.EventSystem import EventSystem
from Systems.Updatable import Updatable


class Triangle(Updatable, Drawable):
    def __init__(self,pos):
        super().__init__()
        self.position = pos
        self.speed = 200

    def Update(self, deltaTime):
        move = EventSystem.GetAxis() * self.speed * deltaTime
        self.position += move

    def Draw(self, screen):
        rect = Rect(self.position.x - 15, self.position.y - 15, 30, 30)
        pygame.draw.rect(screen, (255, 0, 0), rect)
