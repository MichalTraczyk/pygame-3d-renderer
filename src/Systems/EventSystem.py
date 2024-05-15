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
    def GetAxis():
        axis = Vector2(0,0)
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] or keys[K_a]:
            axis.x -=1
        if keys[K_RIGHT] or keys[K_d]:
            axis.x += 1
        if keys[K_UP] or keys[K_w]:
            axis.y -= 1
        if keys[K_DOWN] or keys[K_s]:
            axis.y += 1

        return axis
    @staticmethod
    def AddOnQuitListener(listener):
        EventSystem.onQuit.append(listener)
    @staticmethod
    def FireOnQuitEvent():
        for listener in EventSystem.onQuit:
            listener()
    @staticmethod
    def Update():
        EventSystem.pressedDown.clear()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                EventSystem.pressedDown.append(event.key)
            elif event.type == QUIT:
                EventSystem.FireOnQuitEvent()
    @staticmethod
    def GetKeyDown(key):
        return key in EventSystem.pressedDown
