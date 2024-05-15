import pygame
from pygame import Vector2

from Systems.Updater import Updater
from Systems.Drawer import Drawer
from Systems.EventSystem import EventSystem
from Triangle import Triangle


class Screen:
    def __init__(self, res):
        self.resolution = res
        pygame.init()
        self.screen = pygame.display.set_mode([self.resolution, self.resolution])
        self.running = True
        self.getTicksLastFrame = 0
        p = Vector2(self.resolution, self.resolution)/2
        self.tri = Triangle(p)
        while self.running:
            self.t = pygame.time.get_ticks()
            self.deltaTime = (self.t - self.getTicksLastFrame) / 1000.0
            self.getTicksLastFrame = self.t

            EventSystem.Update()

            if EventSystem.GetKeyDown(pygame.K_ESCAPE):
                self.onQuit()

            EventSystem.AddOnQuitListener(self.onQuit)
            self.screen.fill((0, 0, 0))

            Updater.Update(self.deltaTime)
            Drawer.Draw(self.screen)
            pygame.display.flip()
        pygame.quit()

    def onQuit(self):
        self.running = False