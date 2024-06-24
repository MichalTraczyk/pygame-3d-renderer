import pygame
from pygame import Vector2

from pygame.locals import (
    K_w,
    K_s,
    K_a,
    K_d,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


class EventSystem:
    onQuit = []
    pressedDown = []

    @staticmethod
    def get_axis():
        axis = Vector2(0, 0)
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] or keys[K_a]:
            axis.x -= 1
        if keys[K_RIGHT] or keys[K_d]:
            axis.x += 1
        if keys[K_UP] or keys[K_w]:
            axis.y -= 1
        if keys[K_DOWN] or keys[K_s]:
            axis.y += 1

        return axis

    @staticmethod
    def add_on_quit_listener(listener):
        EventSystem.onQuit.append(listener)

    @staticmethod
    def fire_on_quit_event():
        for listener in EventSystem.onQuit:
            listener()

    @staticmethod
    def update():
        EventSystem.pressedDown.clear()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                EventSystem.pressedDown.append(event.key)
            elif event.type == QUIT:
                EventSystem.fire_on_quit_event()

    @staticmethod
    def get_key_down(key):
        return key in EventSystem.pressedDown
