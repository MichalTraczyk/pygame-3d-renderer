import pygame
from pygame import Vector2, Vector3

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
    QUIT, K_e,K_q
)


class EventSystem:
    __on_quit = []
    __pressed_down = []

    @staticmethod
    def get_axis():
        """
        Returns the active input axis where left and down arrows equal -1
        @return: Active input axis
        @rtype: Vector2
        """
        axis = Vector3(0, 0,0)
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] or keys[K_a]:
            axis.x -= 1
        if keys[K_RIGHT] or keys[K_d]:
            axis.x += 1
        if keys[K_UP] or keys[K_w]:
            axis.z += 1
        if keys[K_DOWN] or keys[K_s]:
            axis.z -= 1
        if keys[K_q]:
            axis.y += 1
        if keys[K_e]:
            axis.y -= 1

        return axis

    @staticmethod
    def add_on_quit_listener(listener):
        """
        Adds a listener for quit event
        @param listener: method to call on quit
        """
        EventSystem.__on_quit.append(listener)

    @staticmethod
    def __fire_on_quit_event():
        for listener in EventSystem.__on_quit:
            listener()

    @staticmethod
    def update():
        """
        Refreshes all inputs
        """
        EventSystem.__pressed_down.clear()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                EventSystem.__pressed_down.append(event.key)
            elif event.type == QUIT:
                EventSystem.__fire_on_quit_event()

    @staticmethod
    def get_key_down(key):
        """
        Returns True if the key is pressed
        @param key: key
        @return: True if the key is pressed
        @rtype: bool
        """
        return key in EventSystem.__pressed_down
