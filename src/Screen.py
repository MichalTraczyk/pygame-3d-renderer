import pygame
from pygame import Vector2

from src.Camera import Camera
from src.Light.LightManager import LightManager
from src.Light.LightSourcesTypes import *
from src.MeshSystem.DrawableMesh import DrawableMesh
from src.MeshSystem.Primitives import Primitives
from src.UI.Screens.MainCanvas import MainCanvas
from src.Systems.Updater import Updater
from src.Systems.Drawer import Drawer
from src.Systems.EventSystem import EventSystem


class Screen:

    def __init__(self, res):
        self.resolution = res
        pygame.init()

        self.screen = pygame.display.set_mode([self.resolution, self.resolution])
        self.camera = Camera(60, self.resolution-150, self.resolution)

        self.running = True
        self.getTicksLastFrame = 0
        # p = Vector3(self.resolution, 0, self.resolution) / 2
        # self.tri = Triangle(p)

        mesh = Primitives.generate_box()
        obj = DrawableMesh(Vector3(0.2, 0, 2))
        obj.assignMesh(mesh)

        canvas = MainCanvas(Vector2(self.resolution,self.resolution))
        LightManager.add_change_listener(canvas.hierarchy.lights_changed)

        LightManager.register_light(PointLight(Vector3(-1, 0.5, 0.5), 0.9))
        LightManager.register_light(SkyboxLight(Vector3(0, 0, 0), 0.1))
        LightManager.register_light(SkyboxLight(Vector3(0, 0, 0), 0.1))
        #LightManager.register_light(DirectionalLight(Vector3(0,0,0),Vector3(1,-1,-1), 1))
        EventSystem.AddOnQuitListener(self.onQuit)
        while self.running:
            self.t = pygame.time.get_ticks()
            self.deltaTime = (self.t - self.getTicksLastFrame) / 1000.0
            self.getTicksLastFrame = self.t

            EventSystem.Update()

            if EventSystem.GetKeyDown(pygame.K_ESCAPE):
                self.onQuit()

            Updater.update(self.deltaTime)

            #obj.SetPosition(Vector3(math.sin(self.t / 1000), math.cos(self.t / 2000)-0.5, 1))
            obj.rotate(self.deltaTime*40)

            if Drawer.is_dirty:
                self.screen.fill((0, 0, 0))
                Drawer.draw(self.screen, self.camera)
                pygame.display.flip()
                # Drawer.is_dirty = False

        pygame.quit()

    def onQuit(self):
        self.running = False
