import pygame
from pygame import Vector2, Vector3

from src.Camera import Camera
from src.Systems.Updater import Updater
from src.Systems.Drawer import Drawer
from src.Systems.EventSystem import EventSystem
from Triangle import Triangle


class Screen:
    def __init__(self, res):
        self.resolution = res
        pygame.init()

        self.screen = pygame.display.set_mode([self.resolution, self.resolution])
        self.camera = Camera(30, self.resolution, self.resolution)

        self.running = True
        self.getTicksLastFrame = 0
        p = Vector3(self.resolution, 0, self.resolution) / 2
        self.tri = Triangle(p)

        while self.running:
            self.t = pygame.time.get_ticks()
            self.deltaTime = (self.t - self.getTicksLastFrame) / 1000.0
            self.getTicksLastFrame = self.t

            EventSystem.Update()

            if EventSystem.GetKeyDown(pygame.K_ESCAPE):
                self.onQuit()

            EventSystem.AddOnQuitListener(self.onQuit)
            Updater.Update(self.deltaTime)

            if Drawer.is_dirty:
                self.screen.fill((0, 0, 0))
                Drawer.Draw(self.screen, self.camera)
                Drawer.is_dirty = False
                pygame.display.flip()
        pygame.quit()

    def onQuit(self):
        self.running = False
