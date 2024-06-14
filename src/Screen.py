import math

import pygame
from pygame import Vector2, Vector3

from src.Camera import Camera
from src.Light.LightManager import LightManager
from src.Light.LightSourcesTypes import *
from src.MeshSystem.DrawableMesh import DrawableMesh
from src.MeshSystem.Primitives import Primitives
from src.Systems.Updater import Updater
from src.Systems.Drawer import Drawer
from src.Systems.EventSystem import EventSystem


class Screen:

    def __init__(self, res):
        self.resolution = res
        pygame.init()

        self.screen = pygame.display.set_mode([self.resolution, self.resolution])
        self.camera = Camera(60, self.resolution, self.resolution)

        self.running = True
        self.getTicksLastFrame = 0

        mesh = Primitives.generate_box()
        obj = DrawableMesh(Vector3(2, 0, 2))
        obj.assign_mesh(mesh)
        obj.rotate(10)
        obj = DrawableMesh(Vector3(-1, 1, 1.7))
        obj.assign_mesh(mesh)
        obj.rotate(45)
        obj = DrawableMesh(Vector3(-0.5, -2, 0.8))
        obj.assign_mesh(mesh)
        obj = DrawableMesh(Vector3(1, -2, 2))
        obj.assign_mesh(Primitives.generate_rotated_pyramid())

        #LightManager.register_light(PointLight(Vector3(-1, 0.5, 0.5), 0.9, Color(255, 0, 0)))
        #LightManager.register_light(PointLight(Vector3(2, 0.5, 0.5), 0.9, Color(0, 255, 0)))
        LightManager.register_light(SkyboxLight(Vector3(0, 0, 0), 0.1, Color(255, 255, 200)))
        LightManager.register_light(DirectionalLight(Vector3(0,0,0),Vector3(1,-1,1), 0.5,Color(255,255,255)))

        while self.running:
            self.t = pygame.time.get_ticks()
            self.deltaTime = (self.t - self.getTicksLastFrame) / 1000.0
            self.getTicksLastFrame = self.t

            EventSystem.Update()

            if EventSystem.GetKeyDown(pygame.K_ESCAPE):
                self.onQuit()

            EventSystem.AddOnQuitListener(self.onQuit)
            Updater.update(self.deltaTime)

            # obj.set_position(Vector3(math.sin(self.t / 400), math.cos(self.t / 400)-0.5, 3))
            # obj.rotate(self.deltaTime*200)

            if Drawer.is_dirty:
                self.screen.fill((0, 0, 0))
                Drawer.draw(self.screen, self.camera)
                pygame.display.flip()
                # Drawer.is_dirty = False

        pygame.quit()

    def onQuit(self):
        self.running = False
