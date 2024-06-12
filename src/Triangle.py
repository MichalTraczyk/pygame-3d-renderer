import pygame
from pygame import Vector2, Rect, Vector3
from Systems.EventSystem import EventSystem
from Systems.Updatable import Updatable
from Systems.Drawable import (Drawable)
from src.Math.Transform import Transform


class Triangle(Updatable, Drawable,Transform):
    def __init__(self,pos):
        super().__init__()
        self.SetPosition(pos)
        self.speed = 200

    def Update(self, deltaTime):
        move = EventSystem.GetAxis() * self.speed * deltaTime
        self.Move(Vector3(move.x,0,move.y))

    def Draw(self, screen):
        pos = self.GetPosition()
        rect = Rect(pos.x - 15, pos.z - 15, 30, 30)
        pygame.draw.rect(screen, (255, 0, 0), rect)
