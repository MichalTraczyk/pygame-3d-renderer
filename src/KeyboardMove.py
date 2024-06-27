import math

import pygame
from pygame import Vector3, Vector2

from src.Math.Transform import Transform
from src.Math.VectorMath import VectorMath
from src.ModelPool import ModelPool
from src.Systems.EventSystem import EventSystem
from src.Systems.Updatable import Updatable


class KeyboardMove(Updatable):
    parent = None
    def __init__(self):
        super().__init__()
        self.parent = Transform()
        self.speed = 5
        self.sensitivity = 0.4
        KeyboardMove.parent = self.parent
        ModelPool.add_change_listener(self.modelpool_changed)
        self.last_mouse_position = pygame.mouse.get_pos()

    def modelpool_changed(self, pool):
        """
        Ensures that all models in the pool have the parent transform.

        @param pool: The model pool
        @type pool: list
        """
        for i in pool:
            if i.get_parent() is None:
                i.set_parent(self.parent)

    def _update(self, deltaTime):

        """
        Updates the position and rotation of the parent transform based on keyboard and mouse input

        @param deltaTime: The time elapsed since the last update.
        @type deltaTime: float
        """
        _input = -EventSystem.get_axis()
        self.parent.move_localy(_input * deltaTime * self.speed)
        if pygame.mouse.get_pressed()[2]:
            diff = pygame.mouse.get_pos()[0] - self.last_mouse_position[0]
            for child in self.parent.get_children():
                child.rotate(-diff * self.sensitivity)
            self.parent.rotate(-diff * self.sensitivity)
            v3 = self.parent.get_position()
            simple_diff = Vector2(v3.x, v3.z)
            dist = VectorMath.length(simple_diff)
            curr_angle = simple_diff.angle_to(Vector2(0, 1))
            curr_angle -= diff * self.sensitivity
            angle_rad = math.radians(curr_angle)
            new_position = Vector2(math.sin(angle_rad), math.cos(angle_rad))
            new_position *= dist
            n_pos_v3 = Vector3(new_position.x, v3.y,new_position.y)
            self.parent.set_local_position(n_pos_v3)

        self.last_mouse_position = pygame.mouse.get_pos()
